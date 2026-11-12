;; =============================================================
;; DNG.BIN - item names as full-name markers (slps_005.00/fullnames.asm), see adv/fullnames.asm.
;; 0x8007782C = string-to-map copy (same code as ADV 0x80067C00): item / equipment menus of the dungeon menu.
;; =============================================================

.org 0x8007782C
    lui     t9, 0x8007                          ; was andi v0, a3, 0xFFFF
    j       fn_adv_copy                         ; was beq v0, zero, ...
    ori     t9, t9, 0x7838                      ; was nop. t9 = copy + 0xC (the plain path returns there)

;; Persona status page bar: proportional arcana + full Persona name (drawer cell-advance, page function, name object)
    persona_bar_hooks 0x80075B50, 0x8007F464, 0x8009AC60

;; ANALYZE demon page bar: proportional race + full demon name (name fill jal, name object)
    analyze_bar_hooks 0x80099920, 0x8009D39C
