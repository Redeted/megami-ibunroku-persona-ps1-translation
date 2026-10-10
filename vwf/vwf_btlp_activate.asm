;; BTLP cell activation (first dead fragment); see vwf_btlp.asm
;; -------------------------------------------------------------
;; btlp_activate(a0 = cell P): put the cell the engine just queued (BTCFG_ENTRY.src, a ring cell) into texture slot P of
;; the text struct and make sprite P show it.
;;  * dialogue struct (texture base y 0x100, never cleared): immediate LoadImage + DrawSync (a page is emitted in ONE call, up
;;    to 135 uploads, more than the game's 72-entry queue);
;;  * every other struct (choice windows at (0x38C,0x154) ...): their texture area is cleared by a ClearImage queued by the
;;    window code, and the game flushes clears BEFORE loads, so an immediate upload is wiped: copy the cell into the game's
;;    glyph ring (0x800EBE48, counter 0x800EBE44) and queue it with 0x80066620 like the original glyph function.
;; -------------------------------------------------------------
btlp_activate:
    addiu   sp, sp, -0x38
    sw      ra, 0x34(sp)
    sw      s0, 0x30(sp)
    sw      s1, 0x2C(sp)
    sw      a0, 0x28(sp)                ; P
    la      s0, vwf_cfg_btlp
    lw      s1, BTCFG_STRUCT(s0)
    li      t0, 15
    divu    a0, t0
    mflo    t1                          ; row
    mfhi    t2                          ; col
    lh      t3, BT_TEX_X(s1)
    sll     t4, t2, 2
    addu    t3, t3, t4                  ; x
    lh      t5, BT_TEX_Y(s1)
    sll     t4, t1, 4
    lw      a1, BTCFG_ENTRY(s0)         ; src of the queued ring cell
    li      t6, 0x100
    lh      t7, BT_TEX_Y(s1)
    addu    t5, t5, t4                  ; y
    bne     t7, t6, @@queue
    nop
    sh      t3, 0x20(sp)                ; RECT x
    sh      t5, 0x22(sp)                ; RECT y
    li      t3, 4
    sh      t3, 0x24(sp)
    li      t3, 16
    sh      t3, 0x26(sp)
    jal     BTLP_LOAD_IMAGE
    addiu   a0, sp, 0x20
    jal     BTLP_DRAW_SYNC
    move    a0, zero
    j       btlp_act_sprites
    nop
@@queue:
    j       btlp_act_queue              ; (BTLP dead function 0x800AAFEC: vwf/vwf_btlp_queue.asm)
    nop
btlp_act_sprites:
    sw      zero, BTCFG_COUNT(s0)       ; queue consumed

    lw      a0, 0x28(sp)
    lw      t0, BT_SPRITES(s1)
    nop
    sltu    t1, t0, a0
    beqz    t1, @@sprite                ; no gap before P
    nop
@@hide:                                 ; sprites count..P-1: park off screen
    sll     t2, t0, 1
    addu    t2, t2, t0
    sll     t2, t2, 2
    addu    t2, t2, s1
    sh      zero, BT_SPRITE_LIST(t2)
    li      t3, -300
    sh      t3, BT_SPRITE_LIST + 2(t2)
    lw      t3, BT_ATTR(s1)
    addiu   t0, t0, 1
    bne     t0, a0, @@hide
    sw      t3, BT_SPRITE_LIST + 8(t2)

@@sprite:
    li      t0, 15
    divu    a0, t0
    mflo    t1                          ; row
    mfhi    t2                          ; col
    sll     t3, a0, 1
    addu    t3, t3, a0
    sll     t3, t3, 2
    addu    t3, t3, s1                  ; sprite P
    sll     t2, t2, 4
    sh      t2, BT_SPRITE_LIST(t3)
    sll     t1, t1, 4
    sh      t1, BT_SPRITE_LIST + 2(t3)
    lw      t4, BT_ATTR(s1)
    nop
    sw      t4, BT_SPRITE_LIST + 8(t3)
    lw      t0, BT_SPRITES(s1)
    addiu   t1, a0, 1
    sltu    t2, t0, t1                  ; count < P+1 ?
    beqz    t2, @@done
    nop
    sw      t1, BT_SPRITES(s1)
@@done:
    lw      ra, 0x34(sp)
    lw      s0, 0x30(sp)
    lw      s1, 0x2C(sp)
    jr      ra
    addiu   sp, sp, 0x38
