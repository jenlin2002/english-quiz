# WORD UP 複習區 Unit 4（WORD UP「B-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 4, 'en': 'B-I', 'zh': 'B 開頭（一）',
  'intro': 'WORD UP「B-I」的 34 個字（baby 到 beard）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('baby', 'n.', '嬰兒', '複數 babies', 'The baby is crying.', '寶寶在哭。', '👶'),
    W('back', 'n./adv.', '背部；後面；回來', 'come back 回來', 'I will be back in ten minutes.', '我十分鐘後回來。', '🔙'),
    W('backward', 'adv.', '向後', '= backwards；forward 向前', 'Can you count backward from ten?', '你會從十倒數嗎？', '⏪'),
    W('bad', 'adj.', '壞的；不好的', '比較級 worse、最高級 worst', 'Eating too much candy is bad for your teeth.', '吃太多糖果對牙齒不好。', '👎'),
    W('badminton', 'n.', '羽毛球', 'play badminton（不加 the）', 'We play badminton after school.', '我們放學後打羽毛球。', '🏸'),
    W('bag', 'n.', '袋子；包包', 'schoolbag 書包', 'Put your books in your bag.', '把書放進你的包包。', '👜'),
    W('bake', 'v.', '烘焙；烤', '', 'Mom is baking a cake for my birthday.', '媽媽在烤我的生日蛋糕。', '🧁'),
    W('bakery', 'n.', '麵包店', 'baker 麵包師傅', 'I bought some bread at the bakery.', '我在麵包店買了一些麵包。', '🥐'),
    W('balcony', 'n.', '陽台', '', 'There are many plants on our balcony.', '我們家陽台有很多植物。', '🪴'),
    W('ball', 'n.', '球', '', 'The boy kicked the ball.', '男孩踢了那顆球。', '⚽'),
    W('balloon', 'n.', '氣球', '', 'The kids are holding colorful balloons.', '孩子們拿著彩色氣球。', '🎈'),
    W('banana', 'n.', '香蕉', '', 'Monkeys love bananas.', '猴子很愛香蕉。', '🍌'),
    W('band', 'n.', '樂團；帶子', '', 'My brother plays the drums in a band.', '我哥哥在樂團裡打鼓。', '🎸'),
    W('bank', 'n.', '銀行；河岸', '', 'Dad went to the bank to get some money.', '爸爸去銀行領錢。', '🏦'),
    W('banker', 'n.', '銀行家', '', 'Her father is a banker.', '她爸爸是銀行家。', '💼'),
    W('bar', 'n.', '酒吧；條狀物', 'a bar of chocolate 一條巧克力', 'I ate a bar of chocolate.', '我吃了一條巧克力。', '🍫'),
    W('barbecue', 'n./v.', '烤肉', '= BBQ', 'We have a barbecue on Moon Festival.', '我們中秋節會烤肉。', '🍖'),
    W('barber', 'n.', '理髮師', 'barbershop 理髮店', 'The barber cut my hair too short.', '理髮師把我的頭髮剪得太短了。', '💈'),
    W('bark', 'v./n.', '（狗）吠叫', '', 'The dog barks at strangers.', '那隻狗會對陌生人叫。', '🐕'),
    W('base', 'n.', '基地；底部；（棒球）壘', '', 'The runner reached second base.', '跑者上了二壘。', '⚾'),
    W('baseball', 'n.', '棒球', 'play baseball', 'Baseball is popular in Taiwan.', '棒球在台灣很受歡迎。', '⚾'),
    W('basement', 'n.', '地下室', '', 'We keep old boxes in the basement.', '我們把舊箱子放在地下室。', '🏚️'),
    W('basic', 'adj.', '基本的', '', 'Learn the basic rules first.', '先學基本規則。', '🧱'),
    W('basis', 'n.', '基礎；根據', 'on a daily basis 每天', 'I practice English on a daily basis.', '我每天練習英文。', '📐'),
    W('basket', 'n.', '籃子', '', 'There are eggs in the basket.', '籃子裡有雞蛋。', '🧺'),
    W('basketball', 'n.', '籃球', 'play basketball', 'Let\'s play basketball this afternoon.', '我們今天下午去打籃球吧。', '🏀'),
    W('bat', 'n.', '球棒；蝙蝠', '', 'He hit the ball with a bat.', '他用球棒打球。', '🦇'),
    W('bath', 'n.', '洗澡；浴缸', 'take a bath 洗澡', 'I take a bath every night.', '我每天晚上洗澡。', '🛁'),
    W('bathroom', 'n.', '浴室；廁所', '', 'May I use your bathroom?', '我可以借用你的廁所嗎？', '🚿'),
    W('be', 'v.', '是；成為', 'am／is／are／was／were／been', 'I want to be a doctor.', '我想當醫生。', '🧑‍⚕️'),
    W('beach', 'n.', '海灘', 'on the beach', 'We built a sandcastle on the beach.', '我們在海灘上堆沙堡。', '🏖️'),
    W('bean', 'n.', '豆子', 'red beans 紅豆', 'I like red bean soup.', '我喜歡紅豆湯。', '🫘'),
    W('bear', 'n./v.', '熊；忍受', 'can\'t bear 受不了', 'I can\'t bear the noise.', '我受不了這個噪音。', '🐻'),
    W('beard', 'n.', '鬍子（下巴的）', 'mustache 嘴上的鬍子', 'Santa Claus has a long white beard.', '聖誕老人有長長的白鬍子。', '🧔'),
  ],
  'focus': [
    {'title': '常考片語', 'head': ('說法', '中文', '例子'), 'rows': [
      ('come back / be back', '回來', 'I\'ll be back soon.'),
      ('take a bath', '洗澡', 'take a bath before bed'),
      ('play + 球類（不加 the）', '打球', 'play badminton ／ play baseball'),
      ('bark at + 人', '對…吠叫', 'The dog barks at me.'),
      ('can\'t bear', '受不了', 'I can\'t bear the heat.'),
      ('on a daily basis', '每天', 'exercise on a daily basis'),
    ], 'note': '樂器要加 the：play the drums；球類不加：play basketball。'},
    {'title': '一家人和容易搞混的字', 'head': ('字', '用法', '例子'), 'rows': [
      ('bake / bakery / baker', '烘焙 ／ 麵包店 ／ 麵包師傅', 'bake cookies ／ go to the bakery'),
      ('bank / banker', '銀行 ／ 銀行家', 'work at a bank ／ a banker'),
      ('base / basic / basis', '基地、壘 ／ 基本的 ／ 基礎', 'first base ／ basic skills ／ on this basis'),
      ('bath / bathroom', '洗澡 ／ 浴室', 'take a bath ／ in the bathroom'),
      ('bat', '球棒 ／ 蝙蝠（一字兩義）', 'a baseball bat ／ Bats fly at night.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '陽台', 'opts': ['basement', 'balcony', 'bathroom', 'bakery'], 'answer': 1, 'exp': 'balcony 陽台。'},
    {'type': 'mc', 'q': '理髮師', 'opts': ['banker', 'baker', 'barber', 'beard'], 'answer': 2, 'exp': 'barber 理髮師。'},
    {'type': 'mc', 'q': '羽毛球', 'opts': ['badminton', 'baseball', 'basketball', 'balloon'], 'answer': 0, 'exp': 'badminton 羽毛球。'},
    {'type': 'mc', 'q': '基本的', 'opts': ['basis', 'base', 'basket', 'basic'], 'answer': 3, 'exp': 'basic 基本的。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '氣球（b＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['balloon']], 'exp': 'balloon。'},
    {'q': '海灘（b＿＿＿＿，5 個字母）：{0}', 'blanks': [['beach']], 'exp': 'beach。'},
    {'q': '地下室（b＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['basement']], 'exp': 'basement。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Grandma likes to {0} cookies on weekends. （烘焙）', 'blanks': [['bake']], 'exp': 'bake 烘焙。'},
    {'q': 'The dog began to {0} at the mailman. （吠叫）', 'blanks': [['bark']], 'exp': 'bark at 對…吠叫。'},
    {'q': 'My grandpa has a long gray {0}. （鬍子）', 'blanks': [['beard']], 'exp': 'beard 下巴的鬍子。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Do you want to play ______ basketball with us?', 'opts': ['a', 'the', '（不填）', 'an'], 'answer': 2, 'exp': 'play + 球類不加冠詞。'},
    {'type': 'mc', 'q': 'I usually take a ______ after dinner.', 'opts': ['bath', 'bathroom', 'beach', 'basket'], 'answer': 0, 'exp': 'take a bath 洗澡。'},
    {'type': 'mc', 'q': 'I can\'t ______ the hot weather in summer.', 'opts': ['bark', 'bake', 'base', 'bear'], 'answer': 3, 'exp': 'can\'t bear 受不了。'},
    {'type': 'mc', 'q': 'My English is getting ______ . I need more practice.', 'opts': ['bad', 'worse', 'worst', 'badly'], 'answer': 1, 'exp': 'bad 的比較級是 worse。'},
  ]},
]
