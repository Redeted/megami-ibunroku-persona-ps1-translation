# BTLP negotiation-text VWF hook: findings and design

**STATUS 2026-10-03: IMPLEMENTED and verified in game** (vwf/vwf_btlp.asm, vwf/vwf_btlp_activate.asm, vwf/vwf_btlp_defs.asm, btlp/vwf_hooks.asm). English VWF text renders correctly in the negotiation box (white, shadow, variable width, 2 lines + FFF6 newline; tested by writing bytes into the TALK buffer on state slot 5 via live write_memory). Deviations from the design below: the text struct is passed in a0 and stored per call (the second call site may use another instance); activate reads the queued ring cell from the config scratch entry and clears the count; code is split over two dead SLPS fragments (0x8001EE84 emit, 0x800124B4 activate); scratch = vwf_cfg_btlp (0x80021A80, 36 bytes). Not yet done: full-disc build test with TALK English, 0x8007BF44 string renderer (header/name text) still Japanese 16px.


Findings (BTLP.BIN, overlay base 0x800643C4):
- Text struct at 0x800EB890: +2 state (s16), +8 read ptr, +0x10 clut-row attr, +0x1C cell counter (0..44, 15/line x 3),
  +0x20 sprite count, +0x28 sprites[48] x 12 B {x s16, y s16, 0, 0, attr u32}, +0x268/+0x26A screen offset (0x20,0xAC),
  +0x26C/+0x26E texture VRAM base (0x380,0x100). Sprite k uses texture cell k of a 15-wide grid (x=base+(k%15)*4, y=base+(k/15)*16).
- Interpreter 0x8007C9E0(struct, ptr)->ptr; ordinary chars call glyph fn 0x8007C754(struct, ptr)->ptr
  (call sites 0x8007CCD4 and 0x8007CF80). Decoder 0x8007BF00 treats every byte >= 0x80 as a 2-byte lead (needs the 88-E6 exception).
- Whole page is emitted in ONE call per frame when struct+0x18 (delay) == 0. Original glyph ring (0x800EBE48) and LoadImage queue
  (0x80066620, 72 entries) are reset every frame, so they cannot hold cells across frames.
- Upload directly: LoadImage = 0x8002B810(RECT*, src), then DrawSync(0) = 0x8002B5E8(0) (the game's own sync pattern).
- No dead code in BTLP; no free FONT.BIN slots; SLPS tail 0x80055C10-0x80056000 is runtime data (NOT free).
  Free homes: dead SLPS fragments 0x800124B4 (328 B), 0x80015510 (252), 0x8001EE84-0x8001EFA0 (284), 0x8002BC84 (220);
  VWF_DATA block has 56 spare bytes after vwf_cfg_s2d (0x80021A80-0x80021AB8).
- TALK text pointer = 0x801C0000 + table[i] + 0x14 (fn 0x80074BAC).

Design:
1. btlp_vwf_emit(a0=struct,a1=ptr)->v0: decode (byte<0x80 or 0x88-0xE6 single; else glyph=((b&7)<<8)|next | 0x8000),
   s2 = next ptr, call vwf_dialog_emit(cfg_btlp, 0, a2), return s2. Patch jal at 0x8007CCD4 and 0x8007CF80.
2. cfg_btlp = {STATE=0x800EB8A2 (struct+0x12 so state+0xA = cell counter), ACTIVATE=btlp_activate, UPLOAD_COUNT/QUEUE=16 B scratch}.
3. btlp_activate(a0=P): LoadImage the ring cell (vwf_dlg_ring + ((P%15)&3)*128) to VRAM slot P, DrawSync(0);
   write sprite P {x=(P%15)*16,y=(P/15)*16,attr=struct+0x10}; sprites count..P-1 hidden (y=-300); count=max(count,P+1). Preserve s regs.
4. Then: tools/talk.py already rebuilds TALK files; add them to build, fixed slots, test in battle (slot 5 area), translate.
