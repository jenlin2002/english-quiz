# WORD UP 複習區 Unit 30（WORD UP「M-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 30, 'en': 'M-II', 'zh': 'M 開頭（二）',
  'intro': 'WORD UP「M-II」的 38 個字（may 到 Miss）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('may', 'aux.', '可以；可能', 'May I…? 我可以…嗎', 'May I come in?', '我可以進來嗎？', '🙋'),
    W('May', 'n.', '五月', '', 'Mother\'s Day is in May.', '母親節在五月。', '🌷'),
    W('maybe', 'adv.', '也許', '放句首；may be 是「可能是」', 'Maybe it will rain tomorrow.', '明天也許會下雨。', '🤷'),
    W('meal', 'n.', '一餐', '', 'Breakfast is the most important meal.', '早餐是最重要的一餐。', '🍽️'),
    W('mean', 'v./adj.', '意思是；刻薄的', '三態 mean-meant-meant', 'What does this word mean?', '這個字是什麼意思？', '❔'),
    W('meaning', 'n.', '意思', '', 'Do you know the meaning of this word?', '你知道這個字的意思嗎？', '📖'),
    W('means', 'n.', '方法；手段', '單複數同形；by means of', 'The MRT is a fast means of transportation.', '捷運是快速的交通工具。', '🚇'),
    W('measure', 'v.', '測量', '', 'Measure the length of the table.', '量一下桌子的長度。', '📏'),
    W('meat', 'n.', '肉', '不可數；meet 見面（同音）', 'I don\'t eat much meat.', '我不太吃肉。', '🥩'),
    W('mechanic', 'n.', '技工；修車師傅', '', 'The mechanic fixed our car.', '技師修好了我們的車。', '🔧'),
    W('medicine', 'n.', '藥', 'take medicine 吃藥', 'Take this medicine three times a day.', '這個藥一天吃三次。', '💊'),
    W('medium', 'adj.', '中等的', 'small／medium／large', 'I\'d like a medium Coke.', '我要一杯中杯可樂。', '🥤'),
    W('meet', 'v.', '遇見；見面', '三態 meet-met-met', 'Nice to meet you.', '很高興認識你。', '🤝'),
    W('meeting', 'n.', '會議', 'have a meeting', 'We have a class meeting on Friday.', '我們星期五開班會。', '🗣️'),
    W('melon', 'n.', '甜瓜', 'watermelon 西瓜', 'Watermelon is my favorite summer fruit.', '西瓜是我最愛的夏季水果。', '🍉'),
    W('member', 'n.', '成員', '', 'She is a member of the music club.', '她是音樂社的社員。', '👥'),
    W('memory', 'n.', '記憶；回憶', '複數 memories', 'I have a good memory.', '我記憶力很好。', '🧠'),
    W('menu', 'n.', '菜單', '', 'Can I see the menu, please?', '可以給我看菜單嗎？', '📋'),
    W('message', 'n.', '訊息；留言', 'leave a message 留言', 'Can I leave a message?', '我可以留言嗎？', '💬'),
    W('metal', 'n.', '金屬', '', 'This box is made of metal.', '這個盒子是金屬做的。', '🔩'),
    W('meter', 'n.', '公尺', '縮寫 m', 'The pool is 25 meters long.', '游泳池長 25 公尺。', '📐'),
    W('method', 'n.', '方法', '', 'This is a good method to learn words.', '這是背單字的好方法。', '🧪'),
    W('microwave', 'n.', '微波爐', '', 'Heat the food in the microwave.', '用微波爐加熱食物。', '📟'),
    W('middle', 'n./adj.', '中間；中間的', 'in the middle of', 'There is a tree in the middle of the yard.', '院子中間有一棵樹。', '🎯'),
    W('midnight', 'n.', '午夜', 'at midnight', 'Don\'t stay up until midnight.', '不要熬夜到半夜。', '🌙'),
    W('might', 'aux.', '可能（may 的過去式）', '可能性比 may 低', 'It might snow tonight.', '今晚可能會下雪。', '🌨️'),
    W('mile', 'n.', '英里', '約 1.6 公里', 'He runs five miles every day.', '他每天跑五英里。', '🛣️'),
    W('military', 'adj.', '軍事的', '', 'He goes to a military school.', '他讀軍校。', '🪖'),
    W('milk', 'n.', '牛奶', '不可數', 'Drink a glass of milk every day.', '每天喝一杯牛奶。', '🥛'),
    W('million', 'n.', '百萬', 'two million（不加 s）；millions of', 'Taiwan has about 23 million people.', '台灣大約有兩千三百萬人。', '💯'),
    W('mind', 'n./v.', '心；介意', 'Do you mind + V-ing? 你介意…嗎', 'Do you mind opening the window?', '你介意打開窗戶嗎？', '🧠'),
    W('mine', 'pron./n.', '我的（東西）；礦', '所有格代名詞', 'This pen is mine.', '這枝筆是我的。', '👆'),
    W('minor', 'adj.', '較小的；次要的', 'major 主要的', 'It\'s only a minor problem.', '這只是個小問題。', '🔹'),
    W('minus', 'prep.', '減', 'plus 加', 'Ten minus three is seven.', '十減三等於七。', '➖'),
    W('minute', 'n.', '分鐘', 'Wait a minute. 等一下', 'Wait a minute, please.', '請等一下。', '⏱️'),
    W('mirror', 'n.', '鏡子', '', 'She looked at herself in the mirror.', '她照了照鏡子。', '🪞'),
    W('miss', 'v.', '想念；錯過', '', 'I miss my grandma.', '我想念奶奶。', '🥺'),
    W('Miss', 'n.', '小姐（稱呼）', '未婚女性', 'Miss Lin is our English teacher.', '林老師是我們的英文老師。', '👩‍🏫'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('meat / meet', '肉 ／ 見面（同音）', 'eat meat ／ meet friends'),
      ('maybe / may be', '也許（副詞）／ 可能是（助動詞＋be）', 'Maybe he is ill. ／ He may be ill.'),
      ('Do you mind + V-ing?', '你介意…嗎？', 'Do you mind closing the door?'),
      ('mean / meaning', '意思是（動詞）／ 意思（名詞）', 'What does it mean? ／ the meaning'),
      ('miss', '想念 ／ 錯過', 'miss you ／ miss the bus'),
      ('in the middle of', '在…中間', 'in the middle of the night'),
      ('two million / millions of', '兩百萬 ／ 數百萬的', 'millions of stars'),
    ], 'note': 'mine 是所有格代名詞（= my + 名詞）：This book is mine.'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '技工', 'opts': ['member', 'mechanic', 'method', 'medium'], 'answer': 1, 'exp': 'mechanic 技工。'},
    {'type': 'mc', 'q': '微波爐', 'opts': ['microwave', 'mirror', 'metal', 'menu'], 'answer': 0, 'exp': 'microwave 微波爐。'},
    {'type': 'mc', 'q': '測量', 'opts': ['mean', 'meet', 'measure', 'miss'], 'answer': 2, 'exp': 'measure 測量。'},
    {'type': 'mc', 'q': '軍事的', 'opts': ['minor', 'million', 'middle', 'military'], 'answer': 3, 'exp': 'military 軍事的。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '藥（m＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['medicine']], 'exp': 'medicine。'},
    {'q': '訊息（m＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['message']], 'exp': 'message。'},
    {'q': '午夜（m＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['midnight']], 'exp': 'midnight。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'I {0} the bus this morning, so I was late. （錯過，過去式）', 'blanks': [['missed']], 'exp': 'miss 的過去式 missed。'},
    {'q': 'We {0} at the station yesterday. （見面，過去式）', 'blanks': [['met']], 'exp': 'meet 的過去式 met。'},
    {'q': 'That red umbrella is not yours. It\'s {0}. （我的）', 'blanks': [['mine']], 'exp': 'mine 我的（東西）。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Do you mind ______ the music down?', 'opts': ['turn', 'turning', 'to turn', 'turned'], 'answer': 1, 'exp': 'Do you mind + V-ing?'},
    {'type': 'mc', 'q': '______ I use your phone?', 'opts': ['Maybe', 'Must', 'May', 'Might be'], 'answer': 2, 'exp': 'May I…? 我可以…嗎？'},
    {'type': 'mc', 'q': 'What does this sign ______ ?', 'opts': ['mean', 'meaning', 'means', 'meant'], 'answer': 0, 'exp': 'does + 原形 mean。'},
    {'type': 'mc', 'q': '______ of people watched the game on TV.', 'opts': ['Million', 'Two millions', 'Million of', 'Millions'], 'answer': 3, 'exp': 'millions of 數百萬的。'},
  ]},
]
