;; QoL: GAME END returns to the title screen (stub and notes: qol/gameend_slps.asm)
.org 0x8009AE68                         ; after the "any button" wait: j 0x8009AEB0 (delay slot nop kept)
    j       qol_gameend
