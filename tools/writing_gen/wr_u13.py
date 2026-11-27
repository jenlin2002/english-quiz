# 寫作園地 Unit 13 Saying Sorry 寫道歉卡片（內容全部自編）

UNIT = {
  'no': 13, 'en': 'Saying Sorry', 'zh': '寫道歉卡片', 'card': True,
  'intro': '寫一張道歉卡片：說明你做錯了什麼、為什麼會這樣、對方的感受、你會怎麼補救、以後會怎麼做。',
  'tense': '說發生的事用過去式（I broke… / I forgot…）；說補救和以後用 will（I will… / I won\'t… again）。開頭 Dear…，結尾署名。',
  'dialog': [
    ('Amy', 'Ben, you look upset. What\'s wrong?'),
    ('Ben', 'I borrowed my friend Leo\'s comic book, and I spilled juice on it.'),
    ('Amy', 'Oh no. Did you tell him?'),
    ('Ben', 'Not yet. I feel terrible. I don\'t know what to say.'),
    ('Amy', 'Why don\'t you write him a card? Say sorry and explain what happened.'),
    ('Ben', 'Good idea. I can also buy him a new one with my pocket money.'),
    ('Amy', 'That\'s a great way to fix it. He\'ll understand.'),
    ('Ben', 'Thanks, Amy. I\'ll be more careful next time.'),
  ],
  'speak': [
    ('When did you last say sorry to someone?', '你上次跟人道歉是什麼時候？', 'Last week, I said sorry to my sister.'),
    ('What happened?', '發生了什麼事？', 'I broke her pencil case.'),
    ('How did the other person feel?', '對方覺得怎樣？', 'She was angry and sad.'),
    ('What did you do to make it better?', '你怎麼補救？', 'I bought her a new one. / I helped her clean up.'),
  ],
  'words': [
    ('I\'m sorry', '對不起', 'I\'m sorry for being late.', '對不起我遲到了。', r"(i'?m|i am|so|really) sorry|apologi[sz]e"),
    ('mistake', '錯誤', 'It was my mistake.', '那是我的錯。', r'mistakes?|my fault'),
    ('break', '打破；弄壞', 'I broke your cup by accident.', '我不小心打破了你的杯子。', r'br(eak|eaks|oke|oken)'),
    ('forget', '忘記', 'I forgot your birthday.', '我忘了你的生日。', r'forg(et|ets|ot|otten)'),
    ('by accident', '不小心', 'I stepped on your foot by accident.', '我不小心踩到你的腳。', r'by accident|accidentally|didn\'t mean to'),
    ('upset', '難過的；生氣的', 'You were upset, and I understand.', '你很難過，我能理解。', r'upset|angry|sad|hurt'),
    ('feel terrible', '覺得很糟', 'I feel terrible about it.', '我對這件事覺得很過意不去。', r'feel(s)? (terrible|bad|awful)|felt (terrible|bad|awful)'),
    ('should have', '早該…', 'I should have told you the truth.', '我早該告訴你實話。', r'should(n\'t)? have'),
    ('promise', '保證', 'I promise it won\'t happen again.', '我保證不會再發生。', r'promis(e|es|ed)'),
    ('careful', '小心的', 'I will be more careful.', '我會更小心。', r'careful(ly)?'),
    ('make it up to you', '補償你', 'Let me make it up to you.', '讓我補償你。', r'make (it )?up|buy you|fix|replace|pay for'),
    ('forgive', '原諒', 'I hope you can forgive me.', '希望你能原諒我。', r'forgiv(e|es|en)|forgave'),
    ('friendship', '友誼', 'Our friendship is important to me.', '我們的友誼對我很重要。', r'friendship|best friend|good friends?'),
    ('next time', '下一次', 'Next time, I will ask first.', '下次我會先問。', r'next time|from now on|again'),
  ],
  'frames': [
    ('Dear ____,', '親愛的……', 'Dear Leo,'),
    ('I\'m really sorry for ____.', '我真的很抱歉……', 'I\'m really sorry for spilling juice on your comic book.'),
    ('I didn\'t mean to ____.', '我不是故意要……', 'I didn\'t mean to make you upset.'),
    ('I should have ____.', '我早該……', 'I should have been more careful.'),
    ('To make it up to you, I will ____.', '為了補償你，我會……', 'To make it up to you, I will buy you a new one.'),
    ('I promise I will ____ next time.', '我保證下次會……', 'I promise I will be more careful next time.'),
  ],
  'write': {
    'prompt': 'Write a card to say sorry to someone.',
    'zh': '寫一張道歉卡片給家人或朋友：開頭 Dear…，說明你做錯了什麼、怎麼補救、以後會怎麼做，最後署名。',
    'qs': [('Who are you writing to? What did you do?', '寫給誰？你做了什麼？'), ('How did he or she feel?', '對方的感受？'),
           ('How will you make it up?', '你會怎麼補救？'), ('What will you do next time?', '下次會怎麼做？')],
    'model': {
      1: 'Dear Mom, I\'m sorry I forgot to clean my room. I know you were upset. '
         'I will clean it right after school today. I promise I will remember next time. Love, Amy',
      2: 'Dear Leo, I\'m really sorry about your comic book. When I was reading it at lunch, I spilled orange juice on it by accident. '
         'I know it was your favorite book, and I feel terrible. I should have been more careful. '
         'To make it up to you, I am going to buy you a new one this weekend with my pocket money. '
         'Our friendship is very important to me, so I hope you can forgive me. '
         'Next time, I will keep drinks away from books. Your friend, Ben',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'I was late. I missed the bus. (because)<br>→ {0}', 'blanks': [['I was late because I missed the bus.', 'Because I missed the bus, I was late.']],
     'exp': '結果 because 原因。'},
    {'q': 'I broke your cup. I didn\'t mean to. (but)<br>→ {0}', 'blanks': [["I broke your cup, but I didn't mean to.", "I broke your cup but I didn't mean to.", 'I broke your cup, but I did not mean to.']],
     'exp': 'but 接相反的兩句。'},
    {'q': 'I forgot your birthday. I feel terrible. (so)<br>→ {0}', 'blanks': [['I forgot your birthday, so I feel terrible.', 'I forgot your birthday so I feel terrible.']],
     'exp': '原因, so 結果。'},
    {'q': 'I was playing ball. I broke the window. (while)<br>→ {0}', 'blanks': [['While I was playing ball, I broke the window.', 'I broke the window while I was playing ball.']],
     'exp': 'while + 過去進行式（正在…的時候）。'},
    {'q': 'I hope. You can forgive me. (that)<br>→ {0}', 'blanks': [['I hope that you can forgive me.', 'I hope you can forgive me.']],
     'exp': 'I hope (that) + 子句。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'I am sorry. I am late.（用 for 合成一句）<br>→ {0}', 'blanks': [['I am sorry for being late.', "I'm sorry for being late."]],
     'exp': 'sorry for + V-ing：am late → being late。'},
    {'q': 'I will be careless again.（改成否定句）<br>→ {0}', 'blanks': [["I won't be careless again.", 'I will not be careless again.']],
     'exp': "will 的否定：won't。"},
    {'q': 'I didn\'t tell you the truth.（改成 I should have … 表示「早該」）<br>→ {0}', 'blanks': [['I should have told you the truth.']],
     'exp': 'should have + p.p.＝早該做卻沒做。tell → told。'},
    {'q': 'You broke my pencil.（改成 Did 開頭的問句）<br>→ {0}', 'blanks': [['Did you break my pencil?']],
     'exp': 'Did + 主詞 + 原形：broke → break。'},
    {'q': 'Be more careful.（改成 Please 開頭）<br>→ {0}', 'blanks': [['Please be more careful.']],
     'exp': 'Please + 祈使句更有禮貌。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'mean / I / to / didn\'t / it / do<br>→ {0}', 'blanks': [["I didn't mean to do it."]], 'exp': "didn't mean to＝不是故意的。"},
    {'q': 'mistake / It / my / was<br>→ {0}', 'blanks': [['It was my mistake.']], 'exp': 'It was my mistake.＝是我的錯。'},
    {'q': 'promise / I / happen / won\'t / it / again<br>→ {0}', 'blanks': [["I promise it won't happen again."]], 'exp': 'I promise + 子句。'},
    {'q': 'up / you / Let / make / it / me / to<br>→ {0}', 'blanks': [['Let me make it up to you.']], 'exp': 'make it up to 人＝補償某人。'},
    {'q': 'forgive / you / Can / me<br>→ {0}', 'blanks': [['Can you forgive me?']], 'exp': 'Can you + 原形？'},
  ]},
]
