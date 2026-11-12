;; =============================================================
;; QoL (separate enhancement build): GAME END at an Agastya tree returns to the title screen.
;; Original (ADV 0x8009ADFC): message 9 "turn off the power (any button returns to the game)", then a wait loop
;; (0x8009AE44) and the menu state 0x800BCB3C = 0xFF (back to the game). The suspend save (message 20, 0x8009B790)
;; ends the game by setting the bytes 0x800BC320 and 0x800BCB40 to 1: the same two flags are set here after the
;; button, so the event overlay leaves with next mode -1 (ATLUS logo, title). Verified live 2026-11-11.
;; Stub in two unreferenced SLPS functions (0x8001A4A8-0x8001A510, free since 2026-10-05); hook: qol/gameend_adv.asm.
;; The message itself is replaced in the QoL build by tools/sysmsg.py (QOL).
;; =============================================================
.org BTLP_PAGE_FIX_ADDR
.area BTLP_PAGE_FIX_SIZE
qol_gameend:
    lui     v1, 0x800C
    ori     v0, zero, 1
    sb      v0, -0x3CE0(v1)             ; 0x800BC320
    sb      v0, -0x34C0(v1)             ; 0x800BCB40
    j       0x8009AEB0                  ; menu state = 0xFF (leave the Agastya menu)
    ori     v0, zero, 0xFF
.endarea
