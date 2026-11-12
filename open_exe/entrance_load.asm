;; =============================================================
;; EXE/OPEN.EXE - Continue: restore the Emergency Exit / Traesto entrance and the Clean Salt timer (2026-11-11)
;;
;; The load function reads the 128-byte location sector to fp + 0x38 (slps_005.00/entrance_save.asm: + 0x18 magic,
;; + 0x1C.. the first 12 bytes of fn_tr_vars) and, for a dungeon save (+ 0x0D == 1), copies the position to
;; 0x801F15A0... The -O0 copy 0x800883C4..0x80088453 (36 words) is rewritten compactly with the restore in front.
;; Old saves (no magic) clear the record. A dungeon save also sets TRV_LOADED, so the DNG entry right after the load
;; (dng/traesto.asm) does not record the save point as a new entrance. fn_tr_vars is kernel RAM: SLPS stays resident
;; while OPEN.EXE runs.
;; =============================================================

.org 0x800883C4
.area 0x80088454 - 0x800883C4, 0
    la      t0, fn_tr_vars
    lbu     v0, 0x50(fp)                ; sector + 0x18
    ori     v1, zero, TR_SAVE_MAGIC
    lw      t1, 0x54(fp)
    lw      t2, 0x58(fp)
    beq     v0, v1, @@have
    lw      t3, 0x5C(fp)
    move    t1, zero                    ; saved before this build: nothing recorded
    move    t2, zero
    move    t3, zero
@@have:
    sw      t1, 0(t0)
    sw      t2, 4(t0)
    sw      t3, 8(t0)
    lbu     v0, 0x45(fp)                ; sector + 0x0D: saved in a dungeon
    nop
    xori    v1, v0, 1
    sltiu   v1, v1, 1
    sb      v1, TRV_LOADED(t0)
    beqz    v1, 0x80088454
    lui     t1, 0x801F
    lhu     v0, 0x46(fp)
    lhu     v1, 0x48(fp)
    sh      v0, 0x15A0(t1)              ; map
    sh      v1, 0x15A2(t1)              ; floor
    lhu     v0, 0x4A(fp)
    lhu     v1, 0x4C(fp)
    sh      v0, 0x15A4(t1)              ; x, 0x15A5
    sh      v1, 0x15A6(t1)              ; y, facing
    lbu     v0, 0x4E(fp)
    lbu     v1, 0x4F(fp)
    sb      v0, 0x15B1(t1)
    sb      v1, 0x15B2(t1)
.endarea
