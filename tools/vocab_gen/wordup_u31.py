# WORD UP 複習區 Unit 31（WORD UP「M-III」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 31, 'en': 'M-III', 'zh': 'M 開頭（三）',
  'intro': 'WORD UP「M-III」的 37 個字（missing 到 must）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('missing', 'adj.', '失蹤的；遺失的', '', 'My cat has been missing for two days.', '我的貓失蹤兩天了。', '🔍'),
    W('mistake', 'n.', '錯誤', 'make a mistake 犯錯', 'Everyone makes mistakes.', '每個人都會犯錯。', '❌'),
    W('mix', 'v.', '混合', 'mix A with B', 'Mix the flour with milk.', '把麵粉和牛奶混在一起。', '🥣'),
    W('model', 'n.', '模型；模特兒；榜樣', 'role model 榜樣', 'My brother likes building model cars.', '我哥哥喜歡組裝模型車。', '🚂'),
    W('modern', 'adj.', '現代的', '', 'Taipei is a modern city.', '台北是現代化的城市。', '🏙️'),
    W('moment', 'n.', '片刻；時刻', 'at the moment 此刻', 'Wait a moment, please.', '請稍等一下。', '⏳'),
    W('Monday', 'n.', '星期一', '', 'I have English class on Monday.', '我星期一有英文課。', '📅'),
    W('money', 'n.', '錢', '不可數；How much money…?', 'I saved a lot of money.', '我存了很多錢。', '💵'),
    W('monkey', 'n.', '猴子', '', 'The monkey is eating a banana.', '猴子在吃香蕉。', '🐒'),
    W('monster', 'n.', '怪物', '', 'The little boy is afraid of monsters.', '那個小男孩怕怪物。', '👾'),
    W('month', 'n.', '月', 'th 唸 /θ/', 'There are twelve months in a year.', '一年有十二個月。', '🗓️'),
    W('monthly', 'adj./adv.', '每月的', '', 'We have a monthly test.', '我們每個月有月考。', '📆'),
    W('moon', 'n.', '月亮', 'the moon', 'The moon is bright tonight.', '今晚月亮很亮。', '🌕'),
    W('mop', 'n./v.', '拖把；拖地', '過去式 mopped', 'Please mop the floor.', '請拖地。', '🧹'),
    W('more', 'adj./adv.', '更多', 'many／much 的比較級', 'Can I have more rice?', '我可以再多要一點飯嗎？', '➕'),
    W('morning', 'n.', '早上', 'in the morning', 'Good morning!', '早安！', '🌅'),
    W('mosquito', 'n.', '蚊子', '複數 mosquitoes', 'A mosquito bit me.', '我被蚊子咬了。', '🦟'),
    W('most', 'adj./adv.', '最多；大部分', 'most of + 名詞', 'Most of my friends like sports.', '我大部分的朋友都喜歡運動。', '🔝'),
    W('mother', 'n.', '母親', '= mom', 'My mother is a nurse.', '我媽媽是護理師。', '👩'),
    W('Mother\'s Day', 'n.', '母親節', '五月第二個星期日', 'I made a card for Mother\'s Day.', '我為母親節做了一張卡片。', '💐'),
    W('motion', 'n.', '動作；移動', 'in slow motion 慢動作', 'Watch the video in slow motion.', '用慢動作看這段影片。', '🎬'),
    W('motorcycle', 'n.', '機車；摩托車', 'ride a motorcycle', 'There are many motorcycles in Taiwan.', '台灣有很多機車。', '🏍️'),
    W('mountain', 'n.', '山', 'climb a mountain 爬山', 'Yushan is the highest mountain in Taiwan.', '玉山是台灣最高的山。', '🏔️'),
    W('mouse', 'n.', '老鼠；滑鼠', '複數 mice', 'The cat is chasing a mouse.', '貓在追老鼠。', '🐭'),
    W('mouth', 'n.', '嘴巴', '', 'Open your mouth and say "Ah."', '張開嘴巴說「啊」。', '👄'),
    W('move', 'v.', '移動；搬家', 'move to + 地點 搬到…', 'We moved to Taichung last year.', '我們去年搬到台中。', '📦'),
    W('movement', 'n.', '動作；運動', '', 'The dancer\'s movements are beautiful.', '舞者的動作很優美。', '🩰'),
    W('movie', 'n.', '電影', 'go to the movies 去看電影', 'Let\'s go to the movies tonight.', '我們今晚去看電影吧。', '🎥'),
    W('Mr.', 'n.', '先生（稱呼）', 'Mister 的縮寫', 'Mr. Wang is our principal.', '王先生是我們的校長。', '👨‍💼'),
    W('Mrs.', 'n.', '太太（稱呼）', '已婚女性', 'Mrs. Chen lives next door.', '陳太太住在隔壁。', '👩‍🦰'),
    W('MRT', 'n.', '捷運', 'take the MRT', 'I take the MRT to school.', '我搭捷運上學。', '🚇'),
    W('Ms.', 'n.', '女士（稱呼）', '不分已婚未婚', 'Ms. Lee is our new teacher.', '李老師是我們的新老師。', '👩‍🏫'),
    W('much', 'adj./adv.', '許多；很', '接不可數名詞；How much…? 多少（錢）', 'How much is this T-shirt?', '這件 T 恤多少錢？', '💲'),
    W('mud', 'n.', '泥巴', 'muddy 泥濘的', 'The kids are playing in the mud.', '孩子們在玩泥巴。', '🟤'),
    W('museum', 'n.', '博物館', '', 'We visited the National Palace Museum.', '我們參觀了故宮博物院。', '🏛️'),
    W('music', 'n.', '音樂', '不可數', 'I listen to music every day.', '我每天聽音樂。', '🎵'),
    W('must', 'aux.', '必須；一定', 'must not 禁止', 'You must wear a helmet.', '你必須戴安全帽。', '❗'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('much / many', '接不可數 ／ 接可數', 'much money ／ many coins'),
      ('How much / How many', '多少（錢、不可數）／ 多少個', 'How much is it?'),
      ('make a mistake', '犯錯', 'make a big mistake'),
      ('most of + 名詞', '大部分的…', 'most of the students'),
      ('move to', '搬到…', 'move to Tainan'),
      ('must / must not', '必須 ／ 禁止', 'You must not run here.'),
      ('mouse → mice', '老鼠的複數', 'three mice'),
    ], 'note': 'Mr. 先生、Mrs. 太太、Ms. 女士、Miss 小姐。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '蚊子', 'opts': ['monkey', 'mosquito', 'monster', 'mouse'], 'answer': 1, 'exp': 'mosquito 蚊子。'},
    {'type': 'mc', 'q': '博物館', 'opts': ['museum', 'music', 'movie', 'mountain'], 'answer': 0, 'exp': 'museum 博物館。'},
    {'type': 'mc', 'q': '失蹤的', 'opts': ['modern', 'monthly', 'missing', 'motion'], 'answer': 2, 'exp': 'missing 失蹤的。'},
    {'type': 'mc', 'q': '混合', 'opts': ['move', 'mop', 'must', 'mix'], 'answer': 3, 'exp': 'mix 混合。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '機車（m＿＿＿＿＿＿＿＿＿，10 個字母）：{0}', 'blanks': [['motorcycle']], 'exp': 'motorcycle。'},
    {'q': '山（m＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['mountain']], 'exp': 'mountain。'},
    {'q': '錯誤（m＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['mistake']], 'exp': 'mistake。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'There are two {0} in the kitchen! （老鼠，複數）', 'blanks': [['mice']], 'exp': 'mouse 的複數 mice。'},
    {'q': 'You {0} not use your phone in class. （禁止）', 'blanks': [['must']], 'exp': 'must not 禁止。'},
    {'q': 'We {0} to a new apartment last month. （搬家，過去式）', 'blanks': [['moved']], 'exp': 'move 的過去式 moved。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'How ______ money do you have?', 'opts': ['many', 'much', 'more', 'most'], 'answer': 1, 'exp': 'money 不可數，用 How much。'},
    {'type': 'mc', 'q': '______ of the students passed the test.', 'opts': ['More', 'Much', 'Most', 'Many of'], 'answer': 2, 'exp': 'most of + 名詞 大部分的…。'},
    {'type': 'mc', 'q': 'Don\'t worry. Everyone ______ mistakes.', 'opts': ['makes', 'does', 'takes', 'has'], 'answer': 0, 'exp': 'make a mistake 犯錯。'},
    {'type': 'mc', 'q': 'I\'m busy at the ______ . Can I call you later?', 'opts': ['month', 'morning', 'motion', 'moment'], 'answer': 3, 'exp': 'at the moment 此刻。'},
  ]},
]
