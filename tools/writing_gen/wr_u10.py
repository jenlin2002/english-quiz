# 寫作園地 Unit 10 A Trip 一次旅行（內容全部自編）

UNIT = {
  'no': 10, 'en': 'A Trip', 'zh': '一次旅行',
  'intro': '寫一次難忘的旅行：去哪裡、跟誰、怎麼去、看到什麼、吃了什麼、發生什麼特別的事。',
  'tense': '寫旅行經驗全部用過去式（We went… / We saw… / It was…）；最後可以用 I hope / I want to… 說以後的計畫。',
  'dialog': [
    ('Amy', 'Where did you go during summer vacation?'),
    ('Ben', 'I went to Hualien with my family. We took the train.'),
    ('Amy', 'How long did you stay there?'),
    ('Ben', 'Three days. We stayed at a hotel near the beach.'),
    ('Amy', 'What did you do?'),
    ('Ben', 'We visited Taroko Gorge and rode bikes along the coast.'),
    ('Amy', 'Sounds amazing! Did anything special happen?'),
    ('Ben', 'Yes! We saw dolphins on a boat trip. I took lots of pictures.'),
  ],
  'speak': [
    ('Where did you go on your last trip?', '你上次旅行去哪裡？', 'I went to Kenting.'),
    ('Who did you go with, and how did you get there?', '跟誰去？怎麼去？', 'I went with my family by car.'),
    ('What did you see or do there?', '在那裡看到什麼、做什麼？', 'We swam in the sea and visited a museum.'),
    ('What was the best part?', '最棒的是什麼？', 'The best part was the night market.'),
  ],
  'words': [
    ('trip', '旅行', 'We took a trip to Tainan.', '我們去台南旅行。', r'trips?|travel(l?ed)?|vacation'),
    ('take the train', '搭火車', 'We took the train to Taitung.', '我們搭火車去台東。', r'(take|took|takes) (the|a) (train|bus|plane|boat|high speed rail|hsr)|by (train|bus|car|plane|boat)'),
    ('stay at', '住在', 'We stayed at a hotel by the sea.', '我們住在海邊的飯店。', r'stay(s|ed)? (at|in)'),
    ('visit', '參觀；拜訪', 'We visited an old temple.', '我們參觀了一座古廟。', r'visit(s|ed|ing)?'),
    ('scenery', '風景', 'The scenery was beautiful.', '風景很美。', r'scenery|view'),
    ('take pictures', '拍照', 'I took pictures of the mountains.', '我拍了山的照片。', r'(take|took|takes|taking) (a lot of |lots of |many )?(pictures|photos)'),
    ('souvenir', '紀念品', 'I bought a souvenir for my friend.', '我買了紀念品給朋友。', r'souvenirs?'),
    ('local food', '當地美食', 'We tried some local food.', '我們吃了一些當地美食。', r'local (food|snacks?)'),
    ('famous', '有名的', 'This beach is famous for its sunset.', '這個海灘以夕陽聞名。', r'famous'),
    ('excited', '興奮的', 'I was excited before the trip.', '旅行前我很興奮。', r'excit(ed|ing)'),
    ('tired', '累的', 'We were tired but happy.', '我們很累但很開心。', r'tired'),
    ('unforgettable', '難忘的', 'It was an unforgettable trip.', '那是一次難忘的旅行。', r'unforgettable|never forget'),
    ('first … then … finally', '首先…然後…最後', 'First, we went to the beach. Finally, we went home.', '首先我們去海邊，最後我們回家。', r'first|then|after that|finally|later'),
    ('weather', '天氣', 'The weather was sunny every day.', '每天都是晴天。', r'weather|sunny|rainy|windy|cloudy'),
  ],
  'frames': [
    ('Last ____, I went to ____ with ____.', '上個……我跟……去了……', 'Last summer, I went to Hualien with my family.'),
    ('We got there by ____.', '我們搭……去', 'We got there by train.'),
    ('We stayed at ____ for ____ days.', '我們住在……，住了……天', 'We stayed at a hotel for three days.'),
    ('First, we ____. Then, we ____.', '首先我們……，然後我們……', 'First, we visited a temple. Then, we ate local food.'),
    ('The best part was ____.', '最棒的是……', 'The best part was the boat trip.'),
    ('I hope I can ____ again.', '我希望能再……', 'I hope I can go there again next year.'),
  ],
  'write': {
    'prompt': 'Write about a trip you took.',
    'zh': '寫一次難忘的旅行：去哪裡、跟誰、做了什麼、最棒的部分、心情。',
    'qs': [('Where and when did you go? Who did you go with?', '什麼時候、去哪裡、跟誰？'), ('How did you get there? Where did you stay?', '怎麼去？住哪裡？'),
           ('What did you do, see, or eat?', '做了什麼、看到什麼、吃了什麼？'), ('What was the best part? How did you feel?', '最棒的是什麼？心情如何？')],
    'model': {
      1: 'Last summer, I went to Kenting with my family. We got there by car. '
         'We swam in the sea and ate local food. The weather was sunny. It was a fun trip.',
      2: 'Last winter vacation, I took a trip to Japan with my parents. We stayed in Osaka for five days. '
         'First, we visited a famous castle and took a lot of pictures. Then, we went to a big market and tried local food. '
         'The best part was a day at a theme park, but we waited in line for a long time. '
         'Every night we were tired, but we were also excited about the next day. '
         'I bought some souvenirs for my classmates. I hope I can go back again someday.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'We went to the beach. We swam in the sea. (and)<br>→ {0}', 'blanks': [['We went to the beach and swam in the sea.', 'We went to the beach, and we swam in the sea.', 'We went to the beach and we swam in the sea.']],
     'exp': '主詞一樣，兩個過去式動詞用 and 接。'},
    {'q': 'It rained. We stayed in the hotel. (because)<br>→ {0}', 'blanks': [['We stayed in the hotel because it rained.', 'Because it rained, we stayed in the hotel.']],
     'exp': '結果 because 原因。'},
    {'q': 'We were tired. We were happy. (but)<br>→ {0}', 'blanks': [['We were tired, but we were happy.', 'We were tired but happy.', 'We were tired but we were happy.']],
     'exp': 'but 接相反的感覺。'},
    {'q': 'We arrived at the hotel. We went out for dinner. (after)<br>→ {0}', 'blanks': [['After we arrived at the hotel, we went out for dinner.', 'We went out for dinner after we arrived at the hotel.']],
     'exp': 'after + 先發生的事。'},
    {'q': 'I saw a beautiful temple. It was built 300 years ago. (which)<br>→ {0}', 'blanks': [['I saw a beautiful temple which was built 300 years ago.', 'I saw a beautiful temple, which was built 300 years ago.']],
     'exp': 'which 代替東西（the temple）。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'I go to Taichung every summer.（把 every summer 改成 last summer）<br>→ {0}', 'blanks': [['I went to Taichung last summer.']],
     'exp': 'go 的過去式是 went。'},
    {'q': 'We stayed there for three days.（針對 for three days 用 How long 問，主詞換成 you）<br>→ {0}', 'blanks': [['How long did you stay there?']],
     'exp': 'How long did + 主詞 + 原形？'},
    {'q': 'They went to Hualien by train.（針對 by train 用 How 問）<br>→ {0}', 'blanks': [['How did they go to Hualien?', 'How did they get to Hualien?']],
     'exp': '問交通方式用 How。'},
    {'q': 'The trip was very interesting.（用 What 改成感嘆句）<br>→ {0}', 'blanks': [['What an interesting trip it was!']],
     'exp': 'What + an + 形容詞 + 名詞 + 主詞 + 動詞！interesting 母音開頭用 an。'},
    {'q': 'I have been to Kenting.（改成否定句）<br>→ {0}', 'blanks': [["I haven't been to Kenting.", 'I have not been to Kenting.', 'I have never been to Kenting.']],
     'exp': "現在完成式否定：haven't + p.p.。"},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'trip / We / a / took / Yilan / to<br>→ {0}', 'blanks': [['We took a trip to Yilan.']], 'exp': 'take a trip to + 地方。'},
    {'q': 'part / The / was / best / the / boat / ride<br>→ {0}', 'blanks': [['The best part was the boat ride.']], 'exp': 'The best part was…＝最棒的部分是…。'},
    {'q': 'is / for / famous / Tainan / its / food<br>→ {0}', 'blanks': [['Tainan is famous for its food.']], 'exp': 'be famous for＝以…聞名。'},
    {'q': 'lot / of / I / a / took / pictures<br>→ {0}', 'blanks': [['I took a lot of pictures.']], 'exp': 'a lot of＝很多。'},
    {'q': 'can / hope / I / I / go / again / there<br>→ {0}', 'blanks': [['I hope I can go there again.']], 'exp': 'I hope + 子句。'},
  ]},
]
