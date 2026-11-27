# 寫作園地 Unit 12 An Invitation Card 寫邀請卡（內容全部自編）

UNIT = {
  'no': 12, 'en': 'An Invitation Card', 'zh': '寫邀請卡', 'card': True,
  'intro': '寫一張邀請卡：邀請朋友參加你的活動（派對、球賽、表演、烤肉），寫清楚什麼活動、時間、地點、要帶什麼、怎麼回覆。',
  'tense': '邀請用 Would you like to…? / Please come to…；活動是未來的事，用 will 或 be going to。卡片開頭 Dear…，結尾 Love／Your friend＋名字。',
  'dialog': [
    ('Amy', 'I\'m having a barbecue party next Saturday. Would you like to come?'),
    ('Ben', 'I\'d love to! What time does it start?'),
    ('Amy', 'At five in the afternoon. It\'s in my backyard.'),
    ('Ben', 'Should I bring anything?'),
    ('Amy', 'You can bring some drinks or snacks if you want.'),
    ('Ben', 'Sure. Can I bring my little sister?'),
    ('Amy', 'Of course! Please tell me by Wednesday, so I can buy enough food.'),
    ('Ben', 'OK. Thanks for inviting me!'),
  ],
  'speak': [
    ('What event do you want to invite friends to?', '你想邀請朋友參加什麼活動？', 'My birthday party. / A basketball game.'),
    ('When and where is it?', '什麼時候、在哪裡？', 'It is on Sunday at three, at my home.'),
    ('What should your friends bring?', '朋友要帶什麼？', 'They can bring a swimsuit.'),
    ('How should they answer you?', '他們要怎麼回覆你？', 'Please call me or send me a message.'),
  ],
  'words': [
    ('invite', '邀請', 'I want to invite you to my party.', '我想邀請你來我的派對。', r'invit(e|es|ed|ing|ation)'),
    ('Would you like to …?', '你想要…嗎？', 'Would you like to come to my concert?', '你想來我的音樂會嗎？', r'would you like to'),
    ('Please come to …', '請來參加…', 'Please come to my birthday party.', '請來參加我的生日派對。', r'please come|hope you can come|join us'),
    ('date', '日期', 'Date: Saturday, May 10', '日期：5 月 10 日星期六', r'date|(monday|tuesday|wednesday|thursday|friday|saturday|sunday)'),
    ('time', '時間', 'Time: 2:00 p.m. to 5:00 p.m.', '時間：下午兩點到五點', r'\btime\b|o\'?clock|\d ?(a\.?m\.?|p\.?m\.?)|\d:\d\d'),
    ('place', '地點', 'Place: My home, 25 Park Road', '地點：我家，公園路 25 號', r'place|address|at my (home|house)'),
    ('bring', '帶來', 'Please bring your swimsuit.', '請帶泳衣。', r'bring(s|ing)?|brought'),
    ('celebrate', '慶祝', 'Let\'s celebrate together!', '我們一起慶祝吧！', r'celebrat(e|es|ed|ing|ion)'),
    ('let me know', '讓我知道', 'Please let me know if you can come.', '能不能來請讓我知道。', r'let me know|tell me|reply|call me|text me|message me'),
    ('by (+ 日期)', '在…之前', 'Please reply by Friday.', '請在星期五前回覆。', r'\bby (monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|next)'),
    ('see you there', '到時見', 'See you there!', '到時見！', r'see you'),
    ('fun', '有趣的；樂趣', 'It will be a lot of fun.', '一定會很好玩。', r'fun'),
    ('dress up', '打扮', 'Please dress up as a movie character.', '請打扮成電影角色。', r'dress(es|ed)? up|wear'),
    ('Dear …', '親愛的…（卡片開頭）', 'Dear Amy,', '親愛的 Amy：', r'^\s*dear|\bdear\b'),
  ],
  'frames': [
    ('Dear ____,', '親愛的……（收卡的人）', 'Dear Tom,'),
    ('I am having a ____ on ____.', '我在……（日期）要辦一個……', 'I am having a pool party on Sunday, July 20.'),
    ('Would you like to come?', '你想來嗎？（照抄這句）', 'Would you like to come?'),
    ('It will be at ____ from ____ to ____.', '地點在……，時間從……到……', 'It will be at my home from two to five p.m.'),
    ('Please bring ____.', '請帶……', 'Please bring a swimsuit and a towel.'),
    ('Please let me know by ____.', '請在……前讓我知道', 'Please let me know by Wednesday.'),
  ],
  'write': {
    'prompt': 'Write an invitation card to a friend.',
    'zh': '寫一張邀請卡給朋友：開頭 Dear…，說明什麼活動、日期時間、地點、要帶什麼、什麼時候前回覆，最後署名。',
    'qs': [('What is the event?', '什麼活動？'), ('When and where is it?', '日期、時間、地點？'),
           ('What should your friend bring or wear?', '要帶或穿什麼？'), ('How and when should your friend reply?', '怎麼回覆、什麼時候前回覆？')],
    'model': {
      1: 'Dear Tom, I am having a birthday party on Saturday. It will be at my home at three p.m. '
         'Would you like to come? Please let me know by Friday. Your friend, Ben',
      2: 'Dear Lisa, Our class is going to have a Christmas party, and I want to invite you! '
         'It will be in our classroom on Friday, December 20, from four to six p.m. '
         'We will play games, sing songs, and exchange presents, so please bring a small gift that costs less than two hundred dollars. '
         'You can also dress up in red or green. '
         'Please let me know by Monday so I can prepare enough food. I hope you can come! Love, Amy',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'The party starts at six. It ends at nine. (and)<br>→ {0}', 'blanks': [['The party starts at six and ends at nine.', 'The party starts at six, and it ends at nine.', 'The party starts at six and it ends at nine.']],
     'exp': '主詞一樣，兩個動詞用 and 接。'},
    {'q': 'I want to invite you. It is my birthday. (because)<br>→ {0}', 'blanks': [['I want to invite you because it is my birthday.', "I want to invite you because it's my birthday."]],
     'exp': '結果 because 原因。'},
    {'q': 'You can come. Please call me. (If)<br>→ {0}', 'blanks': [['If you can come, please call me.', 'Please call me if you can come.']],
     'exp': 'If + 條件, 祈使句。'},
    {'q': 'Please bring a swimsuit. We will swim in the pool. (because)<br>→ {0}', 'blanks': [['Please bring a swimsuit because we will swim in the pool.', "Please bring a swimsuit because we'll swim in the pool."]],
     'exp': '請求 because 原因。'},
    {'q': 'I hope. You can come to my party. (that)<br>→ {0}', 'blanks': [['I hope that you can come to my party.', 'I hope you can come to my party.']],
     'exp': 'I hope (that) + 子句。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'Do you want to come to my party?（改成更有禮貌的 Would you like 開頭）<br>→ {0}', 'blanks': [['Would you like to come to my party?']],
     'exp': 'Would you like to + 原形 ＝ Do you want to 的客氣說法。'},
    {'q': 'The party is at my house.（針對 at my house 用 Where 問）<br>→ {0}', 'blanks': [['Where is the party?', "Where's the party?"]],
     'exp': 'Where is + 主詞？'},
    {'q': 'We have a party every Friday.（把 every Friday 改成 next Friday，用 will）<br>→ {0}', 'blanks': [['We will have a party next Friday.', "We'll have a party next Friday."]],
     'exp': 'next + 時間 → will + 原形。'},
    {'q': 'Let\'s have a barbecue.（改成 Why don\'t we 開頭）<br>→ {0}', 'blanks': [["Why don't we have a barbecue?"]],
     'exp': "Why don't we + 原形？＝我們何不…？"},
    {'q': 'You need to bring food.（改成否定句）<br>→ {0}', 'blanks': [["You don't need to bring food.", 'You do not need to bring food.']],
     'exp': "don't need to＝不需要。"},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'like / Would / to / you / come<br>→ {0}', 'blanks': [['Would you like to come?']], 'exp': 'Would you like to + 原形？'},
    {'q': 'know / let / Please / by / me / Friday<br>→ {0}', 'blanks': [['Please let me know by Friday.']], 'exp': 'let me know＝讓我知道。by＝在…之前。'},
    {'q': 'to / you / invite / I / want / party / my / to<br>→ {0}', 'blanks': [['I want to invite you to my party.']], 'exp': 'invite 人 to 活動。'},
    {'q': 'there / you / See<br>→ {0}', 'blanks': [['See you there!', 'See you there.']], 'exp': 'See you there!＝到時見！'},
    {'q': 'will / It / a / be / fun / of / lot<br>→ {0}', 'blanks': [['It will be a lot of fun.']], 'exp': 'a lot of fun＝很好玩。'},
  ]},
]
