# WORD UP 複習區 Unit 5（WORD UP「B-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 5, 'en': 'B-II', 'zh': 'B 開頭（二）',
  'intro': 'WORD UP「B-II」的 34 個字（beat 到 blame）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('beat', 'v.', '打敗；敲打', '三態 beat-beat-beaten', 'Our team beat them 3 to 1.', '我們隊以三比一打敗他們。', '🥁'),
    W('beautiful', 'adj.', '美麗的', '', 'What a beautiful sunset!', '好美的夕陽！', '🌅'),
    W('become', 'v.', '變成；成為', '三態 become-became-become', 'She became a teacher last year.', '她去年成為老師。', '🦋'),
    W('bed', 'n.', '床', 'go to bed 上床睡覺', 'I go to bed at ten.', '我十點上床睡覺。', '🛏️'),
    W('bedroom', 'n.', '臥室', '', 'My bedroom is upstairs.', '我的臥室在樓上。', '🛌'),
    W('bee', 'n.', '蜜蜂', 'as busy as a bee 非常忙', 'A bee is flying around the flowers.', '一隻蜜蜂在花旁邊飛。', '🐝'),
    W('beef', 'n.', '牛肉', '不可數', 'I\'d like beef noodles, please.', '我要一碗牛肉麵。', '🥩'),
    W('beer', 'n.', '啤酒', '', 'Dad had a glass of beer with dinner.', '爸爸晚餐喝了一杯啤酒。', '🍺'),
    W('begin', 'v.', '開始', '三態 begin-began-begun', 'The movie begins at seven.', '電影七點開始。', '🎬'),
    W('beginner', 'n.', '初學者', '', 'This class is for beginners.', '這堂課是給初學者上的。', '🔰'),
    W('beginning', 'n.', '開始；開端', 'at the beginning of + 時間', 'We have a test at the beginning of the month.', '月初我們有考試。', '🚦'),
    W('behave', 'v.', '表現；守規矩', 'behave yourself 規矩一點', 'The children behaved well at the party.', '孩子們在派對上很守規矩。', '😇'),
    W('belief', 'n.', '信念；信仰', 'believe 的名詞', 'He has a strong belief in himself.', '他對自己很有信心。', '🕯️'),
    W('believe', 'v.', '相信', 'believe in 信任、相信有', 'I can\'t believe it!', '我真不敢相信！', '🤞'),
    W('bell', 'n.', '鈴；鐘', '', 'The school bell rang.', '學校的鐘聲響了。', '🔔'),
    W('belong', 'v.', '屬於', 'belong to + 人', 'This bag belongs to Amy.', '這個包包是 Amy 的。', '🏷️'),
    W('below', 'prep./adv.', '在…下面；低於', 'above 在…上面', 'The temperature is below zero.', '氣溫在零度以下。', '⬇️'),
    W('belt', 'n.', '皮帶；安全帶', 'seat belt 安全帶', 'Fasten your seat belt, please.', '請繫好安全帶。', '🪢'),
    W('bench', 'n.', '長椅', '', 'Let\'s sit on the bench and rest.', '我們坐在長椅上休息一下吧。', '🪑'),
    W('besides', 'prep./adv.', '除了…之外（還有）；此外', 'besides 包含在內；except 不包含', 'Besides English, she speaks Japanese.', '除了英文，她還會說日文。', '➕'),
    W('best', 'adj./adv.', '最好的；最好地', 'good／well 的最高級', 'You are my best friend.', '你是我最好的朋友。', '🥇'),
    W('better', 'adj./adv.', '較好的；更好地', 'good／well 的比較級', 'I feel better today.', '我今天覺得好多了。', '📈'),
    W('bicycle', 'n.', '腳踏車', '= bike；ride a bicycle', 'I ride my bicycle to school.', '我騎腳踏車上學。', '🚲'),
    W('big', 'adj.', '大的', '比較級 bigger', 'An elephant is bigger than a horse.', '大象比馬大。', '🐘'),
    W('bill', 'n.', '帳單；鈔票', '', 'Can I have the bill, please?', '請給我帳單。', '🧾'),
    W('biology', 'n.', '生物學', '', 'We learn about plants in biology class.', '我們在生物課學植物。', '🧬'),
    W('bird', 'n.', '鳥', '', 'The birds are singing in the tree.', '鳥在樹上唱歌。', '🐦'),
    W('birthday', 'n.', '生日', 'Happy birthday!', 'Happy birthday to you!', '祝你生日快樂！', '🎂'),
    W('bit', 'n.', '一點點', 'a bit ＝ a little', 'I\'m a bit tired.', '我有一點累。', '🤏'),
    W('bite', 'v./n.', '咬；一口', '三態 bite-bit-bitten', 'Be careful. The dog may bite.', '小心，那隻狗可能會咬人。', '🦷'),
    W('bitter', 'adj.', '苦的', 'sweet 甜的、sour 酸的', 'This medicine tastes bitter.', '這個藥嚐起來很苦。', '☕'),
    W('black', 'adj./n.', '黑色的；黑色', '', 'She has a black cat.', '她有一隻黑貓。', '🐈‍⬛'),
    W('blackboard', 'n.', '黑板', '', 'The teacher wrote on the blackboard.', '老師在黑板上寫字。', '🧑‍🏫'),
    W('blame', 'v.', '責怪', 'blame + 人 + for + 事', 'Don\'t blame me for your mistake.', '不要把你的錯怪到我身上。', '👉'),
  ],
  'focus': [
    {'title': '常考片語', 'head': ('說法', '中文', '例子'), 'rows': [
      ('belong to + 人', '屬於某人', 'The book belongs to me.'),
      ('believe in', '相信有、信任', 'Do you believe in ghosts?'),
      ('at the beginning of', '在…的開始', 'at the beginning of the year'),
      ('blame + 人 + for + 事', '因某事責怪某人', 'blame him for the mistake'),
      ('a bit / a little', '一點點', 'a bit cold'),
      ('go to bed', '上床睡覺', 'go to bed early'),
    ], 'note': 'belong 不用進行式：This pen belongs to me.（不說 is belonging）'},
    {'title': '容易搞混的字', 'head': ('字', '用法', '例子'), 'rows': [
      ('besides / except', '除了…還有（包含）／ 除了…以外（不包含）', 'Besides Tom, Amy came too. ／ Everyone came except Tom.'),
      ('belief / believe', '名詞 ／ 動詞', 'my belief ／ I believe you.'),
      ('begin / beginner / beginning', '開始 ／ 初學者 ／ 開端', 'begin to learn ／ a beginner ／ the beginning'),
      ('good-better-best', '好 ／ 較好 ／ 最好', 'good ／ better than ／ the best'),
      ('bit / bite', '一點點 ／ 咬（過去式也是 bit）', 'a bit ／ The dog bit me.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '生物學', 'opts': ['belief', 'biology', 'bicycle', 'birthday'], 'answer': 1, 'exp': 'biology 生物學。'},
    {'type': 'mc', 'q': '責怪', 'opts': ['blame', 'behave', 'belong', 'believe'], 'answer': 0, 'exp': 'blame 責怪。'},
    {'type': 'mc', 'q': '初學者', 'opts': ['beginning', 'begin', 'beginner', 'better'], 'answer': 2, 'exp': 'beginner 初學者。'},
    {'type': 'mc', 'q': '苦的', 'opts': ['better', 'bite', 'beer', 'bitter'], 'answer': 3, 'exp': 'bitter 苦的。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '美麗的（b＿＿＿＿＿＿＿＿，9 個字母）：{0}', 'blanks': [['beautiful']], 'exp': 'beautiful。'},
    {'q': '腳踏車（b＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['bicycle']], 'exp': 'bicycle。'},
    {'q': '長椅（b＿＿＿＿，5 個字母）：{0}', 'blanks': [['bench']], 'exp': 'bench。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'This red umbrella {0} to my sister. （屬於）', 'blanks': [['belongs']], 'exp': '主詞單數，belong 加 s：belongs to。'},
    {'q': 'Please {0} yourself in the library. （守規矩）', 'blanks': [['behave']], 'exp': 'behave yourself 規矩一點。'},
    {'q': 'It is cold today. The temperature is {0} ten degrees. （低於）', 'blanks': [['below']], 'exp': 'below 低於。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': '______ math, Ben is also good at science.', 'opts': ['Except', 'Besides', 'Below', 'Because'], 'answer': 1, 'exp': '除了數學「還有」自然：用 besides。'},
    {'type': 'mc', 'q': 'Don\'t blame Tom ______ breaking the window.', 'opts': ['to', 'of', 'for', 'with'], 'answer': 2, 'exp': 'blame + 人 + for + 事。'},
    {'type': 'mc', 'q': 'Our team ______ the champion last night.', 'opts': ['beat', 'beats', 'beating', 'to beat'], 'answer': 0, 'exp': 'beat 的過去式還是 beat。'},
    {'type': 'mc', 'q': 'I feel ______ now. Thanks for the medicine.', 'opts': ['good', 'best', 'well', 'better'], 'answer': 3, 'exp': '比剛才好：比較級 better。'},
  ]},
]
