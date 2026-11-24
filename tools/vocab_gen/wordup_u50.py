# WORD UP 複習區 Unit 50（WORD UP「T-IV」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 50, 'en': 'T-IV', 'zh': 'T 開頭（四）',
  'intro': 'WORD UP「T-IV」的 34 個字（T-shirt 到 typhoon）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('T-shirt', 'n.', 'T 恤', '', 'I bought a white T-shirt.', '我買了一件白 T 恤。', '👕'),
    W('trap', 'n./v.', '陷阱；困住', '過去式 trapped', 'The mouse was caught in a trap.', '老鼠被捕鼠器抓到了。', '🪤'),
    W('trash', 'n.', '垃圾', '不可數；trash can 垃圾桶', 'Put the trash in the trash can.', '把垃圾丟進垃圾桶。', '🗑️'),
    W('travel', 'v./n.', '旅行', 'travel to + 地點', 'I want to travel around the world.', '我想環遊世界。', '🧳'),
    W('treasure', 'n.', '寶藏', '', 'The pirates found the treasure.', '海盜找到了寶藏。', '💰'),
    W('treat', 'v./n.', '對待；請客', 'It\'s my treat. 我請客', 'Don\'t treat me like a child.', '不要把我當小孩子。', '🍦'),
    W('treatment', 'n.', '治療；對待', '', 'He is getting treatment at the hospital.', '他正在醫院接受治療。', '🏥'),
    W('tree', 'n.', '樹', '', 'There is a big tree in the yard.', '院子裡有一棵大樹。', '🌳'),
    W('trial', 'n.', '試用；審判', '', 'You can use the app for a free trial.', '你可以免費試用這個應用程式。', '⚖️'),
    W('triangle', 'n.', '三角形', '', 'A triangle has three sides.', '三角形有三個邊。', '🔺'),
    W('trick', 'n.', '把戲；詭計', 'Trick or treat! 不給糖就搗蛋', 'My dog can do tricks.', '我的狗會表演把戲。', '🃏'),
    W('trip', 'n.', '旅行', 'take a trip', 'We took a trip to Kenting.', '我們去墾丁旅行。', '🚗'),
    W('trouble', 'n.', '麻煩；困難', 'be in trouble 有麻煩', 'You\'ll be in trouble if you\'re late.', '你遲到就麻煩了。', '😰'),
    W('trousers', 'n.', '長褲', '一定用複數', 'These trousers are too long.', '這條長褲太長了。', '👖'),
    W('truck', 'n.', '卡車', '', 'A big truck is on the road.', '路上有一輛大卡車。', '🚚'),
    W('true', 'adj.', '真的；真實的', 'come true 實現', 'I hope your dream comes true.', '希望你的夢想成真。', '✅'),
    W('trumpet', 'n.', '小喇叭', 'play the trumpet', 'He plays the trumpet in the band.', '他在樂隊吹小喇叭。', '🎺'),
    W('trust', 'v./n.', '信任', '', 'I trust you.', '我信任你。', '🤝'),
    W('truth', 'n.', '真相；事實', 'tell the truth 說實話', 'Please tell me the truth.', '請告訴我實話。', '🔍'),
    W('try', 'v./n.', '嘗試；試', 'try to V 努力；try + V-ing 試試看', 'Try this cake. It\'s great.', '試試這個蛋糕，很好吃。', '🧪'),
    W('tub', 'n.', '浴缸；桶', '', 'The baby is in the tub.', '寶寶在浴缸裡。', '🛁'),
    W('Tuesday', 'n.', '星期二', '', 'I have piano class on Tuesday.', '我星期二有鋼琴課。', '🗓️'),
    W('tummy', 'n.', '肚子（口語）', '= stomach', 'My tummy hurts.', '我肚子痛。', '🫃'),
    W('tunnel', 'n.', '隧道', '', 'The train went into a tunnel.', '火車開進隧道。', '🚇'),
    W('turkey', 'n.', '火雞', 'Turkey 大寫是土耳其', 'We eat turkey on Thanksgiving.', '我們感恩節吃火雞。', '🦃'),
    W('turn', 'v./n.', '轉；輪流', 'It\'s your turn. 輪到你了', 'It\'s your turn.', '輪到你了。', '🔄'),
    W('turtle', 'n.', '烏龜', '', 'The turtle walks slowly.', '烏龜走得很慢。', '🐢'),
    W('TV', 'n.', '電視', 'watch TV', 'Don\'t watch TV too long.', '電視不要看太久。', '📺'),
    W('twelve', 'n.', '十二', 'twelfth 第十二', 'There are twelve months in a year.', '一年有十二個月。', '🕛'),
    W('twenty', 'n.', '二十', 'twentieth 第二十', 'I have twenty dollars.', '我有二十元。', '💵'),
    W('twice', 'adv.', '兩次；兩倍', 'twice a week 一週兩次', 'I go swimming twice a week.', '我一週游泳兩次。', '✌️'),
    W('two', 'n.', '二', '', 'I have two cats.', '我有兩隻貓。', '2️⃣'),
    W('type', 'n./v.', '類型；打字', '', 'What type of music do you like?', '你喜歡哪種類型的音樂？', '⌨️'),
    W('typhoon', 'n.', '颱風', '', 'School is closed because of the typhoon.', '因為颱風停課了。', '🌀'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('try to V / try + V-ing', '努力做 ／ 試試看做', 'try to win ／ try eating it'),
      ('tell the truth', '說實話', 'Always tell the truth.'),
      ('come true', '實現', 'My wish came true.'),
      ('be in trouble', '有麻煩', 'He is in trouble.'),
      ('It\'s my treat.', '我請客', 'Lunch is my treat.'),
      ('It\'s your turn.', '輪到你', 'Now it\'s your turn.'),
      ('once / twice / three times', '一次 ／ 兩次 ／ 三次', 'twice a day'),
    ], 'note': 'trousers、jeans、pants 一定用複數；trash 不可數。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '寶藏', 'opts': ['treatment', 'treasure', 'trouble', 'trial'], 'answer': 1, 'exp': 'treasure 寶藏。'},
    {'type': 'mc', 'q': '隧道', 'opts': ['tunnel', 'turtle', 'turkey', 'trumpet'], 'answer': 0, 'exp': 'tunnel 隧道。'},
    {'type': 'mc', 'q': '信任', 'opts': ['trick', 'treat', 'trust', 'trap'], 'answer': 2, 'exp': 'trust 信任。'},
    {'type': 'mc', 'q': '颱風', 'opts': ['triangle', 'trousers', 'type', 'typhoon'], 'answer': 3, 'exp': 'typhoon 颱風。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '三角形（t＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['triangle']], 'exp': 'triangle。'},
    {'q': '星期二（T＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['Tuesday', 'tuesday']], 'exp': 'Tuesday。'},
    {'q': '烏龜（t＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['turtle']], 'exp': 'turtle。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please tell me the {0}. Did you break it? （真相）', 'blanks': [['truth']], 'exp': 'tell the truth 說實話。'},
    {'q': 'I hope all your dreams come {0}. （真的）', 'blanks': [['true']], 'exp': 'come true 實現。'},
    {'q': 'I brush my teeth {0} a day. （兩次）', 'blanks': [['twice']], 'exp': 'twice a day 一天兩次。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'I tried ______ the box, but it was too heavy.', 'opts': ['lift', 'to lift', 'lifted', 'lifts'], 'answer': 1, 'exp': 'try to V 努力去做。'},
    {'type': 'mc', 'q': 'Put away your phone, or you\'ll be in ______ .', 'opts': ['treat', 'truth', 'trouble', 'trust'], 'answer': 2, 'exp': 'be in trouble 有麻煩。'},
    {'type': 'mc', 'q': 'My new trousers ______ black.', 'opts': ['are', 'is', 'was', 'be'], 'answer': 0, 'exp': 'trousers 是複數，用 are。'},
    {'type': 'mc', 'q': 'It\'s your ______ to clean the classroom.', 'opts': ['trip', 'type', 'trick', 'turn'], 'answer': 3, 'exp': 'It\'s your turn. 輪到你了。'},
  ]},
]
