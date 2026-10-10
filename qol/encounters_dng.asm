;; =============================================================
;; QoL (separate enhancement build): half the random encounter rate in the 3D dungeons (DNG.BIN).
;; Original (0x8007099C, once per step on a cell with encounter level 1..3): no roll while the cooldown
;; byte (player struct +0x15B0, set to 7 after a battle) counts down, then a battle when
;; rand() % divisor == 0 (table 0x80099ED0: -, 8, 4, 2). Mean steps between battles = 7 + divisor =
;; 15 / 11 / 9. Doubling both terms (cooldown 14, divisors 16 / 8 / 4) gives 30 / 22 / 18: exactly half
;; as many battles. Constants only, no new code.
;; =============================================================
.org 0x80070A8C
    ori     v0, zero, 14                        ; cooldown after a fixed-formation cell battle (was 7)
.org 0x80070B50
    ori     v0, zero, 14                        ; cooldown after a random battle (was 7)
.org 0x80099ED0
    .halfword 0, 16, 8, 4                       ; per-step chance 1 / divisor (was 0, 8, 4, 2)
