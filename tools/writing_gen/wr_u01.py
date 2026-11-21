# 寫作園地 Unit 1 My Weekend 我的週末（內容全部自編）
# words：(英文, 中文, 例句, 例句中文, 比對用的關鍵字 regex)；regex 用來檢查短文有沒有用到這個字詞（含過去式）

UNIT = {
  'no': 1, 'en': 'My Weekend', 'zh': '我的週末',
  'intro': '週末做了什麼？先聽、先說，再一步一步寫成一篇短文。',
  'tense': '寫「上個週末」的事情，動詞要用過去式（go → went、eat → ate、sleep → slept）。',
  'dialog': [
    ('Amy', 'Hi, Ben! How was your weekend?'),
    ('Ben', 'It was great! I went hiking with my dad on Saturday.'),
    ('Amy', 'Wow! Where did you go?'),
    ('Ben', 'We went to Yangmingshan. The view was beautiful.'),
    ('Amy', 'That sounds fun. What did you do on Sunday?'),
    ('Ben', 'I stayed home and played video games with my sister. How about you?'),
    ('Amy', 'I helped my mom clean the house, and then we ate hot pot for dinner.'),
    ('Ben', 'Yum! That sounds like a nice weekend.'),
  ],
  'speak': [
    ('What do you usually do on Saturday morning?', '你星期六早上通常做什麼？', 'I usually sleep late. / I usually play basketball.'),
    ('Who do you usually spend your weekend with?', '你週末通常和誰一起過？', 'I spend it with my family. / I spend it with my friends.'),
    ('What did you do last Sunday?', '你上星期天做了什麼？', 'I went to the park. / I watched a movie at home.'),
    ('How did you feel? Why?', '你覺得怎麼樣？為什麼？', 'I felt happy because I didn\'t have to go to school.'),
  ],
  'words': [
    ('weekend', '週末', 'What are you going to do this weekend?', '你這個週末要做什麼？', r'weekends?'),
    ('usually', '通常', 'I usually get up at nine on Sundays.', '我星期天通常九點起床。', r'usually'),
    ('sleep late', '睡晚一點', 'I like to sleep late on Saturdays.', '我星期六喜歡睡晚一點。', r'(sleep|slept|sleeping) late'),
    ('go hiking', '去健行', 'We went hiking in the mountains.', '我們去山上健行。', r'hik(e|ed|ing)'),
    ('go shopping', '去購物', 'Mom and I went shopping at the mall.', '我和媽媽去購物中心買東西。', r'shopping'),
    ('visit my grandparents', '拜訪祖父母', 'I visit my grandparents every Sunday.', '我每個星期天都去看祖父母。', r'grandparents?|grandma|grandpa'),
    ('play video games', '打電動', 'My brother played video games all afternoon.', '我哥哥整個下午都在打電動。', r'video games?'),
    ('watch a movie', '看電影', 'We watched a funny movie at home.', '我們在家看了一部好笑的電影。', r'movies?'),
    ('clean my room', '打掃房間', 'I cleaned my room on Saturday morning.', '我星期六早上打掃了房間。', r'clean(ed|ing|s)?'),
    ('do my homework', '寫功課', 'I did my homework before dinner.', '我在晚餐前寫完了功課。', r'homework'),
    ('take a walk', '散步', 'After dinner, we took a walk in the park.', '晚餐後我們在公園散步。', r'(take|took|taking|takes) a walk'),
    ('eat out', '外食；上館子', 'We ate out at a noodle shop.', '我們去一家麵店吃飯。', r'(eat|ate|eating|eats) out'),
    ('relaxing', '令人放鬆的', 'It was a relaxing weekend.', '那是一個很放鬆的週末。', r'relax(ing|ed)?'),
    ('tired', '累的', 'I was tired after the long hike.', '走了那麼遠的路，我很累。', r'tired'),
  ],
  'frames': [
    ('On Saturday morning, I usually ____.', '星期六早上，我通常……', 'On Saturday morning, I usually sleep late.'),
    ('I like weekends because ____.', '我喜歡週末，因為……', 'I like weekends because I don\'t have to go to school.'),
    ('Last Sunday, I ____ with ____.', '上星期天，我和……一起……', 'Last Sunday, I went shopping with my mom.'),
    ('First, I ____. Then, I ____.', '首先我……，接著我……', 'First, I did my homework. Then, I watched a movie.'),
    ('It was ____, but I felt ____.', '那天很……，但我覺得……', 'It was a busy day, but I felt happy.'),
    ('Next weekend, I want to ____.', '下個週末，我想要……', 'Next weekend, I want to visit my grandparents.'),
  ],
  'write': {
    'prompt': 'Write about your last weekend.',
    'zh': '寫一寫你上個週末做了什麼。',
    'qs': [('When did you get up?', '幾點起床？'), ('Who were you with?', '和誰在一起？'),
           ('Where did you go? What did you do?', '去了哪裡？做了什麼？'), ('How did you feel? Why?', '覺得怎麼樣？為什麼？')],
    'model': {
      1: 'Last weekend was fun. On Saturday, I slept late and did my homework. On Sunday, I went shopping with my mom. '
         'We ate noodles for lunch. I was tired, but I felt happy.',
      2: 'My last weekend was busy but relaxing. On Saturday morning, I got up early and went hiking with my dad. '
         'The air in the mountains was fresh, and the view was beautiful. In the afternoon, I cleaned my room and did my homework. '
         'On Sunday, I visited my grandparents. Grandma cooked a big lunch for us. I was a little tired, '
         'but I really enjoyed my weekend because I spent time with my family.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'I got up late. I missed the bus. (so)<br>→ {0}', 'blanks': [['I got up late, so I missed the bus.', 'I got up late so I missed the bus.']],
     'exp': 'so（所以）放在結果的前面：原因, so 結果。'},
    {'q': 'It was raining. We stayed home. (because)<br>→ {0}', 'blanks': [['We stayed home because it was raining.', 'Because it was raining, we stayed home.', 'Because it was raining we stayed home.']],
     'exp': 'because（因為）放在原因的前面：結果 because 原因。'},
    {'q': 'I finished my homework. Then I watched a movie. (after)<br>→ {0}', 'blanks': [['After I finished my homework, I watched a movie.', 'After I finished my homework I watched a movie.', 'I watched a movie after I finished my homework.']],
     'exp': 'after（在…之後）接先發生的事：After 先做的事, 後做的事。'},
    {'q': 'I wanted to go out. I was too tired. (but)<br>→ {0}', 'blanks': [['I wanted to go out, but I was too tired.', 'I wanted to go out but I was too tired.']],
     'exp': 'but（但是）連接意思相反的兩句。'},
    {'q': 'My dad went hiking. I went hiking, too. (and)<br>→ {0}', 'blanks': [['My dad and I went hiking.', 'My dad went hiking, and I went hiking, too.', 'My dad went hiking and I went hiking too.']],
     'exp': '兩個人做同一件事，可以把主詞合起來：My dad and I went hiking.'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'I play basketball every Saturday.（把 every Saturday 改成 last Saturday）<br>→ {0}', 'blanks': [['I played basketball last Saturday.']],
     'exp': 'last Saturday 是過去的時間，動詞用過去式 played。'},
    {'q': 'She goes shopping with her mom on Sundays.（改成否定句）<br>→ {0}', 'blanks': [['She doesn\'t go shopping with her mom on Sundays.', 'She does not go shopping with her mom on Sundays.']],
     'exp': '第三人稱單數的否定：doesn\'t + 原形動詞（goes → go）。'},
    {'q': 'They visited their grandparents last weekend.（改成 Did 開頭的問句）<br>→ {0}', 'blanks': [['Did they visit their grandparents last weekend?']],
     'exp': 'Did 開頭的問句，後面的動詞要改回原形：visited → visit。'},
    {'q': 'Tom watched a movie on Sunday.（針對 on Sunday 用 When 問）<br>→ {0}', 'blanks': [['When did Tom watch a movie?']],
     'exp': 'When + did + 主詞 + 原形動詞？'},
    {'q': 'I will clean my room tomorrow.（用 be going to 改寫）<br>→ {0}', 'blanks': [['I am going to clean my room tomorrow.', 'I\'m going to clean my room tomorrow.']],
     'exp': 'will + 原形 = be going to + 原形，都表示未來要做的事。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'weekend / How / your / was<br>→ {0}', 'blanks': [['How was your weekend?']], 'exp': '問「週末過得怎樣」：How was your weekend?'},
    {'q': 'late / I / on / sleep / Saturdays / usually<br>→ {0}', 'blanks': [['I usually sleep late on Saturdays.']], 'exp': '頻率副詞 usually 放在一般動詞前面。'},
    {'q': 'with / went / my / We / to / cousins / the beach<br>→ {0}', 'blanks': [['We went to the beach with my cousins.', 'We went with my cousins to the beach.']], 'exp': '主詞 + 動詞 + 地點 + with 人。'},
    {'q': 'fun / was / It / a / day / really<br>→ {0}', 'blanks': [['It was a really fun day.', 'It really was a fun day.']], 'exp': 'a really fun day：really 修飾 fun。'},
    {'q': 'next / do / want / What / you / weekend / do / to<br>→ {0}', 'blanks': [['What do you want to do next weekend?']], 'exp': 'What do you want to do…? 你想要做什麼？'},
  ]},
]
