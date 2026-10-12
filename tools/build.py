"""One-step build: tables -> VWF font -> event scripts -> armips -> patched disc image.

Usage (from the project root): python tools/build.py [--image PATH] [--no-disc] [--qol] [--psp PSP_ISO]
Output: build/ (patched files, persona.sym) and ../patched/Persona-TL.bin/.cue
--image: the original disc image (default: ../Megami Ibunroku Persona - Be Your True Mind (Japan).bin). It
         must be the first release (not Rev 1): see image_check.py.
--qol: separate enhancement build (translation + qol/*.asm, e.g. 60 fps dungeon / overworld) written to
       ../patched_qol/Persona-TL-QoL.bin/.cue instead. build/ then holds the QoL files until the next build.
--psp: separate variant with the English of the official PSP release (Shin Megami Tensei: Persona, ULUS10432)
       for the story events and demon negotiations, read from the user's own PSP ISO (tools/pspscript.py ->
       psp_text/); everything else keeps the project's translation. Written to ../patched_psp/Persona-TL-PSP.bin
       (with --qol: ../patched_psp_qol/Persona-TL-PSP-QoL.bin).
"""
import os
import shutil
import subprocess
import sys

import image_check

# Python randomises str hashes per process: some tools pack strings in set / dict order, so pin the seed
# for every tool started below to make the build byte-for-byte reproducible.
os.environ["PYTHONHASHSEED"] = "0"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINAL_IMAGE = os.path.join(ROOT, "..", "Megami Ibunroku Persona - Be Your True Mind (Japan).bin")
if "--image" in sys.argv:
    ORIGINAL_IMAGE = os.path.abspath(sys.argv[sys.argv.index("--image") + 1])
QOL = "--qol" in sys.argv
PSP_ISO = os.path.abspath(sys.argv[sys.argv.index("--psp") + 1]) if "--psp" in sys.argv else None
PATCHED_IMAGE = os.path.join(ROOT, "..", "patched" + ("_psp" if PSP_ISO else "") + ("_qol" if QOL else ""),
                             "Persona-TL" + ("-PSP" if PSP_ISO else "") + ("-QoL" if QOL else "") + ".bin")
ARMIPS = next((p for p in (os.path.join(ROOT, "tools", "armips", "armips.exe"),
                            os.path.join(ROOT, "tools", "armips", "armips"))
               if os.path.exists(p)), None) or shutil.which("armips")
JPSXDEC = os.path.join(ROOT, "tools", "ext", "jpsxdec", "jpsxdec.jar")


def run(*cmd):
    print("+", " ".join(os.path.relpath(c, ROOT) if os.path.isabs(c) else c for c in cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    py = sys.executable
    if not ARMIPS:
        sys.exit("armips not found: put armips(.exe) in tools/armips/ or on the PATH (see README.md)")
    if "--no-disc" not in sys.argv or not os.path.isdir(os.path.join(ROOT, "original")):
        image_check.require(ORIGINAL_IMAGE)
    os.environ["PERSONA_IMAGE"] = ORIGINAL_IMAGE                 # read by fmv_opening.py / endtext.py
    if not os.path.isdir(os.path.join(ROOT, "original")):           # first build: extract the game files once
        run(py, os.path.join("tools", "extract.py"), ORIGINAL_IMAGE, "original")
    run(py, os.path.join("tools", "make_tbl.py"))
    run(py, os.path.join("tools", "make_vwf_font.py"))
    os.makedirs(os.path.join(ROOT, "build", "ADV"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "translation", "images"), exist_ok=True)   # preview PNGs (not in the repository)
    if PSP_ISO:                                                # PSP-script variant: psp_text/ replaces translation/
        run(py, os.path.join("tools", "pspscript.py"), "extract", PSP_ISO)
        run(py, os.path.join("tools", "pspscript.py"), "convert")
        os.environ["PERSONA_TEXT"] = os.path.join(ROOT, "psp_text")
    run(py, os.path.join("tools", "tstatus.py"), "qa")        # fails the build on bad translations
    if not PSP_ISO:
        run(py, os.path.join("tools", "tstatus.py"), "status")    # translation/PROGRESS.md
    run(py, os.path.join("tools", "etext.py"), "build")      # translation/events -> build/ADV/E?.BIN
    run(py, os.path.join("tools", "title_gfx.py"))            # translated bitmap text -> build/gfx
    run(py, os.path.join("tools", "menu_gfx.py"))             # ADV menu labels + small-font lowercase -> build/ADV/, build/open_smallfont.asm
    run(py, os.path.join("tools", "smallfont_pages.py"))     # small-font lowercase in the 2D/ and D0x/ page copies
    run(py, os.path.join("tools", "name_grid.py"))            # name grid + name->VWF tables
    run(py, os.path.join("tools", "name_gfx.py"))             # name-entry labels -> build/name_gfx.asm
    run(py, os.path.join("tools", "s2dnames.py"), "build")    # overworld location names -> build/s2dnames*.asm
    run(py, os.path.join("tools", "s2dscript.py"), "build")   # overworld dialogue -> build/s2dscript.asm
    run(py, os.path.join("tools", "giftmsg.py"))
    run(py, os.path.join("tools", "sysmsg.py"), "build")      # system messages -> build/sysmsg.asm
    run(py, os.path.join("tools", "items.py"), "build")
    run(py, os.path.join("tools", "nicknames.py"), "build")   # party nicknames -> build/nicknames.asm
    run(py, os.path.join("tools", "partynames.py"))   # party full names -> build/partynames.asm
    run(py, os.path.join("tools", "btlfont.py"))              # battle font page (lowercase) in /B/BF.BIN -> build/B/BF.BIN
    run(py, os.path.join("tools", "btlstat.py"))              # English stat labels in the battle label atlas (after btlfont)
    run(py, os.path.join("tools", "scriptmsg.py"))            # ADV / DNG FF55 script messages (in place)
    run(py, os.path.join("tools", "menutext.py"))             # field menu strings (FORM list, item / card menus) in place
    run(py, os.path.join("tools", "skills.py"), "build")      # skill names -> build/skills.asm, build/skill_tails.asm
    run(py, os.path.join("tools", "descs.py"), "build")       # skill / item descriptions -> build/descs.asm
    run(py, os.path.join("tools", "demons.py"), "build")      # demon + race names -> build/demons.asm, races_*.asm
    run(py, os.path.join("tools", "affinity.py"), "build")    # affinity descriptions -> build/affinity.asm
    run(py, os.path.join("tools", "fusionmsg.py"))            # fusion messages + small-font map for inserted names
    run(py, os.path.join("tools", "statmsg.py"))              # equipment header strings
    run(py, os.path.join("tools", "cfgtext.py"))              # Config screen texts
    run(py, os.path.join("tools", "dngnames.py"))             # dungeon floor names -> build/D0x/D??M.BIN
    run(py, os.path.join("tools", "dngtext.py"))               # dungeon script boxes (story lines, doors) in place -> build/D0x/D??.BIN
    run(py, os.path.join("tools", "dngmsg.py"))               # dungeon in-room messages -> build/D0x/D??.BIN (after smallfont_pages)
    run(py, os.path.join("tools", "personas.py"), "build")    # Persona names -> build/personas.asm, persona_tails.asm
    run(py, os.path.join("tools", "btlevt.py"), "build")      # story-battle dialogue -> build/btlevt*.asm
    run(py, os.path.join("tools", "btlmsg.py"), "build")      # battle messages -> build/btlmsg.asm, btlmsg_slps.asm
    run(py, os.path.join("tools", "btlneg.py"), "build")      # negotiation messages -> build/btlneg.asm
    run(py, os.path.join("tools", "btlui.py"))                # battle UI: ANALYZE labels, race tags, personalities, AUTO
    run(py, os.path.join("tools", "btlcmd.py"))               # CONTACT command names
    run(py, os.path.join("tools", "opentext.py"))             # LOAD GAME screen: card messages + SLOT buttons
    run(py, os.path.join("tools", "banner.py"), "build")      # battle banner names -> build/banner_btlp.asm, banner_slps.asm
    run(py, os.path.join("tools", "choices.py"), "build")     # dialogue choices -> build/choices.asm
    os.makedirs(os.path.join(ROOT, "build", "TALK"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "build", "EXE"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "build", "ADV"), exist_ok=True)
    qol = ["-definelabel", "QOL60", "1"] if QOL else []            # main.asm: .ifdef QOL60 -> qol/fps60_*.asm
    run(ARMIPS, "main.asm", "-sym2", os.path.join("build", "persona.sym"), *qol)
    run(py, os.path.join("tools", "casinoprize.py"))          # casino code machine prize bar (in place in build/CASINO.BIN, after armips)
    run(py, os.path.join("tools", "talktl.py"), "qa")         # translated TALK units: codes / 3 lines / 239 px
    run(py, os.path.join("tools", "talk.py"), "build")        # translation/talk -> build/TALK (edited files only)
    run(py, os.path.join("tools", "etctalk.py"), "build")    # TALK/ETC.BIN (other layout) -> build/TALK
    run(py, os.path.join("tools", "endtext.py"))                  # ending epilogue text pages -> build/EXE/END.BIN
    if "--no-disc" not in sys.argv:
        os.makedirs(os.path.dirname(PATCHED_IMAGE), exist_ok=True)
        run(py, os.path.join("tools", "build_disc.py"), ORIGINAL_IMAGE, PATCHED_IMAGE, "build")
        if not os.path.exists(JPSXDEC):
            print("WARNING: tools/ext/jpsxdec/jpsxdec.jar not found: the movies keep their Japanese text (see README.md)")
        else:                                                                            # burned-in English subtitles of the opening movie
            run(py, os.path.join("tools", "fmv_opening.py"), PATCHED_IMAGE)
            run(py, os.path.join("tools", "fmv_subs.py"), PATCHED_IMAGE)             # subtitles of the voiced movies
            run(py, os.path.join("tools", "fmv_poems.py"), PATCHED_IMAGE)            # epilogue poems of MV1E / MV25


if __name__ == "__main__":
    main()
