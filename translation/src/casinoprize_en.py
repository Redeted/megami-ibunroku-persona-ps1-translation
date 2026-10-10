"""English prize names of the casino code machine (tools/casinoprize.py).

Key = Japanese name (text before the "9" / "+" separator). Value = variants, longest first; the longest that fits the
19-cell bar next to the tail ("+C1000000" = 9 cells, "+C5000" = 6, "+MTL CARD" = 9) is used. ALL CAPS, digits, space, hyphen only.
Item names follow the inventory (translation/strings/ITEMS.tsv); where the inventory name is a 10-glyph cut, the full name is
tried first.
"""
NAMES = {
    # sets / bundles
    'ストーンセット': ['STONE SET'],
    'インセンスセット': ['INCENSE SET', 'INCENSES'],
    'レディースセット': ['LADIES SET'],
    'おたのしみセット': ['SURPRISE SET', 'SURPRISES'],
    'ジュエリーセット': ['JEWELRY SET', 'JEWEL SET'],
    'メタルカード８８まい': ['88 CARDS'],
    'メタルカード８８': ['88 CARDS'],
    'メタルカード１０': ['10 CARDS'],
    # items (inventory names)
    'きずぐすり': ['MEDICINE'],
    'ガラガラドリンク': ['GARA DRINK'],
    'ディストーン': ['DI-STONE'],
    'ディスパライズ': ['DI-PARALYZE', 'DI-PARALYZ'],
    'ディスポイズン': ['DI-POISON'],
    'ディスシック': ['DI-SICK'],
    'ほうぎょく': ['JEWEL'],
    'ちがえしのたま': ['CHIGAESHI'],
    'ませき': ['MAGIC STONE', 'MAGICSTONE'],
    'マジカルガード': ['MAGIC GUARD', 'MAGIC GRD'],
    'フィジカルガード': ['PHYSICAL GUARD', 'PHYS GUARD'],
    'ドクロのふりこ': ['SKULL PENDULUM', 'SKULL PEND'],
    'コアシールド': ['CORESHIELD'],
    'マッスルドリンコ': ['MUSCLE DRINK', 'MUSCLE DRK'],
    'ＨＰインセンス': ['HP INCENSE'],
    'ＳＰインセンス': ['SP INCENSE'],
    'ヒランヤ': ['HIRANYA'],
    'ソーマ': ['SOMA'],
    'あまたのかね': ['MUCH MONEY'],
    'ゴッドボイス': ['GOD VOICE'],
    'あくまのいえ': ['DEMON HOME'],
    'あくまのすむいえ': ['DEMON LAIR'],
    'ミリオネアボム': ['MILLION BOMB', 'MIL BOMB'],
    'チューインソウル': ['CHEW SOUL'],
    # stones
    'マハラギストーン': ['MARAGI STONE', 'MARAGI'],
    'マハガルストーン': ['MAGARU STONE', 'MAGARU'],
    'マハブフストーン': ['MABUFU STONE', 'MABUFU'],
    'アギダインストーン': ['AGIDYNE STONE', 'AGIDYNE'],
    'ガルダインストーン': ['GARUDYNE STONE', 'GARUDYNE'],
    'ザンダインストーン': ['ZANDYNE STONE', 'ZANDYNE'],
    'グラダインストーン': ['GURADYNE STONE', 'GURADYNE'],
    'ジオダインストーン': ['ZIODYNE STONE', 'ZIODYNE'],
    'フレイダインストーン': ['FREIDYNE STONE', 'FREIDYNE'],
    'マグダインストーン': ['MAGDYNE STONE', 'MAGDYNE'],
    # tablets
    'はんげつのせきばん': ['HALF MOON TAB'],
    'こうはのせきばん': ['KOHA TABLET', 'KOHA TAB'],
    'えいはのせきばん': ['EIHA TABLET', 'EIHA TAB'],
    'せんこうのせきばん': ['FLASH TABLET', 'FLASH TAB'],
    # gems / equipment
    'ダイヤモンド': ['DIAMOND'],
    'アレキサンドライト': ['ALEXANDRITE', 'ALEXANDRIT'],
    'フィーバークラウン': ['FEVER CROWN', 'FEVER CRWN'],
    'プラチナクィーン': ['PLATINUM QUEEN', 'PLAT QUEEN'],
    'ルージュノワール': ['ROUGE NOIR'],
    'セブンズコート': ['SEVENS COAT', 'SEVENS CT'],
}
