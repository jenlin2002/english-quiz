# 寫作園地 Unit 8 Asking the Way 問路（內容全部自編）

UNIT = {
  'no': 8, 'en': 'Asking the Way', 'zh': '問路',
  'intro': '學會問路和報路：寫一段「從你家（或學校）到某個地方怎麼走」的說明，或寫一次問路的經驗。',
  'tense': '報路用祈使句（Go straight… / Turn left…）和現在式（It is next to…）；寫問路經驗用過去式。',
  'dialog': [
    ('Amy', 'Excuse me. Could you tell me how to get to the library?'),
    ('Ben', 'Sure. Go straight down this street for two blocks.'),
    ('Amy', 'Two blocks. And then?'),
    ('Ben', 'Turn left at the traffic light. The library is on your right.'),
    ('Amy', 'Is it far from here?'),
    ('Ben', 'No, it\'s only about five minutes on foot.'),
    ('Amy', 'Is it next to the post office?'),
    ('Ben', 'Yes, it\'s between the post office and a small park. You can\'t miss it.'),
  ],
  'speak': [
    ('How do you get to school?', '你怎麼去學校？', 'I walk to school. / I take the bus.'),
    ('What is near your home?', '你家附近有什麼？', 'There is a park and a convenience store.'),
    ('How do you get from your home to the nearest store?', '從你家到最近的店怎麼走？', 'Go out and turn right. It\'s on the corner.'),
    ('Did you ever get lost? What did you do?', '你迷過路嗎？怎麼辦？', 'Yes. I asked a police officer for help.'),
  ],
  'words': [
    ('go straight', '直走', 'Go straight for two blocks.', '直走兩個路口。', r'go(es)? straight|went straight'),
    ('turn left / right', '左轉／右轉', 'Turn right at the bank.', '在銀行右轉。', r'turn(s|ed)? (left|right)'),
    ('block', '街區；路口', 'The park is three blocks away.', '公園在三個路口外。', r'blocks?'),
    ('corner', '轉角', 'There is a bakery on the corner.', '轉角有一家麵包店。', r'corners?'),
    ('traffic light', '紅綠燈', 'Stop at the traffic light.', '在紅綠燈停下來。', r'traffic lights?'),
    ('cross', '穿越', 'Cross the street carefully.', '小心過馬路。', r'cross(es|ed|ing)?'),
    ('next to', '在…旁邊', 'The bank is next to the hospital.', '銀行在醫院旁邊。', r'next to'),
    ('between … and …', '在…和…之間', 'The shop is between the bank and the school.', '店在銀行和學校中間。', r'between'),
    ('across from', '在…對面', 'The MRT station is across from the mall.', '捷運站在購物中心對面。', r'across from|opposite'),
    ('on foot', '走路', 'It takes ten minutes on foot.', '走路要十分鐘。', r'on foot|walk(s|ed|ing)?'),
    ('far from', '離…遠', 'My school isn\'t far from my home.', '我的學校離我家不遠。', r'far( from)?'),
    ('get lost', '迷路', 'I got lost in the city.', '我在城市裡迷路了。', r'(get|got|gets) lost|lost'),
    ('map', '地圖', 'Let\'s check the map on my phone.', '我們看一下手機上的地圖。', r'maps?'),
    ('How do I get to …?', '…怎麼去？', 'How do I get to the train station?', '火車站怎麼去？', r'how (do|can) (i|we|you) get to'),
  ],
  'frames': [
    ('Excuse me. How do I get to ____?', '不好意思，……怎麼去？', 'Excuse me. How do I get to the night market?'),
    ('Go straight for ____ blocks.', '直走……個路口', 'Go straight for two blocks.'),
    ('Turn ____ at ____.', '在……左／右轉', 'Turn left at the convenience store.'),
    ('It is next to / across from ____.', '它在……旁邊／對面', 'It is across from the bank.'),
    ('It takes about ____ minutes on foot.', '走路大約……分鐘', 'It takes about ten minutes on foot.'),
    ('If you get lost, you can ____.', '如果迷路，你可以……', 'If you get lost, you can ask a police officer.'),
  ],
  'write': {
    'prompt': 'Tell a friend how to get from your school to a place you like.',
    'zh': '告訴朋友怎麼從你的學校走到一個你喜歡的地方（例如公園、書店、夜市），並說明那裡有什麼。',
    'qs': [('Where do you want your friend to go? Why?', '要朋友去哪裡？為什麼？'), ('Which way should he or she go?', '怎麼走？'),
           ('What is near the place?', '那附近有什麼？'), ('How long does it take?', '要多久？')],
    'model': {
      1: 'There is a good bookstore near my school. Go out of the school and turn right. '
         'Go straight for two blocks. The bookstore is next to the bank. It takes five minutes on foot.',
      2: 'If you like bubble tea, you should visit Happy Tea near my school. '
         'When you leave the school gate, turn left and go straight until you see a traffic light. '
         'Cross the street and turn right. The shop is on the corner, between a bakery and a bookstore. '
         'It is not far from the school, and it only takes about eight minutes on foot. '
         'If you get lost, just check the map on your phone or call me.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'Go straight. Turn left at the bank. (and)<br>→ {0}', 'blanks': [['Go straight and turn left at the bank.', 'Go straight, and turn left at the bank.']],
     'exp': '兩個祈使句用 and 接。'},
    {'q': 'You will see the park. You turn right. (after)<br>→ {0}', 'blanks': [['After you turn right, you will see the park.', 'You will see the park after you turn right.', "After you turn right, you'll see the park."]],
     'exp': 'after + 先做的事。'},
    {'q': 'The museum is far. Let\'s take a bus. (so)<br>→ {0}', 'blanks': [["The museum is far, so let's take a bus.", "The museum is far so let's take a bus.", 'The museum is far, so let us take a bus.']],
     'exp': '原因, so 結果。'},
    {'q': 'I got lost. I asked a police officer for help. (so)<br>→ {0}', 'blanks': [['I got lost, so I asked a police officer for help.', 'I got lost so I asked a police officer for help.']],
     'exp': '原因, so 結果。'},
    {'q': 'Do you know? Where is the station? (Do you know where …)<br>→ {0}', 'blanks': [['Do you know where the station is?']],
     'exp': '間接問句：Do you know where + 主詞 + 動詞？（不是 where is the station）'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'The bank is next to the school.（針對 next to the school 用 Where 問）<br>→ {0}', 'blanks': [['Where is the bank?', "Where's the bank?"]],
     'exp': 'Where is + 地方？'},
    {'q': 'It takes ten minutes to walk there.（針對 ten minutes 用 How long 問）<br>→ {0}', 'blanks': [['How long does it take to walk there?']],
     'exp': 'How long does it take to + 原形？'},
    {'q': 'Turn left.（改成否定祈使句）<br>→ {0}', 'blanks': [["Don't turn left.", 'Do not turn left.']],
     'exp': "否定的祈使句：Don't + 原形。"},
    {'q': 'The park is near my home.（改成否定句，用 far from）<br>→ {0}', 'blanks': [['The park is not far from my home.', "The park isn't far from my home."]],
     'exp': 'near ＝ not far from。'},
    {'q': 'Where is the post office?（改成更客氣的 Could you tell me 開頭）<br>→ {0}', 'blanks': [['Could you tell me where the post office is?']],
     'exp': '間接問句：where + 主詞 + 動詞。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'get / How / I / do / the / zoo / to<br>→ {0}', 'blanks': [['How do I get to the zoo?']], 'exp': 'How do I get to + 地方？'},
    {'q': 'left / Turn / the / at / light / traffic<br>→ {0}', 'blanks': [['Turn left at the traffic light.']], 'exp': 'Turn left at + 地點。'},
    {'q': 'is / The / across / bank / the / from / store<br>→ {0}', 'blanks': [['The bank is across from the store.', 'The store is across from the bank.']], 'exp': 'across from＝在…對面。'},
    {'q': 'on / is / It / your / right<br>→ {0}', 'blanks': [['It is on your right.']], 'exp': 'on your right＝在你的右手邊。'},
    {'q': 'minutes / It / about / takes / five<br>→ {0}', 'blanks': [['It takes about five minutes.']], 'exp': 'It takes + 時間。'},
  ]},
]
