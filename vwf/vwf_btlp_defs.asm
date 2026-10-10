;; BTLP VWF constants (included before the code that uses them)
BTLP_LOAD_IMAGE         equ 0x8002B810  ; void LoadImage(RECT*, void* src)
BTLP_DRAW_SYNC          equ 0x8002B5E8  ; int DrawSync(int)

;; text struct fields
BT_ATTR                 equ 0x10        ; sprite attribute word
BT_CELL                 equ 0x1C        ; cell counter (0..44), engine "pos" is its low half
BT_SPRITES              equ 0x20        ; sprite count
BT_SPRITE_LIST          equ 0x28        ; 12-byte sprites {s16 x, s16 y, 0, 0, u32 attr}
BT_TEX_X                equ 0x26C
BT_TEX_Y                equ 0x26E
BT_STATE_OFFSET         equ 0x12        ; engine pos = state + 0xA = struct + 0x1C


STR16_MAX_CELLS         equ 15          ; cells (16 px) per string of the 16 px string renderer
BTLP_LQUEUE             equ 0x80066620  ; queue a LoadImage: (src, x, y, w) + h at sp+0x10, flushed at the end of the frame
