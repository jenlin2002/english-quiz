# 寫作園地 Unit 5 My Favorite Food 我最喜歡的食物（內容全部自編）

UNIT = {
  'no': 5, 'en': 'My Favorite Food', 'zh': '我最喜歡的食物',
  'intro': '介紹你最喜歡的食物：它是什麼、吃起來怎樣、在哪裡吃、跟誰吃、為什麼喜歡。',
  'tense': '介紹食物用現在式（It tastes… / I often eat…）；說「第一次吃」的經驗用過去式（I first ate it…）。',
  'dialog': [
    ('Amy', 'What\'s your favorite food?'),
    ('Ben', 'Beef noodles! My grandpa makes the best beef noodles.'),
    ('Amy', 'What does it taste like?'),
    ('Ben', 'The soup is rich and a little spicy, and the beef is soft.'),
    ('Amy', 'Sounds delicious. How often do you eat it?'),
    ('Ben', 'About once a week. What about you?'),
    ('Amy', 'I love mango shaved ice. It\'s sweet and cold.'),
    ('Ben', 'That\'s perfect for hot summer days!'),
  ],
  'speak': [
    ('What is your favorite food?', '你最喜歡的食物是什麼？', 'My favorite food is fried rice.'),
    ('What does it taste like?', '吃起來怎麼樣？', 'It is salty and a little sweet.'),
    ('Where and with whom do you eat it?', '在哪裡、跟誰吃？', 'I eat it at home with my family.'),
    ('Why do you like it?', '為什麼喜歡？', 'Because it is cheap and delicious.'),
  ],
  'words': [
    ('favorite', '最喜歡的', 'Dumplings are my favorite food.', '餃子是我最喜歡的食物。', r'favou?rite'),
    ('delicious', '美味的', 'This cake is delicious.', '這個蛋糕很好吃。', r'delicious|yummy|tasty'),
    ('taste', '嚐起來', 'The soup tastes a little salty.', '這湯嚐起來有點鹹。', r'tastes?|tasted'),
    ('sweet', '甜的', 'Bubble tea is too sweet for me.', '珍奶對我來說太甜了。', r'sweet'),
    ('spicy', '辣的', 'I can\'t eat spicy food.', '我不能吃辣。', r'spicy|hot'),
    ('sour', '酸的', 'Lemons are sour.', '檸檬是酸的。', r'sour'),
    ('salty', '鹹的', 'The fries are salty.', '薯條很鹹。', r'salty'),
    ('smell', '聞起來', 'The bread smells good.', '麵包聞起來很香。', r'smells?|smelled'),
    ('night market', '夜市', 'We eat fried chicken at the night market.', '我們在夜市吃炸雞。', r'night markets?'),
    ('restaurant', '餐廳', 'There is a good noodle restaurant near my home.', '我家附近有一家好吃的麵店。', r'restaurants?'),
    ('cook', '煮；廚師', 'My dad cooks dinner on Sundays.', '我爸爸星期天煮晚餐。', r'cook(s|ed|ing)?'),
    ('healthy', '健康的', 'Vegetables are healthy.', '蔬菜很健康。', r'healthy'),
    ('be full', '吃飽的', 'I can\'t eat any more. I\'m full.', '我吃不下了，我飽了。', r'full'),
    ('once a week', '一週一次', 'I eat hot pot once a week.', '我一週吃一次火鍋。', r'(once|twice|three times) a (week|month|day)'),
  ],
  'frames': [
    ('My favorite food is ____.', '我最喜歡的食物是……', 'My favorite food is beef noodles.'),
    ('It tastes ____ and ____.', '它吃起來……又……', 'It tastes sweet and sour.'),
    ('I usually eat it at ____ with ____.', '我通常在……跟……一起吃', 'I usually eat it at the night market with my friends.'),
    ('I eat it about ____.', '我大約多久吃一次', 'I eat it about once a week.'),
    ('I like it because ____.', '我喜歡它是因為……', 'I like it because it reminds me of my grandma.'),
    ('If you come to Taiwan, you should try ____.', '如果你來台灣，你應該試試……', 'If you come to Taiwan, you should try stinky tofu.'),
  ],
  'write': {
    'prompt': 'Write about your favorite food.',
    'zh': '介紹你最喜歡的食物：它的味道、在哪裡吃、跟誰吃、為什麼喜歡。',
    'qs': [('What is your favorite food?', '最喜歡的食物是什麼？'), ('What does it look and taste like?', '看起來、吃起來怎樣？'),
           ('Where and how often do you eat it?', '在哪裡吃？多久吃一次？'), ('Why do you like it?', '為什麼喜歡？')],
    'model': {
      1: 'My favorite food is fried chicken. It is hot and salty. I eat it at the night market with my friends. '
         'I eat it about once a month. It is delicious!',
      2: 'My favorite food is my mom\'s beef noodle soup. The soup smells wonderful, and the beef is soft and a little spicy. '
         'My mom cooks it every Sunday, so the whole family eats together. '
         'I usually eat two bowls because it is so delicious. After dinner, I am always full and happy. '
         'It is not very healthy to eat too much, but I can\'t stop. '
         'If you come to my house, you should try it!',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'The cake is sweet. The cake is soft. (and)<br>→ {0}', 'blanks': [['The cake is sweet and soft.']],
     'exp': '主詞一樣，兩個形容詞用 and 接。'},
    {'q': 'I like spicy food. My sister doesn\'t like it. (but)<br>→ {0}', 'blanks': [["I like spicy food, but my sister doesn't like it.", "I like spicy food but my sister doesn't like it.", 'I like spicy food, but my sister does not like it.']],
     'exp': 'but 接意思相反的兩句。'},
    {'q': 'I was hungry. I ate two bowls of rice. (so)<br>→ {0}', 'blanks': [['I was hungry, so I ate two bowls of rice.', 'I was hungry so I ate two bowls of rice.']],
     'exp': '原因, so 結果。'},
    {'q': 'This is the restaurant. We often eat dumplings there. (where)<br>→ {0}', 'blanks': [['This is the restaurant where we often eat dumplings.']],
     'exp': 'where 代替地點 there：the restaurant where…。'},
    {'q': 'Vegetables are healthy. You should eat more of them. (because)<br>→ {0}', 'blanks': [['You should eat more vegetables because they are healthy.', "You should eat more vegetables because they're healthy.", 'Because vegetables are healthy, you should eat more of them.']],
     'exp': '結果 because 原因；把 them 換回 vegetables 句子比較清楚。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'The soup tastes good.（改成 Does 開頭的問句）<br>→ {0}', 'blanks': [['Does the soup taste good?']],
     'exp': 'Does + 主詞 + 原形：tastes → taste。'},
    {'q': 'I eat hot pot once a week.（針對 once a week 用 How often 問）<br>→ {0}', 'blanks': [['How often do you eat hot pot?']],
     'exp': 'How often 問頻率。'},
    {'q': 'This noodle shop is good. That noodle shop is better.（用 better than 合成一句：That noodle shop …）<br>→ {0}', 'blanks': [['That noodle shop is better than this noodle shop.', 'That noodle shop is better than this one.', 'That noodle shop is better than this.']],
     'exp': 'A is better than B。'},
    {'q': 'My dad cooked dinner last night.（改成否定句）<br>→ {0}', 'blanks': [["My dad didn't cook dinner last night.", 'My dad did not cook dinner last night.']],
     'exp': 'didn\'t + 原形 cook。'},
    {'q': 'The mango ice is very sweet.（用 How 改成感嘆句）<br>→ {0}', 'blanks': [['How sweet the mango ice is!']],
     'exp': 'How + 形容詞 + 主詞 + 動詞！'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'food / is / favorite / My / dumplings<br>→ {0}', 'blanks': [['My favorite food is dumplings.']], 'exp': 'My favorite food is ＋食物。'},
    {'q': 'smells / bread / The / good / really<br>→ {0}', 'blanks': [['The bread smells really good.', 'The bread really smells good.']], 'exp': 'smell + 形容詞（不是副詞）。'},
    {'q': 'eat / can\'t / I / food / spicy<br>→ {0}', 'blanks': [["I can't eat spicy food."]], 'exp': "can't + 原形動詞。"},
    {'q': 'try / You / should / tofu / stinky<br>→ {0}', 'blanks': [['You should try stinky tofu.']], 'exp': 'should + 原形動詞。'},
    {'q': 'full / I\'m / too / to / eat / dessert<br>→ {0}', 'blanks': [["I'm too full to eat dessert."]], 'exp': 'too + 形容詞 + to + 原形＝太…而不能…。'},
  ]},
]
