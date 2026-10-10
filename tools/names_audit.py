"""Generate translation/NAMES_AUDIT.md: every speaker label and recurring proper noun in the
event scripts with counts, first location, the proposed English and a confidence level.

  python tools/names_audit.py

Edit PROPOSALS below (term -> (english, confidence, note)); confidence:
  ok      matches the glossary / obvious reading / official name known
  check   probable but verify (kanji read from the game font, or no official source known)
  ask     do not use until a human decides
Terms with `ok` that are not yet in glossary.tsv are listed at the end ready to paste.
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tstatus  # noqa: E402

ROOT = tstatus.ROOT

# ---- speaker labels (the part before the colon) -------------------------------------
SPEAKERS = {
    '南条': ('Nanjo', 'ok', 'glossary'), 'マーク': ('Mark', 'ok', 'glossary'),
    'アヤセ': ('Ayase', 'ok', 'glossary'), 'エリー': ('Elly', 'ok', 'glossary'),
    '麻希': ('Maki', 'ok', 'glossary'), 'ブラウン': ('Brown', 'ok', 'glossary'),
    'ゆきの': ('Yukino', 'ok', 'glossary'), '玲司': ('Reiji', 'ok', 'Kido Reiji (城戸 玲司)'),
    '神取': ('Kandori', 'ok', 'the main antagonist'),
    '生徒': ('Student', 'ok', ''), '客': ('Customer', 'ok', ''), '店員': ('Clerk', 'ok', ''),
    '店主': ('Shopkeeper', 'ok', ''), '医師': ('Doctor', 'ok', ''), '看護婦': ('Nurse', 'ok', 'glossary'),
    '科学者': ('Scientist', 'ok', ''), '男': ('Man', 'ok', ''), '青年': ('Young Man', 'ok', ''),
    '老人': ('Old Man', 'ok', ''), '患者': ('Patient', 'ok', ''), '部長': ('Club President', 'check', 'which club varies by scene'),
    '先生': ('Teacher', 'ok', ''), '悪魔': ('Demon', 'ok', ''), '警官': ('Police Officer', 'ok', ''),
    '警部': ('Inspector', 'ok', ''), '街の人': ('Townsperson', 'ok', ''), '町の人': ('Townsperson', 'ok', ''),
    '女子高生': ('Schoolgirl', 'ok', ''), '男子生徒': ('Boy Student', 'ok', ''), '女子生徒': ('Girl Student', 'ok', ''),
    '女子大生': ('College Girl', 'ok', 'glossary'), '妊婦': ('Pregnant Woman', 'ok', 'glossary'),
    '山岡': ('Yamaoka', 'ok', 'glossary'), '稲葉': ('Inaba', 'ok', 'glossary'),
    '白い女の子': ('Girl in White', 'ok', 'glossary'), '黒い女の子': ('Girl in Black', 'ok', ''),
    '麻希の母': ("Maki's Mother", 'ok', ''), '玲司の母': ("Reiji's Mother", 'ok', ''), 'マークの母': ("Mark's Mother", 'ok', ''),
    '久美の父親': ("Kumi's Father", 'ok', ''), '神取の声': ("Kandori's Voice", 'ok', ''), '麻希の声': ("Maki's Voice", 'ok', ''),
    '冴子先生': ('Saeko-sensei', 'ok', 'honorific kept'), '夏美先生': ('Natsumi-sensei', 'ok', '吉野 夏美 Yoshino Natsumi'),
    '大石校長': ('Principal Oishi', 'check', 'family name 大石; title Principal'),
    '反谷教頭': ('Vice Principal Hanya', 'check', 'nickname ハンニャ; kanji 反谷 may be 般若-like pun; verify reading'),
    '姫野': ('Himeno', 'ok', '姫野 由子 Himeno Yuko'), '内藤': ('Naito', 'check', ''), '香西': ('Kosai', 'check', 'reading of 香西: Kosai vs Kasai'),
    '金田': ('Kaneda', 'check', ''), '武多': ('Takeda', 'ask', 'kanji 武多 = ? (glyph may be misread)'),
    '黒瓜': ('Kurouri', 'ask', 'kanji 黒瓜 looks odd (glyph misread?)'),
    'たまきちゃん': ('Tamaki-chan', 'ok', ''), 'ただしくん': ('Tadashi-kun', 'ok', ''), '紀一君': ('Kiichi-kun', 'check', ''),
    '久美': ('Kumi', 'ok', ''), 'あき': ('Aki', 'ok', ''), 'まい': ('Mai', 'ok', ''), '陽介': ('Yosuke', 'ok', ''),
    '知美': ('Tomomi', 'ok', ''), '百合子': ('Yuriko', 'ok', ''), '美智子': ('Michiko', 'ok', ''), '真理子': ('Mariko', 'ok', ''),
    '千里': ('Chisato', 'check', 'or Senri'), 'テッソ': ('Tesso', 'check', ''), 'トリッシュ': ('Trish', 'check', ''),
    'トロ': ('Toro', 'check', 'boy fed by the Hee-Ho; kana name'),
    'クイーン': ('Queen', 'ok', 'casino/Queen figure; check against the story'),
    '雪の女王': ('Snow Queen', 'ok', 'official PSP name'), '雪の女王の声': ("Snow Queen's Voice", 'ok', ''),
    '夜の女王': ('Queen of the Night', 'check', ''), '夜の女王の声': ("Queen of the Night's Voice", 'check', ''),
    '蝶': ('Butterfly', 'check', 'a talking butterfly'),
    'イゴール': ('Igor', 'ok', 'official'), 'ヒュプノス': ('Hypnos', 'ok', 'official PSP'), 'ネメシス': ('Nemesis', 'ok', 'official'),
    'タナトス': ('Thanatos', 'ok', 'official'), 'パンドラ': ('Pandora', 'ok', 'official'),
    'ケルベロス': ('Cerberus', 'ok', 'official'), 'ハリティー': ('Hariti', 'ok', 'official'),
    'ヒーホー君': ('Hee-Ho-kun', 'check', 'Jack Frost-type demon; official PSP "Jack Frost"? verify'),
    'ヒホ子ちゃん': ('Hee-Ho-ko-chan', 'check', ''),
    'ニコライ博士': ('Dr. Nikolai', 'check', 'Nicolai vs Nikolai; 2009 PSP spelling unknown'),
    'アガスティアの木': ('Agastya Tree', 'check', 'official PSP name unknown (Agasthya/Agastya)'),
    '仮面の男子生徒': ('Masked Boy', 'ok', ''), '仮面の女子生徒': ('Masked Girl', 'ok', ''), '仮面': ('Mask', 'ok', ''),
    '悪魔先生': ('Demon Teacher', 'check', ''), '演劇部員': ('Drama Club Member', 'ok', ''), '演劇部部長': ('Drama Club President', 'ok', ''),
    'あの声': ('That Voice', 'check', ''), '？？？': ('???', 'ok', ''), '声': ('Voice', 'ok', ''), '女王': ('Queen', 'ok', ''),
    '生徒会長': ('Student Council President', 'ok', ''), '役員': ('Council Member', 'ok', ''),
    'セベク社員': ('SEBEC Employee', 'check', 'SEBEC spelling'), '受付嬢': ('Receptionist', 'ok', ''),
    '見張り': ('Guard', 'ok', ''), '黒服の男': ('Man in Black', 'ok', ''), 'マスター': ('Master', 'ok', 'bar/shop owner'),
    '博士の声': ("Doctor's Voice", 'ok', ''), '下級生': ('Underclassman', 'ok', ''), '先生の彼': ("Teacher's Boyfriend", 'ok', ''),
    '男子部員': ('Boy Club Member', 'ok', ''), '女子部員': ('Girl Club Member', 'ok', ''), '婦警': ('Policewoman', 'ok', ''),
    '女の子': ('Girl', 'ok', ''), '若者': ('Youth', 'ok', ''), 'マヌカン': ('Mannequin', 'check', 'boutique clerk slang (マヌカン)'),
    'コギャル': ('Kogal', 'ok', 'glossary'), 'カエル': ('Frog', 'ok', ''), '化学教師': ('Chemistry Teacher', 'ok', ''),
    'さとりちゃん': ('Satori-chan', 'check', ''), 'アフロさん': ('Afro-san', 'check', 'nickname'), '生徒の霊': ("Student's Ghost", 'ok', ''),
    '教師': ('Teacher', 'ok', ''), '一同': ('Everyone', 'ok', ''), '全員': ('Everyone', 'ok', ''), '怪物': ('Monster', 'ok', ''), '魔物': ('Monster', 'ok', ''),
    '男たち': ('Men', 'ok', ''), '青年たち': ('Young Men', 'ok', ''), '女性の声': ("Woman's Voice", 'ok', ''), '男の声': ("Man's Voice", 'ok', ''),
    '女の子の声': ("Girl's Voice", 'ok', ''), 'まいの声': ("Mai's Voice", 'ok', ''), '警官の霊': ("Police Officer's Ghost", 'ok', ''),
    '悪魔警官': ('Demon Officer', 'ok', ''), '悪魔警部': ('Demon Inspector', 'ok', ''), '怪我した男': ('Injured Man', 'ok', 'glossary'),
    'サラリーマン': ('Salaryman', 'ok', 'glossary'), '看護婦長': ('Head Nurse', 'ok', ''),
}

# ---- other recurring proper nouns ---------------------------------------------------
TERMS = {
    'セベク': ('SEBEC', 'check', 'company; official PSP spelling to confirm'),
    'ペルソナ': ('Persona', 'ok', 'official'), 'ペルソナ様': ('Persona-sama', 'ok', 'glossary'),
    'コンパクト': ('Compact', 'check', 'the COMP device'), 'エルミン': ('Elmin', 'check', 'Elmin Gakuen (Elmin High School)'),
    'ノモラカ': ('Nomoraka', 'ask', 'unknown term'), 'アラヤ': ('Alaya', 'check', 'Alaya (official: Alaya Shrine?)'),
    'デヴァ': ('Deva', 'check', ''), 'ゲルダ': ('Gerda', 'check', ''), 'ロゼッタ': ('Rosetta', 'check', ''),
    'レイジ': ('Reiji', 'ok', 'katakana spelling of 玲司'), 'ニコライ': ('Nikolai', 'check', ''),
    'アンブロシア': ('Ambrosia', 'ok', ''), 'タルタロス': ('Tartarus', 'ok', ''), 'ヨグソトスＪｒ': ('Yog-Sothoth Jr.', 'check', ''),
    'タノママー': ('Tanomamaa', 'ask', 'shop/character name'), 'タノママ': ('Tanomama', 'ask', ''),
    'ピースダイナー': ('Peace Diner', 'ok', 'glossary'), 'ジョイ通': ('Joy-dori', 'ok', 'glossary'),
    'ハーレム': ('Harlem', 'check', ''), 'テイラーズ': ('Taylor\'s', 'check', 'shop'),
    '御影': ('Mikage', 'check', 'place name; was misread as 御彰 before the font fix'),
    '御影町': ('Mikage-cho', 'check', ''), '矢来区': ('Yarai Ward', 'check', 'kanji 矢来 (Yarai); ward'),
    'セブンスターズ': ('Seven Stars', 'ask', 'school name?'), 'ハンニャ': ('Hanya', 'check', 'nickname of the vice principal'),
}


def main():
    load = tstatus.load_glossary
    load()
    seen, texts = set(), []
    for n, e, k, ja, en in tstatus.rows():
        if ja in seen:
            continue
        seen.add(ja)
        texts.append((f'{n}/{e}/{k}', ja))
    sp_count, sp_first = collections.Counter(), {}
    for loc, ja in texts:
        s = tstatus.speaker(ja)
        if s:
            sp_count[s] += 1
            sp_first.setdefault(s, loc)
    plain = [(loc, re.sub(r'<[^>]+>', '', ja)) for loc, ja in texts]
    tm_count, tm_first = collections.Counter(), {}
    for t in TERMS:
        for loc, t_ in plain:
            c = t_.count(t)
            if c:
                tm_count[t] += c
                tm_first.setdefault(t, loc)
    L = ['# Names audit (generated by `python tools/names_audit.py`; edit the PROPOSALS in that script)', '',
         'confidence: **ok** use as is | **check** probable, verify before the story is finished | **ask** do not use, human decides',
         '', 'Kanji in this project were identified from the game font by image matching; five misreads were found',
         'and fixed by a visual audit (風 確 影 審 粗). Names that depend on rare kanji are marked `ask`/`check`.', '',
         '## Speaker labels', '', '| Japanese | uses | first | English | confidence | note |', '|---|---|---|---|---|---|']
    unknown = []
    for s, c in sp_count.most_common():
        en, conf, note = SPEAKERS.get(s, ('?', 'ask', 'not decided'))
        if s not in SPEAKERS:
            unknown.append(s)
        L.append(f'| {s} | {c} | {sp_first[s]} | {en} | {conf} | {note} |')
    L += ['', '## Recurring proper nouns and terms', '', '| Japanese | uses | first | English | confidence | note |', '|---|---|---|---|---|---|']
    for t, (en, conf, note) in TERMS.items():
        if tm_count[t]:
            L.append(f'| {t} | {tm_count[t]} | {tm_first[t]} | {en} | {conf} | {note} |')
    L += ['', f'Undecided speaker labels: {len(unknown)} {unknown}', '']
    open(os.path.join(ROOT, 'translation', 'NAMES_AUDIT.md'), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L))
    todo = [(s, v) for s, v in SPEAKERS.items() if v[1] == 'ok' and s not in tstatus.GLOSS and s in sp_count]
    print(f'{len(sp_count)} speaker labels, {len(unknown)} undecided; {len(todo)} ok labels missing from glossary.tsv')
    return todo


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
