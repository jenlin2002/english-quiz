# WORD UP 複習區 Unit 40（WORD UP「R-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 40, 'en': 'R-II', 'zh': 'R 開頭（二）',
  'intro': 'WORD UP「R-II」的 31 個字（rice 到 Russian）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('rice', 'n.', '米；飯', '不可數；a bowl of rice', 'I eat a bowl of rice for lunch.', '我午餐吃一碗飯。', '🍚'),
    W('rich', 'adj.', '富有的；豐富的', 'be rich in 富含', 'Oranges are rich in vitamin C.', '柳橙富含維他命 C。', '💰'),
    W('ride', 'v./n.', '騎；搭乘', '三態 ride-rode-ridden', 'I ride my bike to school.', '我騎腳踏車上學。', '🚴'),
    W('right', 'adj./n./adv.', '對的；右邊；權利', 'turn right 右轉；right now 馬上', 'Turn right at the bank.', '在銀行那裡右轉。', '➡️'),
    W('ring', 'n./v.', '戒指；（鈴）響', '三態 ring-rang-rung', 'The phone is ringing.', '電話在響。', '💍'),
    W('rise', 'v.', '上升；升起', '三態 rise-rose-risen', 'The sun rises in the east.', '太陽從東方升起。', '🌅'),
    W('river', 'n.', '河', '', 'We went fishing by the river.', '我們去河邊釣魚。', '🏞️'),
    W('road', 'n.', '道路', '', 'Be careful when you cross the road.', '過馬路要小心。', '🛣️'),
    W('rob', 'v.', '搶劫', 'rob + 人／地方 + of + 物；過去式 robbed', 'Two men robbed the bank.', '兩個男人搶了銀行。', '🦹'),
    W('robot', 'n.', '機器人', '', 'This robot can clean the floor.', '這個機器人會掃地。', '🤖'),
    W('rock', 'n.', '岩石；搖滾樂', '', 'He sat on a big rock.', '他坐在一塊大石頭上。', '🪨'),
    W('role', 'n.', '角色', 'play a role 扮演角色', 'She played the role of the queen.', '她演皇后的角色。', '🎭'),
    W('roll', 'v./n.', '滾動；捲', '', 'The ball rolled down the hill.', '球滾下山坡。', '🎳'),
    W('roof', 'n.', '屋頂', '複數 roofs', 'There is a cat on the roof.', '屋頂上有一隻貓。', '🏠'),
    W('room', 'n.', '房間；空間', 'room 當空間不可數', 'Is there room for one more person?', '還有空間給多一個人嗎？', '🚪'),
    W('root', 'n.', '根', '', 'The tree has deep roots.', '這棵樹的根很深。', '🌱'),
    W('rope', 'n.', '繩子', 'jump rope 跳繩', 'Let\'s jump rope.', '我們來跳繩吧。', '🪢'),
    W('rose', 'n.', '玫瑰', '', 'He gave her a red rose.', '他送她一朵紅玫瑰。', '🌹'),
    W('round', 'adj./prep.', '圓的；環繞', 'all year round 一整年', 'The earth is round.', '地球是圓的。', '⚪'),
    W('row', 'n./v.', '一排；划船', 'in a row 連續', 'We sat in the front row.', '我們坐在第一排。', '🚣'),
    W('royal', 'adj.', '皇家的', '', 'They live in a royal palace.', '他們住在皇宮裡。', '👑'),
    W('rub', 'v.', '摩擦；揉', '過去式 rubbed', 'Don\'t rub your eyes.', '不要揉眼睛。', '👐'),
    W('rubber', 'n.', '橡膠；橡皮擦', '', 'The ball is made of rubber.', '這顆球是橡膠做的。', '🧽'),
    W('rude', 'adj.', '無禮的', 'be rude to + 人', 'Don\'t be rude to your parents.', '不要對父母沒禮貌。', '😤'),
    W('ruin', 'v./n.', '毀壞；廢墟', '', 'The rain ruined our picnic.', '雨毀了我們的野餐。', '🏚️'),
    W('rule', 'n.', '規則', 'follow the rules 遵守規則', 'Follow the school rules.', '遵守校規。', '📜'),
    W('ruler', 'n.', '尺；統治者', '', 'Draw a line with a ruler.', '用尺畫一條線。', '📏'),
    W('run', 'v.', '跑；經營', '三態 run-ran-run', 'I ran to school this morning.', '我今天早上跑去學校。', '🏃'),
    W('rush', 'v./n.', '衝；匆忙', 'rush hour 尖峰時間', 'The MRT is crowded during rush hour.', '尖峰時間捷運很擠。', '🏃‍♀️'),
    W('Russia', 'n.', '俄羅斯', '', 'Russia is a very big country.', '俄羅斯是個很大的國家。', '🇷🇺'),
    W('Russian', 'adj./n.', '俄羅斯的；俄國人；俄文', '', 'He is learning Russian.', '他在學俄文。', '🪆'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('rise / raise', '升起（自己）／ 舉起（東西）', 'The sun rises. ／ Raise your hand.'),
      ('be rich in', '富含…', 'rich in protein'),
      ('play a role', '扮演角色', 'play an important role'),
      ('be rude to + 人', '對某人無禮', 'rude to the waiter'),
      ('rush hour', '尖峰時間', 'during rush hour'),
      ('rule / ruler', '規則 ／ 尺、統治者', 'break the rules ／ a ruler'),
      ('in a row', '連續', 'three days in a row'),
    ], 'note': 'ride-rode-ridden、ring-rang-rung、rise-rose-risen、run-ran-run。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '皇家的', 'opts': ['round', 'royal', 'rude', 'rich'], 'answer': 1, 'exp': 'royal 皇家的。'},
    {'type': 'mc', 'q': '搶劫', 'opts': ['rob', 'rub', 'roll', 'rush'], 'answer': 0, 'exp': 'rob 搶劫。'},
    {'type': 'mc', 'q': '毀壞', 'opts': ['root', 'rope', 'ruin', 'rule'], 'answer': 2, 'exp': 'ruin 毀壞。'},
    {'type': 'mc', 'q': '橡膠', 'opts': ['ruler', 'robot', 'river', 'rubber'], 'answer': 3, 'exp': 'rubber 橡膠。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '機器人（r＿＿＿＿，5 個字母）：{0}', 'blanks': [['robot']], 'exp': 'robot。'},
    {'q': '屋頂（r＿＿＿，4 個字母）：{0}', 'blanks': [['roof']], 'exp': 'roof。'},
    {'q': '無禮的（r＿＿＿，4 個字母）：{0}', 'blanks': [['rude']], 'exp': 'rude。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The sun {0} at 5:30 this morning. （升起，過去式）', 'blanks': [['rose']], 'exp': 'rise 的過去式 rose。'},
    {'q': 'I {0} a horse on the farm last summer. （騎，過去式）', 'blanks': [['rode']], 'exp': 'ride 的過去式 rode。'},
    {'q': 'Milk is {0} in calcium. （富含）', 'blanks': [['rich']], 'exp': 'be rich in 富含。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'The price of eggs ______ again last week.', 'opts': ['raised', 'rose', 'rise', 'risen'], 'answer': 1, 'exp': '價格自己上升用 rise，過去式 rose。'},
    {'type': 'mc', 'q': 'It\'s rude ______ talk with food in your mouth.', 'opts': ['for', 'of', 'to', 'at'], 'answer': 2, 'exp': 'It\'s rude to V。'},
    {'type': 'mc', 'q': 'Parents play an important ______ in a child\'s life.', 'opts': ['role', 'roll', 'rule', 'row'], 'answer': 0, 'exp': 'play a role 扮演角色。'},
    {'type': 'mc', 'q': 'Don\'t take the bus during rush ______ .', 'opts': ['time', 'day', 'road', 'hour'], 'answer': 3, 'exp': 'rush hour 尖峰時間。'},
  ]},
]
