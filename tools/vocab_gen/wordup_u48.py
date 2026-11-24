# WORD UP 複習區 Unit 48（WORD UP「T-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 48, 'en': 'T-II', 'zh': 'T 開頭（二）',
  'intro': 'WORD UP「T-II」的 35 個字（terrible 到 time）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('terrible', 'adj.', '可怕的；糟糕的', '', 'The weather is terrible today.', '今天天氣糟透了。', '😖'),
    W('terrific', 'adj.', '極好的', '別和 terrible 搞混', 'You did a terrific job!', '你做得太棒了！', '🤩'),
    W('test', 'n./v.', '測驗；測試', 'pass the test', 'I passed the math test.', '我數學考試及格了。', '📝'),
    W('textbook', 'n.', '課本', '', 'Open your textbook to page 30.', '把課本翻到第 30 頁。', '📘'),
    W('thank', 'v.', '感謝', 'thank + 人 + for', 'Thank you for your help.', '謝謝你的幫忙。', '🙏'),
    W('Thanksgiving', 'n.', '感恩節', '', 'Americans eat turkey on Thanksgiving.', '美國人感恩節吃火雞。', '🦃'),
    W('theater', 'n.', '戲院；劇場', '', 'Let\'s meet at the movie theater.', '我們在電影院見。', '🎭'),
    W('then', 'adv.', '然後；那時', '', 'Finish your homework, then you can play.', '先寫完功課，然後就可以玩。', '➡️'),
    W('there', 'adv.', '那裡', 'There is／are 有…', 'There is a cat under the table.', '桌子底下有一隻貓。', '📍'),
    W('therefore', 'adv.', '因此', '', 'It rained. Therefore, the game was canceled.', '下雨了，因此比賽取消。', '∴'),
    W('thick', 'adj.', '厚的；濃的', 'thin 薄的', 'This book is very thick.', '這本書很厚。', '📚'),
    W('thief', 'n.', '小偷', '複數 thieves', 'The thief ran away.', '小偷逃跑了。', '🦹'),
    W('thin', 'adj.', '瘦的；薄的', '比較級 thinner', 'He is tall and thin.', '他又高又瘦。', '🧍'),
    W('thing', 'n.', '東西；事情', '', 'Put your things in your bag.', '把你的東西放進包包。', '📦'),
    W('think', 'v.', '想；認為', '三態 think-thought-thought；think of／about', 'What do you think of this idea?', '你覺得這個點子怎麼樣？', '🤔'),
    W('third', 'adj./n.', '第三；三分之一', '', 'My birthday is on the third of May.', '我的生日是五月三日。', '3️⃣'),
    W('thirsty', 'adj.', '口渴的', '', 'I\'m thirsty. Can I have some water?', '我口渴了，可以給我一些水嗎？', '🥵'),
    W('thirteen', 'n.', '十三', '', 'My sister is thirteen.', '我妹妹十三歲。', '🔢'),
    W('thirty', 'n.', '三十', '', 'There are thirty days in June.', '六月有三十天。', '📅'),
    W('though', 'conj./adv.', '雖然；不過', '= although；不和 but 連用', 'Though it was raining, we went out.', '雖然在下雨，我們還是出門了。', '🔄'),
    W('thought', 'n.', '想法；思考', 'think 的過去式也是 thought', 'That\'s a good thought.', '那是個好想法。', '💭'),
    W('thousand', 'n.', '千', 'two thousand（不加 s）；thousands of', 'There are thousands of stars in the sky.', '天上有成千上萬顆星星。', '🔢'),
    W('three', 'n.', '三', '', 'I have three brothers.', '我有三個兄弟。', '3️⃣'),
    W('throat', 'n.', '喉嚨', 'sore throat 喉嚨痛', 'I have a sore throat.', '我喉嚨痛。', '🗣️'),
    W('through', 'prep.', '穿過；透過', '', 'The train went through the tunnel.', '火車穿過隧道。', '🚇'),
    W('throw', 'v.', '丟；扔', '三態 throw-threw-thrown', 'Don\'t throw trash on the ground.', '不要亂丟垃圾。', '🤾'),
    W('thumb', 'n.', '大拇指', 'b 不發音', 'Give me a thumbs-up!', '給我一個讚！', '👍'),
    W('thunder', 'n.', '雷', 'lightning 閃電', 'I heard thunder last night.', '我昨晚聽到打雷。', '⛈️'),
    W('Thursday', 'n.', '星期四', '', 'We have PE on Thursday.', '我們星期四有體育課。', '🗓️'),
    W('thus', 'adv.', '因此；如此', '= therefore', 'He studied hard; thus he passed.', '他很用功，因此及格了。', '➡️'),
    W('ticket', 'n.', '票', '', 'I bought two movie tickets.', '我買了兩張電影票。', '🎟️'),
    W('tidy', 'adj./v.', '整齊的；整理', 'messy 亂的', 'Keep your room tidy.', '保持房間整齊。', '🧺'),
    W('tie', 'n./v.', '領帶；綁', 'tie your shoes 綁鞋帶', 'Tie your shoelaces.', '綁好你的鞋帶。', '👔'),
    W('tiger', 'n.', '老虎', '', 'The tiger is a dangerous animal.', '老虎是危險的動物。', '🐯'),
    W('time', 'n.', '時間；次數', 'on time 準時；have a good time 玩得開心', 'We had a good time at the party.', '我們在派對上玩得很開心。', '⏰'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('terrible / terrific', '糟糕的 ／ 極好的', 'a terrible day ／ a terrific show'),
      ('think of / think about', '覺得（意見）／ 考慮', 'What do you think of it?'),
      ('though / although', '雖然（不和 but 連用）', 'Though he is young, he is wise.'),
      ('thank + 人 + for', '因…感謝某人', 'thank you for coming'),
      ('There is / There are', '有…', 'There are two cats.'),
      ('on time / in time', '準時 ／ 及時', 'arrive on time'),
      ('thousands of', '成千上萬的', 'thousands of people'),
    ], 'note': 'thief → thieves；throw-threw-thrown；think-thought-thought。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '極好的', 'opts': ['terrible', 'terrific', 'thick', 'thirsty'], 'answer': 1, 'exp': 'terrific 極好的。'},
    {'type': 'mc', 'q': '喉嚨', 'opts': ['throat', 'thumb', 'thunder', 'through'], 'answer': 0, 'exp': 'throat 喉嚨。'},
    {'type': 'mc', 'q': '整齊的', 'opts': ['thin', 'tie', 'tidy', 'time'], 'answer': 2, 'exp': 'tidy 整齊的。'},
    {'type': 'mc', 'q': '因此', 'opts': ['though', 'then', 'there', 'therefore'], 'answer': 3, 'exp': 'therefore 因此。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '口渴的（t＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['thirsty']], 'exp': 'thirsty。'},
    {'q': '星期四（T＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['Thursday', 'thursday']], 'exp': 'Thursday。'},
    {'q': '課本（t＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['textbook']], 'exp': 'textbook。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The police caught two {0} last night. （小偷，複數）', 'blanks': [['thieves']], 'exp': 'thief 的複數 thieves。'},
    {'q': 'He {0} the ball to me. （丟，過去式）', 'blanks': [['threw']], 'exp': 'throw 的過去式 threw。'},
    {'q': 'Please be on {0}. The bus leaves at eight. （準時）', 'blanks': [['time']], 'exp': 'on time 準時。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': '______ it was cold, he didn\'t wear a coat.', 'opts': ['But', 'Though', 'So', 'Because'], 'answer': 1, 'exp': 'Though 雖然（不和 but 連用）。'},
    {'type': 'mc', 'q': 'What do you think ______ my new hairstyle?', 'opts': ['to', 'at', 'of', 'in'], 'answer': 2, 'exp': 'think of 覺得…如何。'},
    {'type': 'mc', 'q': 'Thank you ______ the lovely gift.', 'opts': ['for', 'to', 'of', 'with'], 'answer': 0, 'exp': 'thank + 人 + for。'},
    {'type': 'mc', 'q': '______ of people visit Taipei 101 every year.', 'opts': ['Thousand', 'Two thousands', 'Thousand of', 'Thousands'], 'answer': 3, 'exp': 'thousands of 成千上萬的。'},
  ]},
]
