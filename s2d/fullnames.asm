;; =============================================================
;; S2D.BIN - item names as full-name markers (slps_005.00/fullnames.asm), see adv/fullnames.asm.
;; 0x800673E0 = string-to-map copy (same code as ADV 0x80067C00): item / equipment menus of the overworld menu.
;; =============================================================

.org 0x800673E0
    lui     t9, 0x8006                          ; was andi v0, a3, 0xFFFF
    j       fn_adv_copy                         ; was beq v0, zero, ...
    ori     t9, t9, 0x73EC                      ; was nop. t9 = copy + 0xC (the plain path returns there)

;; Persona status page bar: proportional arcana + full Persona name (drawer cell-advance, page function, name object)
    persona_bar_hooks 0x80065740, 0x8006F26C, 0x8009D7F0

;; ANALYZE demon page bar: proportional race + full demon name (name fill jal, name object)
    analyze_bar_hooks 0x80089A1C, 0x8009FF2C
