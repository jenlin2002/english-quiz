# WORD UP 複習區 Unit 7（WORD UP「B-IV」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 7, 'en': 'B-IV', 'zh': 'B 開頭（四）',
  'intro': 'WORD UP「B-IV」的 33 個字（bread 到 buy）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('bread', 'n.', '麵包', '不可數；a piece／loaf of bread', 'I had bread and milk for breakfast.', '我早餐吃麵包配牛奶。', '🍞'),
    W('break', 'v./n.', '打破；休息', '三態 break-broke-broken；take a break', 'Let\'s take a short break.', '我們休息一下吧。', '💔'),
    W('breakfast', 'n.', '早餐', 'have breakfast', 'Don\'t skip breakfast.', '不要不吃早餐。', '🍳'),
    W('brick', 'n.', '磚塊', '', 'The old house is made of red bricks.', '那棟老房子是紅磚蓋的。', '🧱'),
    W('bridge', 'n.', '橋', '', 'We walked across the bridge.', '我們走過那座橋。', '🌉'),
    W('brief', 'adj.', '簡短的', 'in brief 簡單地說', 'He gave a brief speech.', '他做了簡短的演講。', '📝'),
    W('bright', 'adj.', '明亮的；聰明的', '', 'The room is bright and clean.', '這個房間明亮又乾淨。', '💡'),
    W('bring', 'v.', '帶來', '三態 bring-brought-brought', 'Bring your umbrella. It may rain.', '帶雨傘，可能會下雨。', '🎒'),
    W('Britain', 'n.', '英國', '= the UK', 'London is the capital of Britain.', '倫敦是英國的首都。', '🇬🇧'),
    W('British', 'adj./n.', '英國的；英國人', '', 'She has a British accent.', '她有英國口音。', '💂'),
    W('broad', 'adj.', '寬的；廣的', '= wide；名詞 breadth', 'The river is broad and deep.', '這條河又寬又深。', '↔️'),
    W('broadcast', 'v./n.', '廣播；播放', '', 'The game will be broadcast live.', '這場比賽會現場轉播。', '📡'),
    W('brother', 'n.', '兄弟', 'older brother 哥哥', 'My older brother is in senior high.', '我哥哥讀高中。', '👦'),
    W('brown', 'adj./n.', '棕色的', '', 'She has long brown hair.', '她有一頭棕色長髮。', '🟫'),
    W('brunch', 'n.', '早午餐', 'breakfast + lunch', 'We have brunch on Sundays.', '我們星期天吃早午餐。', '🥞'),
    W('brush', 'n./v.', '刷子；刷', 'brush your teeth 刷牙', 'Brush your teeth before bed.', '睡前要刷牙。', '🪥'),
    W('bucket', 'n.', '水桶', '', 'He filled the bucket with water.', '他把水桶裝滿水。', '🪣'),
    W('buffet', 'n.', '自助餐', '', 'The hotel has a big breakfast buffet.', '飯店有豐盛的早餐自助餐。', '🍽️'),
    W('bug', 'n.', '小蟲；（程式）錯誤', '', 'There is a bug on your shirt.', '你的襯衫上有一隻小蟲。', '🐛'),
    W('build', 'v.', '建造', '三態 build-built-built', 'They are building a new school.', '他們正在蓋一所新學校。', '🏗️'),
    W('building', 'n.', '建築物；大樓', '', 'Taipei 101 is a very tall building.', '台北 101 是一棟很高的大樓。', '🏙️'),
    W('bun', 'n.', '小圓麵包；包子', 'steamed bun 包子', 'I ate a meat bun for breakfast.', '我早餐吃了一個肉包。', '🥟'),
    W('bundle', 'n.', '一捆；一束', 'a bundle of + 名詞', 'He carried a bundle of newspapers.', '他搬了一捆報紙。', '📦'),
    W('burn', 'v.', '燃燒；燒傷', '', 'Be careful. Don\'t burn your hand.', '小心，別燙到手。', '🔥'),
    W('burst', 'v.', '爆裂；突然…', '三態都是 burst；burst into tears 突然大哭', 'The balloon burst with a loud bang.', '氣球砰一聲爆了。', '💥'),
    W('bus', 'n.', '公車', 'by bus 搭公車', 'I go to school by bus.', '我搭公車上學。', '🚌'),
    W('business', 'n.', '生意；事業', 'on business 出差', 'Dad is in Japan on business.', '爸爸去日本出差。', '💼'),
    W('businessman', 'n.', '商人', '複數 businessmen', 'My uncle is a businessman.', '我叔叔是生意人。', '🧑‍💼'),
    W('busy', 'adj.', '忙碌的', 'be busy + V-ing', 'Mom is busy cooking dinner.', '媽媽正忙著煮晚餐。', '⏰'),
    W('butter', 'n.', '奶油', '不可數', 'Put some butter on the bread.', '在麵包上抹點奶油。', '🧈'),
    W('butterfly', 'n.', '蝴蝶', '複數 butterflies', 'A butterfly landed on the flower.', '一隻蝴蝶停在花上。', '🦋'),
    W('button', 'n.', '按鈕；鈕扣', 'press the button 按按鈕', 'Press the red button to start.', '按紅色按鈕開始。', '🔘'),
    W('buy', 'v.', '買', '三態 buy-bought-bought', 'I bought a new bag yesterday.', '我昨天買了一個新包包。', '🛍️'),
  ],
  'focus': [
    {'title': '不規則動詞三態', 'head': ('原形', '過去式', '過去分詞'), 'rows': [
      ('break', 'broke', 'broken'),
      ('bring', 'brought', 'brought'),
      ('build', 'built', 'built'),
      ('buy', 'bought', 'bought'),
      ('burst', 'burst', 'burst'),
      ('broadcast', 'broadcast', 'broadcast'),
    ], 'note': 'bring 帶來、buy 買：過去式都是 -ought 結尾，拼法不同（brought／bought）。'},
    {'title': '常考片語', 'head': ('說法', '中文', '例子'), 'rows': [
      ('take a break', '休息一下', 'take a ten-minute break'),
      ('brush one\'s teeth', '刷牙', 'brush my teeth'),
      ('be busy + V-ing / be busy with + N', '忙著做…', 'busy doing homework ／ busy with work'),
      ('on business', '出差', 'go to Tokyo on business'),
      ('burst into tears', '突然大哭', 'She burst into tears.'),
      ('by bus', '搭公車（不加 a／the）', 'go to school by bus'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '橋', 'opts': ['brick', 'bridge', 'brief', 'bright'], 'answer': 1, 'exp': 'bridge 橋。'},
    {'type': 'mc', 'q': '早午餐', 'opts': ['breakfast', 'buffet', 'brunch', 'bun'], 'answer': 2, 'exp': 'brunch 早午餐。'},
    {'type': 'mc', 'q': '水桶', 'opts': ['bucket', 'bundle', 'button', 'butter'], 'answer': 0, 'exp': 'bucket 水桶。'},
    {'type': 'mc', 'q': '廣播；播放', 'opts': ['broad', 'British', 'business', 'broadcast'], 'answer': 3, 'exp': 'broadcast 廣播。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '蝴蝶（b＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['butterfly']], 'exp': 'butterfly。'},
    {'q': '建築物（b＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['building']], 'exp': 'building。'},
    {'q': '明亮的（b＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['bright']], 'exp': 'bright。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Jack {0} his leg last week. （打斷，過去式）', 'blanks': [['broke']], 'exp': 'break 的過去式 broke。'},
    {'q': 'Did you {0} your homework today? （帶來）', 'blanks': [['bring']], 'exp': 'Did + 原形：bring。'},
    {'q': 'Mom {0} me a new jacket last Sunday. （買，過去式）', 'blanks': [['bought']], 'exp': 'buy 的過去式 bought。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'My sister is busy ______ for the test.', 'opts': ['study', 'to study', 'studying', 'studied'], 'answer': 2, 'exp': 'be busy + V-ing。'},
    {'type': 'mc', 'q': 'Dad often goes to Shanghai ______ business.', 'opts': ['on', 'in', 'at', 'for'], 'answer': 0, 'exp': 'on business 出差。'},
    {'type': 'mc', 'q': 'You look tired. Why not take a ______ ?', 'opts': ['bridge', 'brick', 'brush', 'break'], 'answer': 3, 'exp': 'take a break 休息一下。'},
    {'type': 'mc', 'q': 'The workers ______ this bridge ten years ago.', 'opts': ['build', 'built', 'builds', 'building'], 'answer': 1, 'exp': 'ten years ago 用過去式 built。'},
  ]},
]
