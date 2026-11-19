# 主題 2000 字 Unit 22：Holidays & festivals 節日與慶典（字表依課本單元；詞性、中文、例句、題目為本站自編）
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 22, 'en': 'Holidays & festivals', 'zh': '節日與慶典',
  'intro': '西洋節日（Christmas、Easter、Halloween）、節日與假期的說法，共 7 個字。節日名稱第一個字母要大寫；放假去玩用 on vacation。',
  'words': [
    W('Christmas', 'n.', '聖誕節', '不可數；Christmas Eve 聖誕夜；Merry Christmas! 聖誕快樂', 'We put up a Christmas tree in the living room.', '我們在客廳擺了一棵聖誕樹。', '🎄'),
    W('Easter', 'n.', '復活節', '不可數；Easter egg 彩蛋', 'Kids look for colorful eggs at Easter.', '復活節時孩子們會找彩色的蛋。', '🐣'),
    W('Halloween', 'n.', '萬聖節前夕；萬聖夜', '10 月 31 日；trick or treat 不給糖就搗蛋', 'The kids dressed up as ghosts on Halloween.', '萬聖夜孩子們打扮成鬼。', '🎃'),
    W('festival', 'n.', '節日；慶典', 'the Moon Festival 中秋節', 'We eat mooncakes at the Moon Festival.', '中秋節我們吃月餅。', '🏮'),
    W('holiday', 'n.', '假日；節日', '複數 holidays；national holiday 國定假日', 'There is no school today because it\'s a holiday.', '今天是假日，所以不用上學。', '🎉'),
    W('vacation', 'n.', '假期', 'summer vacation 暑假；on vacation 度假中', 'My family went to Japan during the summer vacation.', '暑假我們全家去了日本。', '🏖️'),
    W('celebrate', 'v.', '慶祝', 'celebrating／celebrated', 'We celebrated Grandpa\'s birthday at a restaurant.', '我們在餐廳慶祝爺爺的生日。', '🥳'),
  ],
  'focus': [
    {'title': '常見的節日', 'head': ('節日', '中文', '日期'), 'rows': [
      ('Chinese New Year', '春節', '農曆 1 月 1 日'),
      ('Lantern Festival', '元宵節', '農曆 1 月 15 日'),
      ('Dragon Boat Festival', '端午節', '農曆 5 月 5 日'),
      ('Moon Festival', '中秋節', '農曆 8 月 15 日'),
      ('Easter', '復活節', '每年 3、4 月的星期日'),
      ('Halloween', '萬聖夜', '10 月 31 日'),
      ('Christmas', '聖誕節', '12 月 25 日'),
    ], 'note': '節日名稱每個字的第一個字母都要大寫。在某個節日用 on（on Christmas Day）或 at（at Christmas、at Easter）。'},
    {'title': 'holiday、vacation、festival 怎麼分', 'head': ('字', '意思', '例子'), 'rows': [
      ('holiday', '不用上班上課的一天；節日', 'Monday is a holiday.'),
      ('vacation', '一段比較長的假期（美式）', 'summer vacation, winter vacation'),
      ('festival', '有特別活動的節日、慶典', 'the Moon Festival, a music festival'),
      ('on vacation／on holiday', '在度假', 'They are on vacation in Hualien.'),
    ], 'note': '英式英文常用 holiday 表示長假：go on holiday＝go on vacation。'},
    {'title': 'celebrate 的變化與用法', 'head': ('用法', '例句', '中文'), 'rows': [
      ('celebrate + 節日', 'We celebrate Christmas with a big dinner.', '我們用一頓大餐慶祝聖誕節。'),
      ('celebrate + 事情', 'Let\'s celebrate your good grades!', '來慶祝你考得好！'),
      ('過去式', 'They celebrated their wedding anniversary.', '他們慶祝了結婚週年。'),
      ('V-ing', 'People are celebrating in the street.', '人們正在街上慶祝。'),
    ], 'note': 'celebrate 字尾是 e：加 -ing 去 e（celebrating），加 -ed 只加 d（celebrated）。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '萬聖節前夕', 'opts': ['Easter', 'Halloween', 'Christmas', 'holiday'], 'answer': 1, 'exp': 'Halloween 萬聖夜（10 月 31 日）。'},
    {'type': 'mc', 'q': '慶祝', 'opts': ['celebrate', 'collect', 'complete', 'continue'], 'answer': 0, 'exp': 'celebrate 慶祝。'},
    {'type': 'mc', 'q': '假期', 'opts': ['festival', 'Easter', 'vacation', 'village'], 'answer': 2, 'exp': 'vacation 假期。'},
    {'type': 'mc', 'q': '復活節', 'opts': ['Christmas', 'Halloween', 'festival', 'Easter'], 'answer': 3, 'exp': 'Easter 復活節。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'festival', 'opts': ['節日；慶典', '假期', '生日', '派對'], 'answer': 0, 'exp': 'festival 節日、慶典。'},
    {'type': 'mc', 'q': 'Christmas', 'opts': ['新年', '聖誕節', '復活節', '感恩節'], 'answer': 1, 'exp': 'Christmas 聖誕節（12 月 25 日）。'},
    {'type': 'mc', 'q': 'holiday', 'opts': ['旅館', '房子', '假日；節日', '嗜好'], 'answer': 2, 'exp': 'holiday 假日、節日；hotel 旅館、hobby 嗜好。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數；節日名稱第一個字母要大寫。', 'items': [
    {'q': '假期（v＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['vacation']], 'exp': 'vacation。'},
    {'q': '慶祝（c＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['celebrate']], 'exp': 'celebrate，cel-e-brate。'},
    {'q': '聖誕節（C＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['Christmas']], 'exp': 'Christmas，C 大寫，t 不發音。'},
    {'q': '節日（f＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['festival']], 'exp': 'festival。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Kids say "Trick or treat!" on {0}. （萬聖夜）', 'blanks': [['Halloween']], 'exp': '不給糖就搗蛋 → Halloween。'},
    {'q': 'We had a big party to {0} the New Year. （慶祝）', 'blanks': [['celebrate']], 'exp': 'to + 原形動詞 → celebrate。'},
    {'q': 'Last year we {0} Christmas at Grandma\'s house. （慶祝，過去式）', 'blanks': [['celebrated']], 'exp': 'celebrate 字尾 e，只加 d → celebrated。'},
    {'q': 'The Dragon Boat {0} is in summer. （節日）', 'blanks': [['Festival', 'festival']], 'exp': 'the Dragon Boat Festival 端午節。'},
    {'q': 'Mr. Lin isn\'t in the office. He is on {0} in Japan. （假期）', 'blanks': [['vacation', 'holiday']], 'exp': 'on vacation 度假中（英式也說 on holiday）。'},
    {'q': 'holiday → (複數) {0}', 'blanks': [['holidays']], 'exp': '母音 + y 直接加 -s → holidays。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Christmas is ______ December 25.', 'opts': ['in', 'on', 'at', 'for'], 'answer': 1, 'exp': '特定日期用 on：on December 25。'},
    {'type': 'mc', 'q': 'Children look for colorful eggs at ______.', 'opts': ['Halloween', 'Easter', 'the Moon Festival', 'Christmas Eve'], 'answer': 1, 'exp': '找彩蛋 → Easter 復活節。'},
    {'type': 'mc', 'q': 'People eat mooncakes at the ______ Festival.', 'opts': ['Dragon Boat', 'Lantern', 'Moon', 'Easter'], 'answer': 2, 'exp': '吃月餅 → the Moon Festival 中秋節。'},
    {'type': 'mc', 'q': 'The students are ______ their teacher\'s birthday now.', 'opts': ['celebrate', 'celebrated', 'celebrates', 'celebrating'], 'answer': 3, 'exp': 'are + V-ing（現在進行式）→ celebrating。'},
    {'type': 'mc', 'q': 'Summer ______ starts in July, and we can stay home for two months.', 'opts': ['vacation', 'festival', 'Christmas', 'party'], 'answer': 0, 'exp': 'summer vacation 暑假。'},
  ]},
]
