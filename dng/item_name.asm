;; =============================================================
;; DNG.BIN - full item name for the FF09 insert of the dungeon script boxes (full item names, translation).
;; Included by dng/estoma.asm inside the second DNG extension (QoL build) or placed at its start (base build).
;; =============================================================
;; FF09 item name insert of the dungeon script boxes (hook 0x800741E8 in dng/vwf_script.asm): a0 = 1-based item id << 5,
;; s5 = script read pointer. Prints the full title-cased name (fn_item_text into fn_buf: the sorter is not running here).
dng_item_name:
    addiu   sp, sp, -0x20
    sw      ra, 0x1C(sp)
    sw      s5, 0x18(sp)                        ; fn_item_text clobbers s5 (and v0, v1, at, t3, t5)
    sw      s2, 0x14(sp)
    srl     s2, a0, 5
    la      a1, fn_buf
    jal     fn_item_text
    nop
    lw      s5, 0x18(sp)
    lw      s2, 0x14(sp)
    la      a0, fn_buf
    jal     0x800753AC                          ; name printer (FF-terminated, a1 = max glyphs)
    li      a1, FN_BUF_SIZE - 1
    lw      ra, 0x1C(sp)
    nop
    j       0x8007423C                          ; as the original after the name printer: next script byte
    addiu   sp, sp, 0x20
