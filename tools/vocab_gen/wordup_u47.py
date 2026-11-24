# WORD UP 複習區 Unit 47（WORD UP「T-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 47, 'en': 'T-I', 'zh': 'T 開頭（一）',
  'intro': 'WORD UP「T-I」的 35 個字（table 到 term）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('table', 'n.', '桌子；表格', '', 'Put the plates on the table.', '把盤子放在桌上。', '🪑'),
    W('Taichung', 'n.', '台中', '', 'Taichung is in central Taiwan.', '台中在台灣中部。', '🏙️'),
    W('tail', 'n.', '尾巴', '', 'The dog is wagging its tail.', '狗在搖尾巴。', '🐕'),
    W('Tainan', 'n.', '台南', '', 'Tainan is famous for its old temples.', '台南以古廟聞名。', '⛩️'),
    W('Taiwan', 'n.', '台灣', '', 'I was born in Taiwan.', '我在台灣出生。', '🇹🇼'),
    W('Taiwanese', 'adj./n.', '台灣的；台灣人；台語', '', 'Grandma speaks Taiwanese.', '奶奶說台語。', '🧋'),
    W('take', 'v.', '拿；搭乘；花（時間）', '三態 take-took-taken；It takes + 時間 + to V', 'It takes 20 minutes to walk to school.', '走路到學校要 20 分鐘。', '🤲'),
    W('talent', 'n.', '天分；才能', '', 'She has a talent for music.', '她很有音樂天分。', '🎹'),
    W('talk', 'v./n.', '說話；談話', 'talk to／with + 人；talk about', 'What are you talking about?', '你們在聊什麼？', '💬'),
    W('talkative', 'adj.', '愛說話的', '', 'My little sister is very talkative.', '我妹妹很愛說話。', '🗣️'),
    W('tall', 'adj.', '高的', '比較級 taller', 'He is taller than his father.', '他比他爸爸高。', '📏'),
    W('tangerine', 'n.', '橘子', '', 'We eat tangerines during Chinese New Year.', '過年我們吃橘子。', '🍊'),
    W('tank', 'n.', '水箱；坦克', 'fish tank 魚缸', 'There are fish in the tank.', '魚缸裡有魚。', '🐠'),
    W('tape', 'n.', '膠帶；錄音帶', '', 'Use tape to fix the paper.', '用膠帶黏住紙。', '📼'),
    W('target', 'n.', '目標；靶子', '', 'He hit the target.', '他打中了目標。', '🎯'),
    W('task', 'n.', '任務；工作', '', 'Cleaning the room is my daily task.', '打掃房間是我每天的任務。', '📋'),
    W('taste', 'v./n.', '嚐；味道', 'taste + 形容詞', 'This soup tastes good.', '這湯很好喝。', '👅'),
    W('taxi', 'n.', '計程車', 'take a taxi', 'Let\'s take a taxi.', '我們搭計程車吧。', '🚕'),
    W('tea', 'n.', '茶', '不可數；a cup of tea', 'Would you like a cup of tea?', '你要喝杯茶嗎？', '🍵'),
    W('teach', 'v.', '教', '三態 teach-taught-taught', 'Mr. Lin teaches us math.', '林老師教我們數學。', '👨‍🏫'),
    W('teacher', 'n.', '老師', '', 'My teacher is very kind.', '我的老師很親切。', '🧑‍🏫'),
    W('Teacher\'s Day', 'n.', '教師節', '9 月 28 日', 'We made cards for Teacher\'s Day.', '我們為教師節做了卡片。', '💐'),
    W('team', 'n.', '隊伍', '', 'Our team won the game.', '我們隊贏了比賽。', '👥'),
    W('teapot', 'n.', '茶壺', '', 'Grandpa makes tea in a teapot.', '爺爺用茶壺泡茶。', '🫖'),
    W('tear', 'n./v.', '眼淚；撕', '眼淚唸 /tɪr/，撕唸 /tɛr/；tear-tore-torn', 'Tears ran down her face.', '眼淚從她臉上流下。', '😢'),
    W('teenager', 'n.', '青少年', '13～19 歲', 'Many teenagers like K-pop.', '很多青少年喜歡韓流音樂。', '🧑'),
    W('telephone', 'n.', '電話', '= phone', 'The telephone is ringing.', '電話在響。', '☎️'),
    W('television', 'n.', '電視', '= TV', 'I watch television after dinner.', '我晚餐後看電視。', '📺'),
    W('tell', 'v.', '告訴；講', '三態 tell-told-told；tell + 人 + to V', 'Mom told me to clean my room.', '媽媽叫我打掃房間。', '🗨️'),
    W('temperature', 'n.', '溫度；體溫', '', 'The temperature is 30 degrees today.', '今天氣溫 30 度。', '🌡️'),
    W('temple', 'n.', '廟', '', 'We visited a temple in Tainan.', '我們參觀了台南的一座廟。', '🛕'),
    W('ten', 'n.', '十', '', 'I have ten fingers.', '我有十根手指。', '🔟'),
    W('tennis', 'n.', '網球', 'play tennis', 'Do you play tennis?', '你打網球嗎？', '🎾'),
    W('tent', 'n.', '帳篷', '', 'We slept in a tent.', '我們睡在帳篷裡。', '⛺'),
    W('term', 'n.', '學期；術語；期限', '', 'The final exam is at the end of the term.', '期末考在學期末。', '📅'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('It takes + 人 + 時間 + to V', '某人花多少時間做…', 'It takes me an hour to cook.'),
      ('tell + 人 + to V', '叫某人做…', 'tell him to wait'),
      ('talk to / talk about', '跟…說話 ／ 談論', 'talk to Amy about the trip'),
      ('taste / smell + 形容詞', '嚐起來 ／ 聞起來', 'taste sweet'),
      ('take a taxi / take the MRT', '搭計程車 ／ 搭捷運', 'take a taxi home'),
      ('have a talent for', '有…的天分', 'a talent for art'),
      ('take care of / take a picture', '照顧 ／ 拍照', 'take a picture of us'),
    ], 'note': 'teach-taught、tell-told、take-took-taken、tear-tore-torn。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '愛說話的', 'opts': ['talent', 'talkative', 'tall', 'target'], 'answer': 1, 'exp': 'talkative 愛說話的。'},
    {'type': 'mc', 'q': '青少年', 'opts': ['teenager', 'teacher', 'team', 'temple'], 'answer': 0, 'exp': 'teenager 青少年。'},
    {'type': 'mc', 'q': '橘子', 'opts': ['tank', 'tape', 'tangerine', 'taxi'], 'answer': 2, 'exp': 'tangerine 橘子。'},
    {'type': 'mc', 'q': '帳篷', 'opts': ['term', 'tennis', 'teapot', 'tent'], 'answer': 3, 'exp': 'tent 帳篷。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '溫度（t＿＿＿＿＿＿＿＿＿＿，11 個字母）：{0}', 'blanks': [['temperature']], 'exp': 'temperature。'},
    {'q': '電視（t＿＿＿＿＿＿＿＿＿，10 個字母）：{0}', 'blanks': [['television']], 'exp': 'television。'},
    {'q': '天分（t＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['talent']], 'exp': 'talent。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Ms. Chen {0} us English last year. （教，過去式）', 'blanks': [['taught']], 'exp': 'teach 的過去式 taught。'},
    {'q': 'He {0} me a funny story. （告訴，過去式）', 'blanks': [['told']], 'exp': 'tell 的過去式 told。'},
    {'q': 'This cake {0} really sweet. （嚐起來）', 'blanks': [['tastes']], 'exp': 'taste + 形容詞，主詞單數加 s。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'It ______ me 30 minutes to get to school.', 'opts': ['spends', 'takes', 'costs', 'pays'], 'answer': 1, 'exp': 'It takes + 人 + 時間 + to V。'},
    {'type': 'mc', 'q': 'The teacher told us ______ quiet.', 'opts': ['be', 'being', 'to be', 'are'], 'answer': 2, 'exp': 'tell + 人 + to V。'},
    {'type': 'mc', 'q': 'My brother has a ______ for drawing.', 'opts': ['talent', 'task', 'target', 'term'], 'answer': 0, 'exp': 'have a talent for 有…的天分。'},
    {'type': 'mc', 'q': 'What are you talking ______ ?', 'opts': ['to', 'with', 'for', 'about'], 'answer': 3, 'exp': 'talk about 談論。'},
  ]},
]
