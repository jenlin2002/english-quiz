# WORD UP 複習區 Unit 22（WORD UP「G-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 22, 'en': 'G-II', 'zh': 'G 開頭（二）',
  'intro': 'WORD UP「G-II」的 33 個字（golden 到 gym）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('golden', 'adj.', '金色的；金的', '', 'She has golden hair.', '她有一頭金髮。', '✨'),
    W('golf', 'n.', '高爾夫球', 'play golf', 'My uncle plays golf on weekends.', '我叔叔週末打高爾夫球。', '⛳'),
    W('good', 'adj.', '好的', '比較級 better、最高級 best；be good at 擅長', 'She is good at math.', '她擅長數學。', '👍'),
    W('good-bye', 'interj.', '再見', '= goodbye／bye', 'Say good-bye to your friends.', '跟你的朋友說再見。', '👋'),
    W('goose', 'n.', '鵝', '複數 geese', 'There are three geese on the farm.', '農場上有三隻鵝。', '🪿'),
    W('government', 'n.', '政府', '', 'The government built a new park.', '政府蓋了一座新公園。', '🏛️'),
    W('grade', 'n.', '年級；成績', 'in the seventh grade 七年級', 'I\'m in the eighth grade.', '我讀八年級。', '📊'),
    W('gram', 'n.', '公克', '縮寫 g', 'I need 200 grams of sugar.', '我需要 200 公克的糖。', '⚖️'),
    W('grand', 'adj.', '雄偉的；盛大的', '', 'We stayed at a grand hotel.', '我們住在一家豪華的飯店。', '🏰'),
    W('granddaughter', 'n.', '孫女；外孫女', '', 'Grandpa loves his granddaughter.', '爺爺很疼他的孫女。', '👧'),
    W('grandfather', 'n.', '祖父；外祖父', '= grandpa', 'My grandfather is eighty.', '我爺爺八十歲。', '👴'),
    W('grandmother', 'n.', '祖母；外祖母', '= grandma', 'My grandmother tells great stories.', '我奶奶很會說故事。', '👵'),
    W('grandson', 'n.', '孫子；外孫', '', 'Her grandson is a doctor.', '她的孫子是醫生。', '👦'),
    W('grape', 'n.', '葡萄', '', 'I bought a bunch of grapes.', '我買了一串葡萄。', '🍇'),
    W('grass', 'n.', '草；草地', '不可數', 'Keep off the grass.', '請勿踐踏草地。', '🌱'),
    W('gray', 'adj./n.', '灰色的；灰色', '英式 grey', 'The sky is gray today.', '今天天空灰灰的。', '🩶'),
    W('great', 'adj.', '很棒的；偉大的', '', 'That\'s a great idea!', '那是個好主意！', '🌟'),
    W('greedy', 'adj.', '貪心的', '', 'Don\'t be greedy. Share with others.', '不要貪心，跟別人分享。', '🤑'),
    W('green', 'adj./n.', '綠色的；綠色', '', 'The traffic light turned green.', '紅綠燈變綠燈了。', '🟢'),
    W('greet', 'v.', '問候；迎接', 'greeting 問候（名詞）', 'The teacher greeted us at the door.', '老師在門口迎接我們。', '🙋'),
    W('ground', 'n.', '地面；場地', 'on the ground 在地上', 'The ball fell to the ground.', '球掉到地上。', '🟫'),
    W('group', 'n.', '團體；組', 'in groups 分組', 'We worked in groups of four.', '我們四人一組。', '👥'),
    W('grow', 'v.', '生長；種植；變得', '三態 grow-grew-grown；grow up 長大', 'What do you want to be when you grow up?', '你長大想做什麼？', '🌱'),
    W('growth', 'n.', '成長', '', 'Milk is good for children\'s growth.', '牛奶對兒童的成長有益。', '📈'),
    W('guard', 'n./v.', '警衛；守衛', '', 'The guard stands at the gate.', '警衛站在大門口。', '💂'),
    W('guava', 'n.', '芭樂', '', 'Guavas are popular in Taiwan.', '芭樂在台灣很受歡迎。', '🍈'),
    W('guess', 'v./n.', '猜', 'Guess what! 你猜怎麼著', 'Guess what! I won the prize.', '你猜怎麼著！我得獎了。', '🤔'),
    W('guest', 'n.', '客人', 'host 主人', 'We have guests for dinner tonight.', '我們今晚有客人來吃晚餐。', '🛎️'),
    W('guide', 'n./v.', '導遊；引導', 'tour guide 導遊', 'Our tour guide speaks three languages.', '我們的導遊會說三種語言。', '🧭'),
    W('guitar', 'n.', '吉他', 'play the guitar', 'He plays the guitar very well.', '他吉他彈得很好。', '🎸'),
    W('gun', 'n.', '槍', '', 'The police officer has a gun.', '那位警察有配槍。', '🔫'),
    W('guy', 'n.', '傢伙；人', 'you guys 你們', 'He is a nice guy.', '他是個好人。', '🧑'),
    W('gym', 'n.', '體育館；健身房', '', 'We have PE class in the gym.', '我們在體育館上體育課。', '🏋️'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('be good at', '擅長', 'be good at drawing'),
      ('grow up', '長大', 'I grew up in Tainan.'),
      ('grow / growth', '生長（動詞）／ 成長（名詞）', 'Plants grow. ／ fast growth'),
      ('guest / guess', '客人 ／ 猜', 'invite guests ／ guess the answer'),
      ('goose → geese', '鵝的複數', 'two geese'),
      ('grandfather / grandson', '祖父 ／ 孫子', 'my grandfather and his grandson'),
      ('in the + 序數 + grade', '讀幾年級', 'in the seventh grade'),
    ], 'note': 'good-better-best：good 的比較級 better、最高級 best。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '政府', 'opts': ['guard', 'government', 'group', 'guide'], 'answer': 1, 'exp': 'government 政府。'},
    {'type': 'mc', 'q': '貪心的', 'opts': ['greedy', 'great', 'green', 'grand'], 'answer': 0, 'exp': 'greedy 貪心的。'},
    {'type': 'mc', 'q': '芭樂', 'opts': ['grape', 'grass', 'guava', 'gram'], 'answer': 2, 'exp': 'guava 芭樂。'},
    {'type': 'mc', 'q': '問候；迎接', 'opts': ['guess', 'grow', 'guard', 'greet'], 'answer': 3, 'exp': 'greet 問候。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '吉他（g＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['guitar']], 'exp': 'guitar。'},
    {'q': '客人（g＿＿＿＿，5 個字母）：{0}', 'blanks': [['guest']], 'exp': 'guest。'},
    {'q': '成長（g＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['growth']], 'exp': 'growth。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'My cousin is very {0} at singing. （擅長的）', 'blanks': [['good']], 'exp': 'be good at 擅長。'},
    {'q': 'There are five {0} in the pond. （鵝，複數）', 'blanks': [['geese']], 'exp': 'goose 的複數 geese。'},
    {'q': 'I {0} up in a small town. （長大，過去式）', 'blanks': [['grew']], 'exp': 'grow 的過去式 grew。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Amy is ______ the seventh grade.', 'opts': ['at', 'on', 'in', 'of'], 'answer': 2, 'exp': 'in the seventh grade 讀七年級。'},
    {'type': 'mc', 'q': 'Ben runs ______ than Tom.', 'opts': ['good', 'better', 'best', 'well'], 'answer': 1, 'exp': '比較：well 的比較級 better。'},
    {'type': 'mc', 'q': '______ what! We are going to Japan!', 'opts': ['Guess', 'Guest', 'Greet', 'Guide'], 'answer': 0, 'exp': 'Guess what! 你猜怎麼著。'},
    {'type': 'mc', 'q': 'The teacher put us ______ groups of five.', 'opts': ['on', 'at', 'with', 'into'], 'answer': 3, 'exp': 'put…into groups 分成小組。'},
  ]},
]
