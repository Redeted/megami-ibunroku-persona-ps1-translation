;; =============================================================
;; SLPS_005.00 - Emergency Exit / Traesto entrance and the Clean Salt timer in memory-card saves (2026-11-11)
;;
;; fn_tr_vars (kernel RAM, dng/traesto.asm) is not part of the saved block (0x801F1BCC, 0x3780 bytes), so a save made
;; inside a dungeon lost the entrance. The save function 0x80013E2C first writes a 128-byte location sector
;; (0x8005E380: +0x0D dungeon flag, +0x0E.. map / floor / position, +0x7F XOR checksum); +0x18..+0x7E were always 0.
;; It now also stores TR_SAVE_MAGIC at +0x18 and the first 12 bytes of fn_tr_vars at +0x1C (entrance, Clean Salt
;; timer), before the checksum. Old saves have 0 there. The title's Continue (EXE/OPEN.EXE, open_exe/entrance_load.asm)
;; restores them; SLPS 0x80014660 (the EXE's copy of that loader) is never called.
;;
;; The checksum loop 0x80014348..0x800143C3 (-O0 code, 31 words) is rewritten compactly to make room.
;; =============================================================

TR_SAVE_MAGIC   equ 0x54                ; location sector + 0x18: entrance record present

.ifdef QOL60                            ; QoL build only (equ above: armips allows none inside .ifdef)

.org 0x80014348
.area 0x800143C4 - 0x80014348, 0
    lui     t1, 0x8006
    addiu   t1, t1, -0x1C80             ; location sector 0x8005E380
    la      t0, fn_tr_vars
    ori     v0, zero, TR_SAVE_MAGIC
    sb      v0, 0x18(t1)
    lw      v0, 0(t0)                   ; valid, fresh, pending, floor
    lw      v1, 4(t0)                   ; map, x, y
    sw      v0, 0x1C(t1)
    lw      v0, 8(t0)                   ; facing, Clean Salt timer, "wore off", last map
    sw      v1, 0x20(t1)
    sw      v0, 0x24(t1)
    lbu     v1, 0x68(fp)                ; checksum (starts at 0)
    move    v0, t1
    addiu   t2, t1, 0x7F
@@sum:
    lbu     t3, 0(v0)
    addiu   v0, v0, 1
    bne     v0, t2, @@sum
    xor     v1, v1, t3
    sb      v1, 0x68(fp)
    sb      v1, 0(v0)                   ; + 0x7F
.endarea
.endif                                  ; QOL60
