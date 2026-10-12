;; =============================================================
;; QoL (separate enhancement build): Persona summons and skill effects in battle at double speed (BTLP.BIN).
;; The battle main loop (0x80090050, loop 0x80090080) runs one logic tick per iteration and presents it with
;; the frame function 0x80080F14 (called at 0x80092270). Its swap code waits with VSync(0) once (60 fps), or
;; twice while the effect players (0x800B1C5C, 0x800B29DC, 0x800B6F94, 0x800B76F0) hold the half-rate flag
;; 0x800CF073 (summons, skill / magic effects: 30 fps, the slow part). Code that needs real-time speed reads the
;; same flag and doubles its step (fades 0x10 -> 0x20, 0x8008BF94 ...), the model animation advances once per
;; tick. Dropping the second wait gives exactly twice the tick rate there: the whole effect runs 2x, including
;; the compensated parts; menus, text and everything at 60 fps keep their speed.
;; Sound is not touched: the SPU plays every sample at its own pitch and length, so voices ("Persona!") and
;; effect sounds keep their original speed and only start earlier. Measured (round of 5 Persona skills, state
;; on the Yes prompt): 700 ticks 1169 -> 715 vblanks; SPU samples end by themselves as before.
;; If a frame takes longer than one vblank (real hardware, heavy effects), VSync(0) waits for the next one:
;; the effect is then between 1x and 2x, never slower than the original.
;; =============================================================
.org 0x800811B8
    nop                                         ; was jal VSync (second wait of the half-rate mode); the delay
                                                ; slot (move a0, zero) is harmless
