;; btlp_activate, queued path for texture areas that the window code clears (see vwf_btlp_activate.asm).
;; Lives in three dead BTLP functions (tools/deadovl.py): A 0x800AAFEC (24 instr), B 0x800663F0 (18), C 0x8007D6CC (8).
;;
;; The VWF engine reports every cell a glyph touches, so a text of N glyphs reports ~1.6 N cells, most of them the SAME
;; cell again with more pixels. The original glyph function queued one LoadImage (BTLP_LQUEUE, circular queue of 72
;; entries; the flush loads entries 0..count-1) and used one glyph-ring slot (0x800EBE48, 128 B each, no bound) per glyph.
;; Queuing every report overflowed both: a choice window with 3 answers of ~50 glyphs wrapped the queue (the flush then loads
;; only the last count-72 entries: blank answers with a few cells of the last one) and the ring ran into the GPU
;; packet area behind it (0x800EEB48).  Fix: before allocating, look at the last 4 queue entries; a cell that is already
;; queued (same VRAM x,y) just gets its pending ring slot overwritten with the newer pixels.
;;
;; in: a1 = engine ring cell, t3 = x, t5 = y (VRAM), s0/s1 = cfg / text struct, sp = btlp_activate frame
;; out: j btlp_act_sprites (its first instruction, sw zero,BTCFG_COUNT(s0), sits in the delay slot of the jump)

;; ---- A: scan the newest queue entries ----
.org 0x800AAFEC
.area 0x800AB04C - 0x800AAFEC
btlp_act_queue:
    lui     t6, 0x800D
    lw      t7, -0x78BC(t6)            ; queue count n
    lui     t8, 0x800F
    sll     t0, t7, 1
    addu    t0, t0, t7
    sll     t0, t0, 2                  ; 12 n
    addu    t0, t0, t8
    addiu   t0, t0, -0x53BC            ; &entry[n-1]  (entries: 0x800EAC50, {u16 x, y, w, h; u32 src})
    li      t1, 4
@@scan:
    lhu     t2, 0(t0)
    lhu     t4, 2(t0)
    xor     t2, t2, t3
    xor     t4, t4, t5
    or      t2, t2, t4                 ; 0 = same cell
    beqz    t2, @@found
    addiu   t1, t1, -1
    bnez    t1, @@scan
    addiu   t0, t0, -12
    j       btlp_act_new               ; not queued yet: allocate a ring slot
    lw      t7, -0x41BC(t8)            ; glyph counter
@@found:
    j       btlp_act_copy              ; reuse its slot
    lw      t9, 8(t0)
.endarea

;; ---- B: ring slot, copy, queue ----
.org 0x800663F0
.area 0x80066438 - 0x800663F0
btlp_act_new:
    sll     t9, t7, 7
    addiu   t6, t8, -0x41B8            ; ring base
    addu    t9, t9, t6                 ; destination slot
    addiu   t7, t7, 1
    sw      t7, -0x41BC(t8)
btlp_act_copy:                         ; t9 = slot, t2 = 0 when the cell was already queued
    addiu   t4, a1, CELL_BYTES
    move    a0, t9
@@loop:
    lw      t0, 0(a1)
    addiu   a1, a1, 4
    addiu   t9, t9, 4
    bne     a1, t4, @@loop
    sw      t0, -4(t9)
    bnez    t2, @@queue
    move    a1, t3                     ; x
    j       btlp_act_sprites + 4       ; already queued: only the slot changed
    sw      zero, BTCFG_COUNT(s0)      ; = first instruction of btlp_act_sprites
@@queue:
    j       btlp_act_queue2
    li      t0, 16
.endarea

;; ---- C ----
.org 0x8007D6CC
.area 0x8007D6EC - 0x8007D6CC
btlp_act_queue2:
    move    a2, t5                     ; y
    sw      t0, 0x10(sp)               ; h
    jal     BTLP_LQUEUE
    li      a3, 4                      ; w (16 px of 4bpp)
    j       btlp_act_sprites + 4
    sw      zero, BTCFG_COUNT(s0)
.endarea
