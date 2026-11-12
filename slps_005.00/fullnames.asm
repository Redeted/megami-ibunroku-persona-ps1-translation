;; =============================================================
;; SLPS_005.00 - full-length item names in a proportional small font (tools/fullnames.py)
;;
;; Menus draw item names into libgs GsBG maps (u16 cell = glyph code + colour set * 0xD7, 8x12 cells) that the
;; resident cell sorter at 0x8003235C turns into one sprite per cell, so a name could never be longer than its cells.
;; Now a cell holding  0x8000 | set << 13 | id  (id = 1-based item id, set = colour set 0-3) is a NAME MARKER: the sorter hook draws the
;; item's full name from that cell on, glyph by glyph with proportional advances (fn_width), inside the marker cell
;; plus the blank cells (0xFFFF or glyph 0 of any colour set) to its right in the same map row = the budget. Wider than the
;; budget: 1 px less per glyph; still wider: the glyphs that do not fit are dropped.
;; Writers: ADV's string-to-map copy 0x80067C00 writes the marker when it is asked to copy a 10-glyph item record name
;; (item-name helper 0x80090164 with 40 callers + inlined copies: shop, item and equipment menus ...); fn_adv_copy.
;;
;; The code and data live in kernel RAM FN_BLOB_ADDR..0x8000FFFF: the BIOS only allocates its control blocks at
;; 0x8000E000..0x8000E59F (EvCB/TCB/ExCB/PCB, alloc_kernel_memory) and the rest of that 8 KB area stays unused.
;; A boot stub appended to the EXE (new entry point) copies the blob there and jumps to the original entry 0x80011930.
;; =============================================================

FN_BLOB_ADDR            equ 0x8000EA00
FN_BAR_ADDR             equ 0x8000E780          ; Persona status bar block (below the blob, same copy)
FN_BLOB_LIMIT           equ 0x8000FFF0
FN_ORIG_ENTRY           equ 0x80011930
FN_ITEM_NAMES           equ 0x8004440C          ; + id * 0x20 = record name (10 glyphs, FF-terminated when shorter)
FN_BUF_SIZE             equ 32
FN_BTL_BUDGET           equ 98                  ; px of the battle result ITEM line (x 200 .. the window frame)
FN_BTL_LIST             equ 86                  ; px of a battle ITEM list name (x 40 .. the count at 128)
FN_BTL_IDS              equ 0x800F8088          ; BTLP: the 12 listed items (id | count << 9)
FN_FIELD                equ 10                  ; budget cap in cells (the original name field)
FN_RUN_MAX              equ 12                  ; longer budget only when content ends the blank run within this
FN_PERSONA_NAMES        equ PERSONA_RECORDS_ADDR + 0x2C + PERSONA_NAME   ; Persona 1's name
FN_PERSONA_COUNT        equ 100
FN_PERSONA_FLAG         equ 0x1000              ; marker id bit: Persona
FN_DEMON_FLAG           equ 0x800               ; marker id bit: demon (neither: item id 1-382)
FN_DEMON_RECORDS        equ 0x800417A0          ; + id * 0x38 = record, name at +0 (tools/demons.py)
FN_DEMON_COUNT          equ 194
FN_SKILL_COUNT          equ 242                 ; skill records 1-242 (tools/skills.py COUNT); marker id 0x1800 | id
FN_ITEM_COUNT           equ 382                ; items 0-162 + equipment 163-381 (tools/items.py COUNT)
FN_UPPER_FIRST          equ 0xA6                ; small-font A..Z (checked by tools/fullnames.py)
FN_UPPER_LAST           equ 0xBF

;; =============================================================
;; Persona status page, bottom bar (menus of ADV / DNG / S2D): arcana + FULL Persona name, proportional.
;; The bar is a sprite-string object list (DNG 0x8009AC54: 12-byte entries {header*, x, y, ...}; header = {cols, rows,
;; 0, 0, u16 cell w, u16 cell h} + 8-byte cells {u, v, 0x1E, -, u16 0x3C0, u16 0x1A0 + colour}; u = (glyph % 31) * 8,
;; v = (glyph / 31) * 12, FFFF = empty) drawn by the overlay's sprite drawer (DNG cell loop 0x80075A04, x += cell w at
;; 0x80075B54). The page function (DNG 0x8007F464) filled two 10-cell strings 88 px apart: arcana and the first 10
;; glyphs of the Persona master name.
;; Now: byte 3 of a cell (unused by the drawer) = 0x80 | x advance, used by the drawer hook instead of the cell width;
;; fn_bar_fill writes cells with the proportional advances of fn_width; the name is a 16-cell string of its own
;; (fn_bar_hdr / fn_bar_cells, text from persona_name_copy) at x 68. This block sits right below the blob in kernel
;; RAM (FN_BAR_ADDR..FN_BLOB_ADDR) and is copied by the same boot-stub loop.
;; =============================================================
.macro persona_bar_hooks, drawer, func, listptr
.org drawer
    lb      v0, 3(s6)                           ; was nop                 (s6 = the cell)
    jal     fn_bar_adv                          ; was addu v0, s4, a3     (ra is saved by the drawer)
    nop                                         ; was addu s4, v0, zero
.org func + 0x2C
    lui     s1, (fn_bar_cells >> 16) + ((fn_bar_cells >> 15) & 1)
    addiu   s1, s1, fn_bar_cells & 0xFFFF       ; was the overlay's 10-cell name string
.org func + 0x3C
    ori     a1, zero, 16                        ; clear 16 cells (was 10)
.org func + 0x68
    jal     fn_bar_fill                         ; arcana (a0 cells, a1 string, a3 = 10)
.org func + 0x70
    lbu     a1, 0x18(s2)                        ; Persona id
    jal     fn_bar_name
    nop
    j       func + 0xA4
    nop
.org listptr
    .word   fn_bar_hdr                          ; was the overlay's name string header
    .halfword 68                                ; x, was 88
.endmacro

;; ANALYZE demon page (SYSTEM > ANALYZE), bottom bar: race + FULL demon name, proportional, through the same cell
;; advances and the same 16-cell string as the Persona bar. `fill` = the jal that filled the 10-cell name string from
;; the demon record (s0 = demon id * 0x38); the race fill is the jal 0x40 further. The name object keeps x 64.
.macro analyze_bar_hooks, fill, listptr
.org fill - 0x28
    lui     s1, (fn_bar_cells >> 16) + ((fn_bar_cells >> 15) & 1)
    addiu   s1, s1, fn_bar_cells & 0xFFFF       ; was the overlay's 10-cell name string
.org fill - 0x18
    ori     a1, zero, 16                        ; clear 16 cells (was 10)
.org fill - 0x14
    jal     fn_ana_name
    addu    a1, s0, zero                        ; demon id * 0x38
    nop
    nop
    nop
    nop
.org fill + 0x40
    jal     fn_bar_fill                         ; race (a0 cells, a1 string, a3 = 6)
.org listptr
    .word   fn_bar_hdr                          ; was the overlay's name string header
.endmacro

;; --- hook 1: first cell of a row (sorter reads the cell into a0 at 0x80032724) ---
.org 0x80032728
    jal     fn_hook_first                       ; was ori v0, zero, 0xFFFF
    lw      v1, 8(a1)                           ; was at 0x80032734 (GsMAP cell table)
    beq     a0, v0, 0x80032918                  ; was at 0x8003272C: empty cell
    sll     v0, a0, 3                           ; was at 0x80032730

;; --- hook 2: the other cells of a row (cell in a1, loaded at 0x800329B0) ---
.org 0x800328A4
    jal     fn_hook_int                         ; was ori v0, zero, 0xFFFF
    nop
    beq     a1, v0, 0x80032918                  ; was at 0x800328A8 (delay slot: lw v0, 0x14(t7) as before)
                                                ; addiu a0, s0, 0x18 (was the delay slot) is done by the hook

;; --- boot stub, appended to the EXE (the original image ends at 0x80056000) ---
.org 0x80056000
fn_boot:
    la      t0, fn_bar_src
    li      t1, FN_BAR_ADDR
    li      t2, fn_blob_end
@@copy:
    lw      t3, 0(t0)
    addiu   t0, t0, 4
    sw      t3, 0(t1)
    addiu   t1, t1, 4
    sltu    at, t1, t2
    bnez    at, @@copy
    nop
    j       FN_ORIG_ENTRY
    nop
.align 16
fn_bar_src:
;; =============================================================
;; Persona status bar block (see persona_bar_hooks), assembled for FN_BAR_ADDR; the blob follows at FN_BLOB_ADDR
;; =============================================================
.headersize FN_BAR_ADDR - orga()
.org FN_BAR_ADDR
.area FN_BLOB_ADDR - FN_BAR_ADDR
fn_bar_adv:                                     ; v0 = (signed) byte 3 of the cell just handled; returns into the loop
    bgez    v0, @@plain
    andi    v0, v0, 0x7F
    jr      ra
    addu    s4, s4, v0
@@plain:
    jr      ra
    addu    s4, s4, a3

;; a0 = cells, a1 = glyph string (FF ends), a3 = max glyphs. Glyph i is drawn at pen - first used column (the 8 px
;; sprite keeps its width): advance = width + left - left of the next glyph.
fn_bar_fill:
    ori     t4, zero, 0xFF
@@loop:
    beqz    a3, @@ret
    nop
    lbu     t0, 0(a1)
    ori     t1, zero, 31
    beq     t0, t4, @@ret
    nop
    divu    t0, t1
    mflo    t2
    mfhi    t3
    sll     t3, t3, 3
    sb      t3, 0(a0)                           ; u
    sll     t5, t2, 1
    addu    t5, t5, t2
    sll     t5, t5, 2
    sb      t5, 1(a0)                           ; v
    ori     t5, zero, 0x3C0
    sh      t5, 4(a0)
    ori     t5, zero, 0x1A0
    sh      t5, 6(a0)
    la      t5, fn_width
    addu    t6, t5, t0
    lbu     t6, 0(t6)
    lbu     t7, 1(a1)                           ; next glyph
    andi    t8, t6, 0xF
    bnez    t8, @@w
    srl     t6, t6, 4
    ori     t8, zero, 8
@@w:
    andi    t6, t6, 3
    beq     t7, t4, @@store
    addu    t8, t8, t6
    addu    t7, t5, t7
    lbu     t7, 0(t7)
    nop
    srl     t7, t7, 4
    andi    t7, t7, 3
    subu    t8, t8, t7
@@store:
    ori     t8, t8, 0x80
    sb      t8, 3(a0)
    addiu   a1, a1, 1
    addiu   a3, a3, -1
    b       @@loop
    addiu   a0, a0, 8
@@ret:
    jr      ra
    nop

;; a1 = Persona id: the full name (persona_name_copy: 16 glyphs, blank-padded) into the 16-cell string
fn_bar_name:
    addiu   sp, sp, -0x18
    sw      ra, 0x14(sp)
    la      a0, fn_buf
    jal     persona_name_copy                   ; clobbers v0, v1, a0, a1, a2, at
    nop
    la      a1, fn_buf
    addiu   t0, a1, 16
@@trim:
    beq     t0, a1, @@go
    nop
    lbu     t1, -1(t0)
    nop
    bnez    t1, @@go
    nop
    b       @@trim
    addiu   t0, t0, -1
@@go:
    ori     t1, zero, 0xFF
    sb      t1, 0(t0)
    la      a0, fn_bar_cells
    lw      ra, 0x14(sp)
    ori     a3, zero, 16
    j       fn_bar_fill
    addiu   sp, sp, 0x18

;; a1 = demon id * 0x38: the full demon name (fn_item_text) into the 16-cell string
fn_ana_name:
    addiu   sp, sp, -0x20
    sw      ra, 0x14(sp)
    sw      s2, 0x18(sp)
    sw      s5, 0x1C(sp)
    ori     v0, zero, 0x38
    divu    a1, v0
    mflo    s2
    ori     s2, s2, FN_DEMON_FLAG
    la      a1, fn_buf
    jal     fn_item_text                        ; clobbers v0, v1, at, t3, t5, s5
    nop
    la      a1, fn_buf
    la      a0, fn_bar_cells
    lw      ra, 0x14(sp)
    lw      s2, 0x18(sp)
    lw      s5, 0x1C(sp)
    ori     a3, zero, 16
    j       fn_bar_fill
    addiu   sp, sp, 0x20

.align 4
fn_bar_hdr:
    .byte   16, 1, 0, 0, 8, 0, 12, 0
fn_bar_cells:
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
    .byte   0xFF, 0xFF, 0x1E, 0, 0xC0, 3, 0xA0, 1
.endarea
.org FN_BLOB_ADDR                               ; (pads the block: the blob is contiguous in the file and in RAM)

fn_blob_src:

;; =============================================================
;; kernel blob (assembled for FN_BLOB_ADDR, stored right after the stub)
;; =============================================================
.area FN_BLOB_LIMIT - FN_BLOB_ADDR

;; a0 = cell. Returns v0 = 0xFFFF; a0 = 0xFFFF when the cell was a name marker (the sorter then skips it).
fn_hook_first:
    ori     v0, zero, 0xFFFF
    beq     a0, v0, @@ret
    andi    v0, a0, 0x8000
    beqz    v0, @@ret
    nop
    sw      ra, fn_save_ra
    jal     fn_draw
    nop
    lw      ra, fn_save_ra
    ori     a0, zero, 0xFFFF
@@ret:
    jr      ra
    ori     v0, zero, 0xFFFF

;; a1 = cell. Returns v0 = 0xFFFF, a0 = s0 + 0x18; a1 = 0xFFFF when the cell was a name marker.
fn_hook_int:
    ori     v0, zero, 0xFFFF
    beq     a1, v0, @@ret
    andi    v0, a1, 0x8000
    beqz    v0, @@ret
    nop
    sw      ra, fn_save_ra
    sw      a0, fn_save_a0
    jal     fn_draw
    move    a0, a1
    lw      ra, fn_save_ra
    lw      a0, fn_save_a0
    ori     a1, zero, 0xFFFF
@@ret:
    ori     v0, zero, 0xFFFF
    jr      ra
    addiu   a0, s0, 0x18

;; Draw the name of marker a0 at the current cell. Sorter registers used (read only): t7 GsBG*, t1 cell index,
;; t6 cells per map row, t2 = x | y << 16, t0 = w | h << 16, s1 = v offset, s7 = draw mode, 0x28(sp) = sprite tag.
;; s0 = packet pointer (advanced by 0x18 per glyph). Everything else is preserved.
fn_draw:
    la      at, fn_save
    sw      v1, 0x00(at)
    sw      a1, 0x04(at)
    sw      a2, 0x08(at)
    sw      a3, 0x0C(at)
    sw      t3, 0x10(at)
    sw      t5, 0x14(at)
    sw      t8, 0x18(at)
    sw      t9, 0x1C(at)
    sw      s2, 0x20(at)
    sw      s3, 0x24(at)
    sw      s4, 0x28(at)
    sw      s5, 0x2C(at)
    sw      s6, 0x30(at)
    andi    s2, a0, 0x1FFF                      ; s2 = item id (1-based)
    srl     s3, a0, 13
    andi    s3, s3, 3
    sll     v1, s3, 8
    sll     at, s3, 5
    subu    v1, v1, at
    sll     at, s3, 3
    subu    v1, v1, at
    subu    s3, v1, s3                          ; s3 = colour set * 0xD7 (glyph offset)
    lw      a1, 0x14(t7)                        ; GsMAP
    nop
    lw      s4, 8(a1)                           ; s4 = GsCELL table
    lw      a2, 0xC(a1)                         ; map cells
    lbu     s5, 0(a1)                           ; s5 = cell width
    ; --- budget: this cell + the blank cells right of it in the row, when real content (yen sign, count, next
    ;     column) ends them within FN_RUN_MAX cells; otherwise the row is blank up to / behind the window frame
    ;     (the layer is often full-screen): the original field, FN_FIELD cells ---
    divu    t1, t6
    mfhi    a3                                  ; column
    sll     v0, t1, 1
    addu    v0, v0, a2
    addiu   v0, v0, 2                           ; next cell
    subu    a3, t6, a3
    addiu   a3, a3, -1                          ; cells left in the row
    ori     s6, zero, 1                         ; s6 = budget in cells
@@scan:
    blez    a3, @@row_end
    nop
    lhu     v1, 0(v0)
    ori     at, zero, 0xFFFF
    beq     v1, at, @@blank                     ; empty cell
    nop
    beqz    v1, @@blank                         ; glyph 0 (space) of colour set 0..3
    ori     at, zero, 0xD7
    beq     v1, at, @@blank
    ori     at, zero, 0x1AE
    beq     v1, at, @@blank
    ori     at, zero, 0x285
    bne     v1, at, @@content
    nop
@@blank:
    addiu   s6, s6, 1
    addiu   v0, v0, 2
    b       @@scan
    addiu   a3, a3, -1
@@content:
    sltiu   at, s6, FN_RUN_MAX + 1
    bnez    at, @@scan_end                      ; ended by content within FN_RUN_MAX cells: keep the run
    nop
@@row_end:                                      ; also: a run longer than FN_RUN_MAX
    sltiu   at, s6, FN_FIELD + 1
    bnez    at, @@scan_end                      ; <= FN_FIELD: keep
    nop
    ori     s6, zero, FN_FIELD                  ; else cap to the original field
@@scan_end:
    multu   s6, s5
    mflo    s6                                  ; s6 = budget in px
    ; --- Persona (id | 0x1000): persona_name_copy (16 glyphs, blank-padded); skill (id | 0x1800): skill_name_copy
    ;     (15 glyphs); the trailing blanks are cut ---
    andi    at, s2, FN_PERSONA_FLAG
    beqz    at, @@item
    addiu   s6, s6, -1                          ; (both paths) 1 px kept free: a tightened name must not touch the count digit / yen sign after it
    sw      ra, fn_save_ra2                     ; (macro: uses at)
    la      a0, fn_buf
    sb      zero, PERSONA_MAXLEN - 1(a0)        ; skills write one glyph less
    andi    at, s2, FN_DEMON_FLAG
    bnez    at, @@skill
    andi    a1, s2, FN_DEMON_FLAG - 1
    jal     persona_name_copy                   ; clobbers v0, v1, a0, a1, a2, at
    nop
    b       @@named
    nop
@@skill:
    jal     skill_name_copy                     ; clobbers v0, v1, a0, a1, a2, at
    nop
@@named:
    lw      ra, fn_save_ra2
    la      a1, fn_buf + PERSONA_MAXLEN
@@trim:
    la      at, fn_buf
    beq     a1, at, @@copied
    nop
    lbu     v1, -1(a1)
    nop
    bnez    v1, @@copied
    nop
    b       @@trim
    addiu   a1, a1, -1
@@item:
    sw      ra, fn_save_ra2                     ; (macro: uses at)
    la      a1, fn_buf
    jal     fn_item_text
    nop
    lw      ra, fn_save_ra2
@@copied:
    ori     at, zero, 0xFF
    sb      at, 0(a1)
    ; --- total width a3, glyph count t3 -> t8 = 1 px less per glyph (shadow column dropped) when too wide; s2 = px
    ;     still missing after that, taken 1 px at a time from glyphs spread evenly over the name (v0 = Bresenham
    ;     accumulator); only the longest names in 10-cell fields need it ---
    la      a1, fn_buf
    move    a3, zero
    move    t3, zero
@@width:
    lbu     v1, 0(a1)
    ori     at, zero, 0xFF
    beq     v1, at, @@width_end
    addiu   a1, a1, 1
    la      at, fn_width
    addu    at, at, v1
    lbu     v1, 0(at)
    nop
    andi    v1, v1, 0xF
    bnez    v1, @@width_add
    nop
    ori     v1, zero, 8
@@width_add:
    addiu   t3, t3, 1
    b       @@width
    addu    a3, a3, v1
@@width_end:
    move    t8, zero
    move    s2, zero
    move    v0, zero
    slt     at, s6, a3
    beqz    at, @@fits
    subu    a3, a3, t3
    ori     t8, zero, 1
    slt     at, s6, a3
    beqz    at, @@fits
    nop
    subu    s2, a3, s6                          ; s2 = px still missing
@@fits:
    ; --- draw: t9 = pen x, s6 = right end ---
    sll     t9, t2, 16
    sra     t9, t9, 16
    addu    s6, s6, t9
    la      a1, fn_buf
@@draw:
    lbu     v1, 0(a1)
    ori     at, zero, 0xFF
    beq     v1, at, @@done
    addiu   a1, a1, 1
    la      at, fn_width
    addu    at, at, v1
    lbu     a2, 0(at)                           ; a2 = width byte
    nop
    andi    a3, a2, 0xF
    bnez    a3, @@draw_w
    nop
    ori     a3, zero, 8
@@draw_w:
    subu    a3, a3, t8                          ; a3 = advance
    move    s5, a3                              ; s5 = sprite width (shadow column dropped when tightened)
    beqz    s2, @@draw_fit
    addu    v0, v0, s2
    slt     at, v0, t3
    bnez    at, @@draw_fit
    nop
    subu    v0, v0, t3
    addiu   a3, a3, -1                          ; this glyph overlaps the next one by 1 px
@@draw_fit:
    addu    at, t9, a3                          ; fits by its advance (a 1 px overlap may reach past the end)
    slt     at, s6, at
    bnez    at, @@done                          ; does not fit any more
    nop
    beqz    v1, @@draw_next                     ; space: advance only
    addu    v1, v1, s3
    sll     v1, v1, 3
    addu    v1, v1, s4                          ; GsCELL of the glyph
    addiu   at, s0, 0x18
    sw      at, 0(s0)
    ori     at, zero, 5
    sb      at, 3(s0)                           ; tag: next packet, 5 words
    lhu     at, 6(v1)
    nop
    andi    at, at, 0x1F
    or      at, at, s7
    sw      at, 4(s0)                           ; draw mode (texture page)
    lw      at, 0x28(sp)
    nop
    sw      at, 8(s0)                           ; SPRT command + colour (as the sorter's own sprites)
    andi    at, t9, 0xFFFF
    lui     t5, 0xFFFF
    and     t5, t2, t5
    or      at, at, t5
    sw      at, 0xC(s0)                         ; x = pen, y = cell y
    srl     t5, a2, 4
    andi    t5, t5, 3
    lbu     at, 0(v1)
    nop
    addu    at, at, t5
    sb      at, 0x10(s0)                        ; u + first used column
    lbu     at, 1(v1)
    nop
    addu    at, at, s1
    sb      at, 0x11(s0)                        ; v
    lhu     at, 2(v1)
    nop
    sh      at, 0x12(s0)                        ; clut
    sh      s5, 0x14(s0)                        ; w
    srl     at, t0, 16
    sh      at, 0x16(s0)                        ; h (as the cell)
    addiu   s0, s0, 0x18
@@draw_next:
    b       @@draw
    addu    t9, t9, a3
@@done:
    la      at, fn_save
    lw      v1, 0x00(at)
    lw      a1, 0x04(at)
    lw      a2, 0x08(at)
    lw      a3, 0x0C(at)
    lw      t3, 0x10(at)
    lw      t5, 0x14(at)
    lw      t8, 0x18(at)
    lw      t9, 0x1C(at)
    lw      s2, 0x20(at)
    lw      s3, 0x24(at)
    lw      s4, 0x28(at)
    lw      s5, 0x2C(at)
    jr      ra
    lw      s6, 0x30(at)

;; Item / demon name of id s2 (1-based item id, or FN_DEMON_FLAG | demon id) as glyph bytes at a1, FF-terminated:
;; the record name title-cased, or a pool entry (u16 LE id, glyphs, FF): id = the whole name, id | 0x8000 = the glyphs
;; that follow the (title-cased) record name. Returns a1 = the FF. Clobbers v0, v1, at, t3, t5, s5 (at most 31 glyphs).
fn_item_text:
    ; --- the name: the record name title-cased, or a pool entry (u16 LE id, glyphs, FF): id = the whole name,
    ;     id | 0x8000 = the glyphs that follow the (title-cased) record name ---
    la      v0, fn_pool
    move    s5, zero                            ; s5 = tail after the record (0 = none)
@@t_find:
    lbu     v1, 0(v0)
    lbu     at, 1(v0)
    addiu   v0, v0, 2
    sll     at, at, 8
    or      v1, v1, at
    ori     at, zero, 0xFFFF
    beq     v1, at, @@t_record
    andi    at, v1, 0x7FFF
    bne     at, s2, @@t_skip
    andi    at, v1, 0x8000
    beqz    at, @@t_pool_copy                     ; whole name
    ori     t3, zero, FN_BUF_SIZE - 1
    b       @@t_record                            ; record + tail
    move    s5, v0
@@t_skip:
    lbu     v1, 0(v0)
    addiu   v0, v0, 1
    ori     at, zero, 0xFF
    bne     v1, at, @@t_skip
    nop
    b       @@t_find
    nop
@@t_pool_copy:
    lbu     v1, 0(v0)
    addiu   v0, v0, 1
    ori     at, zero, 0xFF
    beq     v1, at, @@t_done
    nop
    sb      v1, 0(a1)
    addiu   t3, t3, -1
    bnez    t3, @@t_pool_copy
    addiu   a1, a1, 1
    b       @@t_done
    nop
@@t_record:
    andi    at, s2, FN_DEMON_FLAG
    bnez    at, @@t_rec_demon
    sll     v0, s2, 5
    li      at, FN_ITEM_NAMES
    b       @@t_rec_go
    addu    v0, v0, at
@@t_rec_demon:
    andi    at, s2, FN_DEMON_FLAG - 1
    sll     v0, at, 6
    sll     at, at, 3
    subu    v0, v0, at                          ; id * 0x38
    li      at, FN_DEMON_RECORDS
    addu    v0, v0, at
@@t_rec_go:
    ori     t3, zero, 10
    move    t5, zero                            ; previous glyph was a word character
@@t_rec_copy:
    lbu     v1, 0(v0)
    addiu   v0, v0, 1
    ori     at, zero, 0xFF
    beq     v1, at, @@t_rec_end
    nop
    beqz    t5, @@t_rec_store
    sltiu   at, v1, FN_UPPER_FIRST
    bnez    at, @@t_rec_store
    sltiu   at, v1, FN_UPPER_LAST + 1
    beqz    at, @@t_rec_store
    nop
    la      at, fn_lower - FN_UPPER_FIRST
    addu    at, at, v1
    lbu     v1, 0(at)                           ; uppercase after a word character -> lowercase
    nop
@@t_rec_store:
    sb      v1, 0(a1)
    addiu   a1, a1, 1
    la      at, fn_width
    addu    at, at, v1
    lbu     t5, 0(at)
    addiu   t3, t3, -1
    bnez    t3, @@t_rec_copy
    andi    t5, t5, 0x40
@@t_rec_end:
    beqz    s5, @@t_done
    move    v0, s5
    b       @@t_pool_copy                         ; append the tail (the buffer still has >= 21 bytes)
    ori     t3, zero, FN_BUF_SIZE - 11
@@t_done:
    ori     at, zero, 0xFF
    jr      ra
    sb      at, 0(a1)

;; (The same routine exists in DNG 0x8007782C and S2D 0x800673E0: dng/fullnames.asm, s2d/fullnames.asm; each hook passes
;; its own return address copy + 0xC in t9.)
;; ADV string-to-map copy 0x80067C00 (a0 = glyph bytes, a1 = map cell, a2 = glyph offset, a3 = max count; stops at
;; FF), entered from its first instruction. A copy of a 10-glyph ITEM RECORD NAME (a0 = 0x8004442C + n * 0x20, a3 = 10:
;; the item-name helper 0x80090164 and its inlined copies, e.g. the equipment list redraw 0x800914E4) writes a marker
;; instead (also a Persona MASTER RECORD NAME, a0 = 0x8004B100 + n * 0x2C: Velvet Room lists 0x8007B9E4 ...;
;; marker id 0x1000 | Persona id, name from persona_name_copy; and a DEMON record name, a0 = 0x800417A0 + n * 0x38:
;; fusion lists, marker id 0x800 | demon id; and a SKILL record name, a0 = 0x80047D44 + n * 0x14: Persona status page
;; 0x8007BAD8, marker id 0x1800 | skill id, text from skill_name_copy). Glyph offset = colour set * 0xD7 (0 white, 0xD7 grey: can't buy / max owned, 0x1AE, 0x285); other offsets
;; and every other string: the original copy. The blank cells of the old 10-glyph field become empty cells (0xFFFF).
fn_adv_copy:
    andi    v0, a3, 0xFFFF
    ori     t0, zero, 10
    bne     v0, t0, @@plain
    lui     t0, 0x8004
    addiu   t0, t0, 0x442C
    subu    t1, a0, t0
    sltiu   t2, t1, FN_ITEM_COUNT * 0x20
    beqz    t2, @@persona
    andi    t2, t1, 0x1F
    bnez    t2, @@plain
    srl     t1, t1, 5
    b       @@colour
    addiu   t1, t1, 1                           ; t1 = item id (1-based)
@@persona:                                      ; Persona master record name: 0x8004B100 + (id - 1) * 0x2C
    li      t0, FN_PERSONA_NAMES
    subu    t1, a0, t0
    sltiu   t2, t1, FN_PERSONA_COUNT * 0x2C
    beqz    t2, @@demon
    ori     t2, zero, 0x2C
    divu    t1, t2
    mfhi    t2
    mflo    t1
    bnez    t2, @@plain
    addiu   t1, t1, 1
    b       @@colour
    ori     t1, t1, FN_PERSONA_FLAG             ; t1 = 0x1000 | Persona id
@@demon:                                        ; demon master record name: 0x800417A0 + id * 0x38 (+0)
    li      t0, FN_DEMON_RECORDS + 0x38
    subu    t1, a0, t0
    sltiu   t2, t1, FN_DEMON_COUNT * 0x38
    beqz    t2, @@skill
    ori     t2, zero, 0x38
    divu    t1, t2
    mfhi    t2
    mflo    t1
    bnez    t2, @@plain
    addiu   t1, t1, 1
    b       @@colour
    ori     t1, t1, FN_DEMON_FLAG               ; t1 = 0x800 | demon id
@@skill:                                        ; skill record name: 0x80047D44 + id * 0x14 (+0)
    li      t0, SKILL_RECORDS_ADDR + 0x14
    subu    t1, a0, t0
    sltiu   t2, t1, FN_SKILL_COUNT * 0x14
    beqz    t2, @@plain
    ori     t2, zero, 0x14
    divu    t1, t2
    mfhi    t2
    mflo    t1
    bnez    t2, @@plain
    addiu   t1, t1, 1
    ori     t1, t1, FN_PERSONA_FLAG | FN_DEMON_FLAG     ; t1 = 0x1800 | skill id
@@colour:
    andi    a2, a2, 0xFFFF
    beqz    a2, @@set
    move    t0, zero
    ori     t2, zero, 0xD7
    beq     a2, t2, @@set
    ori     t0, zero, 1
    ori     t2, zero, 0x1AE
    beq     a2, t2, @@set
    ori     t0, zero, 2
    ori     t2, zero, 0x285
    bne     a2, t2, @@plain
    ori     t0, zero, 3
@@set:
    sll     t0, t0, 13
    or      t0, t0, t1
    ori     t0, t0, 0x8000
    sh      t0, 0(a1)
    addiu   t1, a1, 2
    ori     t2, zero, 9
    ori     t4, zero, 0xFFFF
@@blank:
    lhu     t3, 0(t1)
    nop
    beqz    t3, @@empty
    ori     t5, zero, 0xD7
    beq     t3, t5, @@empty
    ori     t5, zero, 0x1AE
    beq     t3, t5, @@empty
    ori     t5, zero, 0x285
    bne     t3, t5, @@next
    nop
@@empty:
    sh      t4, 0(t1)
@@next:
    addiu   t2, t2, -1
    bnez    t2, @@blank
    addiu   t1, t1, 2
    jr      ra
    nop
@@plain:
    andi    v0, a3, 0xFFFF                      ; the two replaced instructions
    beqz    v0, @@ret
    nop
    jr      t9                                  ; the overlay's copy + 0xC (t9 set by the hook: ADV 0x80067C0C, DNG 0x80077838, S2D 0x800673EC)
    nop
@@ret:
    jr      ra
    nop

;; BTLP battle result screen, ITEM line (btlp/fullnames.asm). The dropped item's name was copied (10 glyphs) into the
;; 16-byte buffer 0x800F7DBC that the result layout entry 0x800DF7A8 prints with BTLP's fixed 8 px text drawer; now
;; the entry prints fn_btl_buf, filled here with the full name (a0 = 1-based item id, 0 = none). Preserves s*/t*/a3.
fn_btl_drop:
    la      at, fn_save_btl
    sw      ra, 0x00(at)
    sw      s2, 0x04(at)
    sw      s5, 0x08(at)
    sw      t3, 0x0C(at)
    sw      t5, 0x10(at)
    move    s2, a0
    la      a1, fn_btl_buf
    beqz    a0, @@end
    nop
    jal     fn_item_text
    nop
@@end:
    ori     v0, zero, 0xFF
    sb      v0, 0(a1)
    la      at, fn_save_btl
    lw      ra, 0x00(at)
    lw      s2, 0x04(at)
    lw      s5, 0x08(at)
    lw      t3, 0x0C(at)
    jr      ra
    lw      t5, 0x10(at)

;; BTLP text drawer 0x80088E80, glyph x (hooked at 0x80088F84): v0 = entry x, t0 = glyph index, a3 = glyph pointer,
;; t3 = layout entry (+4 = string). Returns v0 + the glyph's offset: t0 * 8 (as before), or for fn_btl_buf the
;; proportional pen (fn_width advances, 1 px less per glyph when the name is wider than FN_BTL_BUDGET) minus the
;; glyph's first used column (the drawer draws the whole 8 px cell). Clobbers v1, at only.
fn_btl_x:
    la      v1, fn_btl_buf                      ; proportional when the glyph pointer is inside fn_btl_buf
    subu    at, a3, v1
    sltiu   at, at, FN_BUF_SIZE + 4
    bnez    at, @@prop
    nop
    sll     v1, t0, 3
    jr      ra
    addu    v0, v0, v1
@@prop:
    la      at, fn_save_x
    sw      a0, 0x00(at)
    sw      a1, 0x04(at)
    sw      t8, 0x08(at)
    sw      t9, 0x0C(at)
    move    a0, v1
    move    a1, zero                            ; a1 = total width
@@tot:
    lbu     t8, 0(a0)
    ori     at, zero, 0xFF
    beq     t8, at, @@tot_end
    addiu   a0, a0, 1
    la      at, fn_width
    addu    at, at, t8
    lbu     t8, 0(at)
    nop
    andi    t8, t8, 0xF
    bnez    t8, @@tot_add
    nop
    ori     t8, zero, 8
@@tot_add:
    b       @@tot
    addu    a1, a1, t8
@@tot_end:
    lw      t8, 4(t3)                           ; result line (entry string = fn_btl_buf) or an item list row
    nop
    beq     t8, v1, @@budget
    ori     t8, zero, FN_BTL_BUDGET + 1
    ori     t8, zero, FN_BTL_LIST + 1
@@budget:
    slt     t9, a1, t8
    xori    t9, t9, 1                           ; t9 = 1: too wide, 1 px less per glyph
    move    a1, zero                            ; a1 = pen
@@pre:
    beq     v1, a3, @@pre_end
    nop
    lbu     t8, 0(v1)
    addiu   v1, v1, 1
    la      at, fn_width
    addu    at, at, t8
    lbu     t8, 0(at)
    nop
    andi    t8, t8, 0xF
    bnez    t8, @@pre_add
    nop
    ori     t8, zero, 8
@@pre_add:
    subu    t8, t8, t9
    b       @@pre
    addu    a1, a1, t8
@@pre_end:
    lbu     t8, 0(a3)
    la      at, fn_width
    addu    at, at, t8
    lbu     t8, 0(at)
    nop
    srl     t8, t8, 4
    andi    t8, t8, 3
    subu    a1, a1, t8
    addu    v0, v0, a1
    la      at, fn_save_x
    lw      a0, 0x00(at)
    lw      a1, 0x04(at)
    lw      t8, 0x08(at)
    jr      ra
    lw      t9, 0x0C(at)

;; BTLP battle ITEM list (FIGHT > ITEM): fn_btl_ent lives in BTLP (btlp/fullnames.asm) and prints a row from
;; fn_btl_buf; fn_btl_max replaces the drawer loop's "lbu v0, 0(a2)" (max glyphs): 31 while printing fn_btl_buf.
fn_btl_max:
    la      at, fn_btl_buf
    subu    at, a3, at
    sltiu   at, at, FN_BUF_SIZE + 4
    beqz    at, @@ret
    lbu     v0, 0(a2)
    ori     v0, zero, 31
@@ret:
    jr      ra
    nop

;; BTLP battle messages, item name insert (btlp/fullnames.asm). The name setter 0x8007A920 (a0 = kind, a1 = stored
;; name) copied kind 3 = item record name (10 glyphs, uppercase) into the 24-byte slot 0x800EBDE0 ("Obtained <item>":
;; negotiation gifts ...). Now kind 3 goes to fn_btl_msg (the text reader 0x8007CC18 points there): an item record
;; (a1 = FN_ITEM_NAMES + id * 0x20) as its full title-cased name, anything else as before (10 glyphs).
;; Runs inside the setter's frame (ra saved there), leaves through its epilogue.
fn_btl_msg_item:
    li      at, FN_ITEM_NAMES + 0x20
    subu    v0, a1, at
    sltiu   v1, v0, (FN_ITEM_COUNT - 1) * 0x20
    beqz    v1, @@copy
    ori     a2, zero, 10
    andi    v1, v0, 0x1F
    bnez    v1, @@copy
    la      at, fn_save_btl
    sw      s2, 0x04(at)
    sw      s5, 0x08(at)
    srl     s2, v0, 5
    addiu   s2, s2, 1
    la      a1, fn_buf
    jal     fn_item_text                        ; clobbers v0, v1, at, t3, t5, s5
    nop
    la      at, fn_save_btl
    lw      s2, 0x04(at)
    lw      s5, 0x08(at)
    la      a1, fn_buf
    ori     a2, zero, FN_BUF_SIZE - 1
@@copy:
    la      a0, fn_btl_msg
    jal     btl_name_copy                       ; small-font codes -> battle text bytes (btlp/name_lowercase.asm)
    nop
    j       0x8007AA18
    nop

.align 4
;; Emergency Exit / Traesto (dng/traesto.asm): the dungeon entrance, kept here because the DNG overlay is reloaded
fn_tr_vars:     .fill 16                        ; TRV_* offsets in dng/traesto.asm
fn_save_btl:    .fill 0x14
fn_save_x:      .fill 0x10
fn_btl_buf:     .fill FN_BUF_SIZE + 4
fn_btl_msg:     .fill FN_BUF_SIZE * 2           ; battle message item name (2 bytes per glyph + FF)
fn_save_ra:     .word 0
fn_save_a0:     .word 0
fn_save_ra2:    .word 0
fn_save:        .fill 0x34
fn_buf:         .fill FN_BUF_SIZE
.include "build/fullnames_data.asm"            ; fn_width, fn_lower, fn_pool (tools/fullnames.py)
.align 4
fn_blob_end:
.endarea

;; back to the EXE mapping: pad the file to a whole sector and update the header
.headersize SLPS_ADDR
.align 0x800
fn_exe_end:
.org SLPS_ADDR + 0x10
    .word   fn_boot                             ; pc0: the boot stub
.org SLPS_ADDR + 0x1C
    .word   fn_exe_end - 0x80010000             ; t_size
