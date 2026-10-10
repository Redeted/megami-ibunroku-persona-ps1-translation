;; =============================================================
;; SLPS_005.00 - Free space for cross-binary string relocation
;; The main EXE stays resident while overlays swap, so strings
;; placed here can be referenced from any overlay.
;; Verify SLPS_FREE_START..SLPS_FREE_END is unused before relying on it.
;; =============================================================

.org SLPS_FREE_START
.area SLPS_FREE_END - SLPS_FREE_START
; relocated_example_str:
;     .string LONG_EXAMPLE_STR
.endarea
