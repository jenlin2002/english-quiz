# 主題 2000 字 Unit 25：Geographical terms 地理名詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# bank、beach、pool（Unit 17）、spring（Unit 8 春天）在前面出現過，這裡用地理的意思（河岸、泉水…）。
def W(w, pos, zh, note, ex, exzh, pic, exsay=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if exsay:
        d['exsay'] = exsay   # 語音唸法（Mt. 要唸成 Mount）
    return d

UNIT = {
  'book': 'w2000', 'no': 25, 'en': 'Geographical terms', 'zh': '地理名詞',
  'intro': '山、河、湖、海、島……描述地形的 12 個字。有些字前面單元學過別的意思：bank 也是「河岸」、spring 也是「泉水」。',
  'words': [
    W('area', 'n.', '地區；面積；範圍', '', 'This area is famous for its tea.', '這個地區以茶聞名。', '🗺️'),
    W('bank', 'n.', '河岸；銀行', 'river bank 河岸', 'We had a picnic on the bank of the river.', '我們在河岸邊野餐。', '🏞️'),
    W('beach', 'n.', '海灘', '複數 beaches', 'The kids built a sandcastle on the beach.', '孩子們在海灘上堆沙堡。', '🏖️'),
    W('hill', 'n.', '小山；丘陵', 'on the top of the hill 在山頂上', 'Our school is at the foot of a hill.', '我們學校在小山的山腳下。', '⛰️'),
    W('island', 'n.', '島', 's 不發音', 'Taiwan is a beautiful island.', '臺灣是個美麗的島嶼。', '🏝️'),
    W('lake', 'n.', '湖', 'Sun Moon Lake 日月潭', 'We went boating on Sun Moon Lake.', '我們去日月潭划船。', '🛶'),
    W('mountain', 'n.', '山；山岳', '縮寫 Mt.；Mt. Jade 玉山', 'Mt. Jade is the highest mountain in Taiwan.', '玉山是臺灣最高的山。', '🏔️',
      exsay='Mount Jade is the highest mountain in Taiwan.'),
    W('pond', 'n.', '池塘', '比 lake 小', 'There are some fish in the pond.', '池塘裡有一些魚。', '🦆'),
    W('pool', 'n.', '水池；游泳池', 'swimming pool 游泳池', 'The kids are swimming in the pool.', '孩子們在游泳池游泳。', '🏊'),
    W('river', 'n.', '河', 'the Tamsui River 淡水河', 'A long river runs through the city.', '一條長長的河流經這座城市。', '🏞️'),
    W('sea', 'n.', '海', 'by the sea 在海邊', 'We swam in the sea last summer.', '去年夏天我們在海裡游泳。', '🌊'),
    W('spring', 'n./v.', '泉水；春天；彈簧；跳躍', 'hot spring 溫泉；三態 spring／sprang／sprung', 'Grandpa likes to take a hot spring bath in winter.', '爺爺冬天喜歡泡溫泉。', '♨️'),
  ],
  'focus': [
    {'title': '比大小：哪個大？', 'head': ('小', '大', ''), 'rows': [
      ('hill 小山', 'mountain 山', ''),
      ('pond 池塘', 'lake 湖', ''),
      ('river 河', 'sea 海 → ocean 洋', ''),
      ('island 島', '（大陸 mainland）', ''),
    ], 'note': '山、河、湖的名字常加在前面：Mt. Jade（玉山）、the Tamsui River（淡水河）、Sun Moon Lake（日月潭）。'},
    {'title': '臺灣的地理名稱', 'head': ('英文', '中文', ''), 'rows': [
      ('Mt. Jade', '玉山', ''),
      ('Sun Moon Lake', '日月潭', ''),
      ('the Tamsui River', '淡水河', ''),
      ('Kenting Beach', '墾丁海灘', ''),
      ('Green Island', '綠島', ''),
      ('Wulai Hot Spring', '烏來溫泉', ''),
    ], 'note': '河、海前面通常加 the：the Tamsui River、the Pacific Ocean。'},
    {'title': '介系詞：on、in、by', 'head': ('說法', '意思', '例句'), 'rows': [
      ('on the beach', '在海灘上', 'We played on the beach.'),
      ('in the sea / in the river / in the lake', '在海裡、河裡、湖裡（水中）', 'Fish live in the river.'),
      ('on the lake / on the river', '在湖面上、河面上', 'A boat is on the lake.'),
      ('by the sea / by the river', '在海邊、河邊', 'They live by the sea.'),
      ('on the top of the hill', '在山頂上', 'There is a house on the top of the hill.'),
    ], 'note': '在島上用 on：on the island、on Green Island。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '島', 'opts': ['island', 'Ireland', 'lake', 'land'], 'answer': 0, 'exp': 'island 島，s 不發音。'},
    {'type': 'mc', 'q': '池塘', 'opts': ['pool', 'pond', 'point', 'pound'], 'answer': 1, 'exp': 'pond 池塘。'},
    {'type': 'mc', 'q': '小山；丘陵', 'opts': ['mountain', 'hall', 'hill', 'heel'], 'answer': 2, 'exp': 'hill 小山。'},
    {'type': 'mc', 'q': '地區；面積', 'opts': ['area', 'earth', 'address', 'army'], 'answer': 0, 'exp': 'area 地區、面積。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'river', 'opts': ['湖', '海', '河', '池塘'], 'answer': 2, 'exp': 'river 河。'},
    {'type': 'mc', 'q': 'beach', 'opts': ['海灘', '山頂', '河岸', '橋'], 'answer': 0, 'exp': 'beach 海灘。'},
    {'type': 'mc', 'q': 'mountain', 'opts': ['小山', '山；山岳', '高原', '島'], 'answer': 1, 'exp': 'mountain 山（比 hill 大）。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '山（m＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['mountain']], 'exp': 'mountain，中間是 ou、ai。'},
    {'q': '島（i＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['island']], 'exp': 'island，s 不發音。'},
    {'q': '湖（l＿＿＿，4 個字母）：{0}', 'blanks': [['lake']], 'exp': 'lake。'},
    {'q': '海（s＿＿，3 個字母）：{0}', 'blanks': [['sea']], 'exp': 'sea（和 see 同音）。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'We went to Beitou to take a hot {0} bath. （泉水）', 'blanks': [['spring']], 'exp': 'hot spring 溫泉。'},
    {'q': 'There are many flowers on the river {0}. （河岸）', 'blanks': [['bank']], 'exp': 'river bank 河岸。'},
    {'q': 'The hotel has a big swimming {0}. （游泳池）', 'blanks': [['pool']], 'exp': 'swimming pool 游泳池。'},
    {'q': 'There are many beautiful {0} in Kenting. （海灘，複數）', 'blanks': [['beaches']], 'exp': 'beach → beaches（-ch 加 -es）。'},
    {'q': 'Ships sail on the {0}. （海）', 'blanks': [['sea']], 'exp': 'on the sea 在海上。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'A ______ is smaller than a mountain.', 'opts': ['hill', 'sea', 'river', 'lake'], 'answer': 0, 'exp': 'hill 比 mountain 小。'},
    {'type': 'mc', 'q': 'A ______ is smaller than a lake.', 'opts': ['sea', 'pond', 'river', 'island'], 'answer': 1, 'exp': 'pond 比 lake 小。'},
    {'type': 'mc', 'q': 'There is an old temple ______ the top of the hill.', 'opts': ['in', 'at', 'on', 'by'], 'answer': 2, 'exp': 'on the top of the hill 在山頂上。'},
    {'type': 'mc', 'q': 'My grandparents live ______ the sea.', 'opts': ['by', 'in', 'under', 'into'], 'answer': 0, 'exp': 'by the sea 在海邊。'},
    {'type': 'mc', 'q': 'Mt. Jade is the highest ______ in Taiwan.', 'opts': ['island', 'river', 'mountain', 'beach'], 'answer': 2, 'exp': 'Mt. = mountain，玉山是最高的山。'},
    {'type': 'mc', 'q': 'Taiwan is an ______. There is sea all around it.', 'opts': ['area', 'island', 'hill', 'pond'], 'answer': 1, 'exp': '四面環海 → island。'},
  ]},
]
