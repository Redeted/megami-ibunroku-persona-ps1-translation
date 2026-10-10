;; =============================================================
;; Variable-width font engine - glyph compositing and cell upload
;; (second half of vwf_dialog.asm; placed in its own SLPS block)
;; =============================================================

;; -------------------------------------------------------------
;; vwf_dialog_draw - internal to vwf_dialog_emit (shares its frame).
;; In: a0 glyph rows, a1 row format, s0 line, s2 px, s3 advance, s5 config.
;; Clears newly touched ring cells, composites the glyph (shadow +2,+1),
;; queues the touched cells for upload and activates them in the map.
;; -------------------------------------------------------------
vwf_dialog_draw:
    sw      ra, 0x0C(sp)

    ; --- touched cells: px>>4 .. min(14, (px+adv+2)>>4) ---
    srl     t6, s2, 4                   ; t6 = first cell
    addu    t7, s2, s3
    addiu   t7, t7, 2
    srl     t7, t7, 4
    sltiu   t0, t7, DLG_BOX_COLS
    bnez    t0, @@last_ok
    nop
    li      t7, DLG_BOX_COLS - 1
@@last_ok:
    la      t4, vwf_dlg_state
    sh      t7, DLG_LAST(t4)
    lh      t5, DLG_INIT(t4)            ; highest cell already cleared
    move    t0, t6
@@prep:                                 ; clear ring cells entered for the first time
    slt     t1, t5, t0
    beqz    t1, @@prep_next
    andi    t1, t0, RING_CELLS - 1
    sll     t1, t1, 7
    la      t2, vwf_dlg_ring
    addu    t2, t2, t1
    addiu   t3, t2, CELL_BYTES
@@clear:
    sw      zero, 0(t2)
    addiu   t2, t2, 4
    bne     t2, t3, @@clear
    nop
    move    t5, t0
@@prep_next:
    addiu   t0, t0, 1
    slt     t1, t7, t0
    beqz    t1, @@prep
    nop
    sh      t5, DLG_INIT(t4)

    ; --- rows: narrow = rows 1-14 (1 byte each), wide = rows 0-15 (2 bytes) ---
    addiu   t8, a1, 15                  ; end row: 15 narrow, 16 wide
    beqz    a1, @@row
    li      t0, 1                       ; narrow start row
    move    t0, zero                    ; wide start row
@@row:
    beqz    a1, @@row_narrow
    nop
    lbu     t1, 0(a0)
    lbu     t2, 1(a0)
    sll     t1, t1, 8
    or      t1, t1, t2                  ; t1 = 16-bit row, MSB = left
    j       @@row_bits
    addiu   a0, a0, 2
@@row_narrow:
    lbu     t1, 0(a0)
    addiu   a0, a0, 1
    sll     t1, t1, 8
@@row_bits:
    beqz    t1, @@row_next
    move    t2, zero                    ; t2 = bit index
@@bit:
    li      t3, 0x8000
    srlv    t3, t3, t2
    and     t3, t3, t1
    beqz    t3, @@bit_next
    nop
    la      t4, vwf_dlg_state           ; colours / shadow offset are per overlay (DLG_COLOR_*, set by the caller)
    lbu     t9, DLG_COLOR_MAIN(t4)
    addu    a2, s2, t2                  ; main pixel at (px+bit, row)
    jal     vwf_dialog_plot
    move    a3, t0
    sltiu   t3, t0, 15                  ; shadow pixel at (px+bit+dx, row+1)
    beqz    t3, @@bit_next
    nop
    la      t4, vwf_dlg_state
    lbu     a2, DLG_SHADOW_DX(t4)
    lbu     t9, DLG_COLOR_SHADOW(t4)
    addu    a2, a2, s2
    addu    a2, a2, t2
    jal     vwf_dialog_plot
    addiu   a3, t0, 1
@@bit_next:
    addiu   t2, t2, 1
    sltiu   t3, t2, 16
    bnez    t3, @@bit
    nop
@@row_next:
    addiu   t0, t0, 1
    sltu    t3, t0, t8
    bnez    t3, @@row
    nop

    ; --- queue upload + activate each touched cell ---
    srl     s1, s2, 4                   ; s1 = cell iterator (saved by emit)
@@cell:
    li      t1, DLG_BOX_COLS            ; P = line*15 + cell
    multu   s0, t1
    andi    t6, s1, RING_CELLS - 1
    sll     t6, t6, 7
    la      t0, vwf_dlg_ring
    addu    t6, t0, t6                  ; src = ring cell
    mflo    t2
    addu    t2, t2, s1                  ; t2 = P
    addiu   t3, t2, 1                   ; P+1 selects the VRAM slot
    andi    t4, t3, 0xF
    sll     t4, t4, 2
    addiu   t4, t4, DLG_TEXT_VRAM_X     ; x
    andi    t5, t3, 0xF0
    addiu   t5, t5, DLG_TEXT_VRAM_Y     ; y
    lw      t7, VWF_CFG_UPLOAD_COUNT(s5)
    lw      v0, VWF_CFG_UPLOAD_QUEUE(s5)
    lw      t8, 0(t7)
    nop
    sll     t9, t8, 1
    addu    t9, t9, t8
    sll     t9, t9, 2                   ; *12
    addu    t9, t9, v0
    sw      t6, 0(t9)
    sh      t4, 4(t9)
    sh      t5, 6(t9)
    li      v0, 4
    sh      v0, 8(t9)
    li      v0, 16
    sh      v0, 10(t9)
    addiu   t8, t8, 1
    sw      t8, 0(t7)
    lw      t1, VWF_CFG_ACTIVATE(s5)    ; activate map cell P
    nop
    jalr    t1
    move    a0, t2
    la      t4, vwf_dlg_state
    lhu     t1, DLG_LAST(t4)
    nop
    sltu    t1, s1, t1                  ; more cells?
    beqz    t1, @@done
    nop
    j       @@cell
    addiu   s1, s1, 1
@@done:
    lw      ra, 0x0C(sp)
    nop
    jr      ra
    nop

;; -------------------------------------------------------------
;; vwf_dialog_plot: OR color t9 into pixel (a2 = x, a3 = row) of the ring.
;; Leaf; clobbers v0, v1, t3, t4. Ignores x >= box width.
;; -------------------------------------------------------------
vwf_dialog_plot:
    sltiu   v0, a2, DLG_BOX_WIDTH_PX
    beqz    v0, @@out
    srl     v0, a2, 4                   ; cell
    andi    v0, v0, RING_CELLS - 1
    sll     v0, v0, 7                   ; ring slot * 128
    sll     v1, a3, 3                   ; row * 8
    addu    v0, v0, v1
    andi    v1, a2, 0xF
    srl     t3, v1, 1
    addu    v0, v0, t3
    la      t3, vwf_dlg_ring
    addu    v0, v0, t3                  ; byte address
    andi    v1, v1, 1
    sll     v1, v1, 2                   ; nibble shift (low nibble = left pixel)
    sllv    t3, t9, v1
    lbu     t4, 0(v0)
    nop
    or      t4, t4, t3
    sb      t4, 0(v0)
@@out:
    jr      ra
    nop
