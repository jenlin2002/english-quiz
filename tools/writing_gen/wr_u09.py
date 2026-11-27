# 寫作園地 Unit 9 Holidays in Taiwan 臺灣的節日（內容全部自編）

UNIT = {
  'no': 9, 'en': 'Holidays in Taiwan', 'zh': '臺灣的節日',
  'intro': '向外國朋友介紹一個臺灣的節日：什麼時候、大家做什麼、吃什麼、你家怎麼過。',
  'tense': '介紹節日的習俗用現在式（People eat… / We usually…）；寫今年怎麼過可以用過去式。',
  'dialog': [
    ('Amy', 'What\'s the most important holiday in Taiwan?'),
    ('Ben', 'Chinese New Year. It\'s usually in January or February.'),
    ('Amy', 'What do people do?'),
    ('Ben', 'Families get together and eat a big dinner on New Year\'s Eve.'),
    ('Amy', 'Do children get presents?'),
    ('Ben', 'We get red envelopes with money inside. That\'s my favorite part!'),
    ('Amy', 'What other holidays do you have?'),
    ('Ben', 'The Moon Festival. We eat mooncakes and have barbecues with our neighbors.'),
  ],
  'speak': [
    ('What is your favorite holiday?', '你最喜歡哪個節日？', 'My favorite holiday is Chinese New Year.'),
    ('When is it?', '是什麼時候？', 'It is in January or February.'),
    ('What do people eat?', '大家吃什麼？', 'People eat rice dumplings. / People eat mooncakes.'),
    ('What does your family do?', '你家做什麼？', 'We visit my grandparents and play cards.'),
  ],
  'words': [
    ('holiday', '節日；假日', 'Chinese New Year is a long holiday.', '農曆新年是很長的假期。', r'holidays?'),
    ('festival', '節慶', 'The Lantern Festival is very beautiful.', '元宵節很漂亮。', r'festivals?'),
    ('Chinese New Year', '農曆新年', 'We clean the house before Chinese New Year.', '過年前我們大掃除。', r'(chinese|lunar) new year'),
    ('New Year\'s Eve', '除夕', 'We eat a big dinner on New Year\'s Eve.', '除夕我們吃年夜飯。', r"new year'?s eve"),
    ('red envelope', '紅包', 'Grandma gave me a red envelope.', '奶奶給我一個紅包。', r'red (envelopes?|packets?)'),
    ('lantern', '燈籠', 'Children carry lanterns at night.', '孩子們晚上提燈籠。', r'lanterns?'),
    ('mooncake', '月餅', 'Mooncakes are sweet and heavy.', '月餅又甜又紮實。', r'moon ?cakes?'),
    ('rice dumpling', '粽子', 'We eat rice dumplings at the Dragon Boat Festival.', '端午節我們吃粽子。', r'rice dumplings?|zongzi'),
    ('dragon boat race', '龍舟賽', 'We watched a dragon boat race.', '我們看了龍舟賽。', r'dragon boats?'),
    ('get together', '團聚', 'Families get together for dinner.', '家人團聚吃晚餐。', r'(get|gets|got) together|reunion'),
    ('fireworks', '煙火', 'The fireworks were amazing.', '煙火好壯觀。', r'fireworks?|firecrackers?'),
    ('tradition', '傳統', 'It is a Taiwanese tradition.', '這是臺灣的傳統。', r'traditions?|traditional'),
    ('wish', '祝福；願望', 'We wish everyone good luck.', '我們祝大家好運。', r'wish(es|ed)?'),
    ('barbecue', '烤肉', 'We have a barbecue at the Moon Festival.', '中秋節我們烤肉。', r'barbecues?|bbq'),
  ],
  'frames': [
    ('My favorite holiday is ____.', '我最喜歡的節日是……', 'My favorite holiday is the Moon Festival.'),
    ('It is in ____.', '它在……（月份）', 'It is in September or October.'),
    ('On this holiday, people ____.', '這個節日大家會……', 'On this holiday, people look at the moon.'),
    ('We eat ____ because ____.', '我們吃……，因為……', 'We eat rice dumplings because it is a tradition.'),
    ('My family usually ____.', '我家通常……', 'My family usually has a barbecue with our neighbors.'),
    ('I like this holiday because ____.', '我喜歡這個節日，因為……', 'I like this holiday because I can see all my cousins.'),
  ],
  'write': {
    'prompt': 'Introduce a holiday in Taiwan to a foreign friend.',
    'zh': '向外國朋友介紹一個臺灣的節日：什麼時候、大家做什麼、吃什麼，還有你家怎麼過。',
    'qs': [('What is the holiday? When is it?', '什麼節日？什麼時候？'), ('What do people do and eat?', '大家做什麼、吃什麼？'),
           ('What does your family do?', '你家怎麼過？'), ('Why do you like it?', '你為什麼喜歡？')],
    'model': {
      1: 'My favorite holiday is Chinese New Year. It is in January or February. '
         'My family gets together and eats a big dinner. I get red envelopes. I love this holiday.',
      2: 'The Dragon Boat Festival is a traditional holiday in Taiwan. It is usually in June. '
         'On this day, people eat rice dumplings and watch dragon boat races on the river. '
         'My grandma makes rice dumplings with pork and mushrooms, and they are delicious. '
         'Last year, my family went to Yilan to watch a race, and the boats were very fast. '
         'I like this holiday because the weather is hot, so it is a good time for a short trip.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'We eat mooncakes. We look at the moon. (and)<br>→ {0}', 'blanks': [['We eat mooncakes and look at the moon.', 'We eat mooncakes, and we look at the moon.', 'We eat mooncakes and we look at the moon.']],
     'exp': '主詞一樣，兩個動作用 and 接。'},
    {'q': 'Chinese New Year is coming. We clean the house. (before)<br>→ {0}', 'blanks': [['We clean the house before Chinese New Year comes.', 'Before Chinese New Year comes, we clean the house.', 'We clean the house before Chinese New Year.']],
     'exp': 'before + 後發生的事。'},
    {'q': 'I love the Lantern Festival. The lanterns are beautiful. (because)<br>→ {0}', 'blanks': [['I love the Lantern Festival because the lanterns are beautiful.', 'Because the lanterns are beautiful, I love the Lantern Festival.']],
     'exp': '結果 because 原因。'},
    {'q': 'The fireworks were loud. The baby started to cry. (so)<br>→ {0}', 'blanks': [['The fireworks were loud, so the baby started to cry.', 'The fireworks were loud so the baby started to cry.']],
     'exp': '原因, so 結果。'},
    {'q': 'The Moon Festival comes. We have a barbecue with our neighbors. (When)<br>→ {0}', 'blanks': [['When the Moon Festival comes, we have a barbecue with our neighbors.', 'We have a barbecue with our neighbors when the Moon Festival comes.']],
     'exp': 'When + 子句, 主要子句。When 放句首要加逗號。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'People eat mooncakes at the Moon Festival.（針對 mooncakes 用 What 問）<br>→ {0}', 'blanks': [['What do people eat at the Moon Festival?']],
     'exp': 'What do + 主詞 + 原形？'},
    {'q': 'We watched the fireworks last night.（改成 Did 開頭的問句，主詞換成 you）<br>→ {0}', 'blanks': [['Did you watch the fireworks last night?']],
     'exp': 'Did + 主詞 + 原形 watch。'},
    {'q': 'My aunt gives me a red envelope every year.（改成 My aunt gives a red envelope … 的說法）<br>→ {0}', 'blanks': [['My aunt gives a red envelope to me every year.']],
     'exp': 'give 人 東西 ＝ give 東西 to 人。'},
    {'q': 'The Lantern Festival is beautiful.（用 How 改成感嘆句）<br>→ {0}', 'blanks': [['How beautiful the Lantern Festival is!']],
     'exp': 'How + 形容詞 + 主詞 + 動詞！'},
    {'q': 'We will visit Grandpa during the holiday.（改成 be going to）<br>→ {0}', 'blanks': [['We are going to visit Grandpa during the holiday.', "We're going to visit Grandpa during the holiday."]],
     'exp': 'will ＝ be going to + 原形。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'get / Families / together / New Year\'s Eve / on<br>→ {0}', 'blanks': [["Families get together on New Year's Eve."]], 'exp': 'get together＝團聚。'},
    {'q': 'is / favorite / Which / your / holiday<br>→ {0}', 'blanks': [['Which is your favorite holiday?', 'Which holiday is your favorite?']], 'exp': 'Which + 名詞／Which is…？'},
    {'q': 'eat / We / dumplings / rice / in / June<br>→ {0}', 'blanks': [['We eat rice dumplings in June.']], 'exp': '月份前面用 in。'},
    {'q': 'a / It / tradition / is / Taiwanese<br>→ {0}', 'blanks': [['It is a Taiwanese tradition.']], 'exp': 'a + 形容詞 + 名詞。'},
    {'q': 'you / I / a / wish / happy / New Year<br>→ {0}', 'blanks': [['I wish you a happy New Year.']], 'exp': 'wish + 人 + 祝福＝祝某人…。'},
  ]},
]
