# 寫作園地 Unit 7 Going Shopping 去買東西（內容全部自編）

UNIT = {
  'no': 7, 'en': 'Going Shopping', 'zh': '去買東西',
  'intro': '寫一次買東西的經驗：去哪裡、跟誰、想買什麼、價錢、最後買了沒有、心情如何。',
  'tense': '寫一次買東西的經驗用過去式（I went… / It cost… / I bought…）。',
  'dialog': [
    ('Amy', 'Excuse me. How much is this T-shirt?'),
    ('Ben', 'It\'s three hundred dollars. It\'s on sale today.'),
    ('Amy', 'Do you have it in a smaller size?'),
    ('Ben', 'Yes, here you are. The fitting room is over there.'),
    ('Amy', 'Thanks. Hmm, it fits well. Do you have it in blue?'),
    ('Ben', 'Sorry, we only have white and black.'),
    ('Amy', 'OK, I\'ll take the black one. Can I pay by card?'),
    ('Ben', 'Sure. Here\'s your receipt. Have a nice day!'),
  ],
  'speak': [
    ('Where do you usually go shopping?', '你通常去哪裡買東西？', 'I usually go to the department store.'),
    ('What did you buy last time?', '你上次買了什麼？', 'I bought a pair of shoes.'),
    ('How much was it?', '多少錢？', 'It was eight hundred dollars.'),
    ('Do you like shopping? Why?', '你喜歡逛街嗎？為什麼？', 'Yes, because I like to look at new things.'),
  ],
  'words': [
    ('go shopping', '去購物', 'We go shopping on Saturdays.', '我們星期六去購物。', r'(go|goes|went) shopping|shop(ping|ped)?'),
    ('How much', '多少錢', 'How much is this cap?', '這頂帽子多少錢？', r'how much'),
    ('cost', '花費', 'The shoes cost one thousand dollars.', '這雙鞋要一千元。', r'costs?'),
    ('price', '價格', 'The price is too high.', '價格太高了。', r'prices?'),
    ('cheap', '便宜的', 'This bag is cheap.', '這個包包很便宜。', r'cheap(er)?'),
    ('expensive', '貴的', 'That phone is too expensive.', '那支手機太貴了。', r'expensive'),
    ('on sale', '特價', 'Everything is on sale today.', '今天全部都在特價。', r'on sale|sale'),
    ('size', '尺寸', 'Do you have a larger size?', '有大一點的尺寸嗎？', r'sizes?'),
    ('try on', '試穿', 'Can I try on these jeans?', '我可以試穿這條牛仔褲嗎？', r'(try|tried|tries) (it |them )?on'),
    ('fit', '合身', 'The jacket fits me well.', '這件外套很合身。', r'fits?'),
    ('pay', '付錢', 'I paid in cash.', '我付現金。', r'pa(y|ys|id)'),
    ('buy', '買', 'I bought a gift for my mom.', '我買了禮物給媽媽。', r'buy(s|ing)?|bought'),
    ('spend', '花（錢）', 'I spent five hundred dollars.', '我花了五百元。', r'spen(d|ds|t)'),
    ('department store', '百貨公司', 'The department store is crowded.', '百貨公司人很多。', r'(department store|mall|market|shop|store)s?'),
  ],
  'frames': [
    ('Last ____, I went shopping at ____.', '上個……我去……買東西', 'Last Sunday, I went shopping at the mall.'),
    ('I went with ____.', '我跟……一起去', 'I went with my mom and sister.'),
    ('I wanted to buy ____.', '我想買……', 'I wanted to buy a new pair of sneakers.'),
    ('It cost ____ dollars.', '它要……元', 'It cost nine hundred dollars.'),
    ('It was ____, so I ____.', '它很……，所以我……', 'It was on sale, so I bought two.'),
    ('I spent ____ in total.', '我總共花了……', 'I spent one thousand two hundred dollars in total.'),
  ],
  'write': {
    'prompt': 'Write about a shopping trip.',
    'zh': '寫一次去買東西的經驗：去哪裡、跟誰、買了什麼、花多少錢、心情如何。',
    'qs': [('Where and when did you go shopping?', '什麼時候、去哪裡買東西？'), ('Who did you go with?', '跟誰去？'),
           ('What did you buy? How much was it?', '買了什麼？多少錢？'), ('Were you happy with it? Why?', '你滿意嗎？為什麼？')],
    'model': {
      1: 'Last Saturday, I went shopping with my mom. We went to the night market. '
         'I bought a cap. It cost two hundred dollars. It was cheap, and I like it.',
      2: 'Last weekend, I went to the department store with my sister to buy new sneakers. '
         'There were many nice shoes, but most of them were too expensive. '
         'Finally, we found a pair that was on sale. I tried them on, and they fit me well. '
         'They cost only nine hundred dollars, so I paid with my own money. '
         'I also spent one hundred dollars on bubble tea. I was tired, but I was happy with my new shoes.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'The bag was cheap. I bought it. (so)<br>→ {0}', 'blanks': [['The bag was cheap, so I bought it.', 'The bag was cheap so I bought it.']],
     'exp': '原因, so 結果。'},
    {'q': 'I liked the jacket. It was too big. (but)<br>→ {0}', 'blanks': [['I liked the jacket, but it was too big.', 'I liked the jacket but it was too big.']],
     'exp': 'but 接相反的兩句。'},
    {'q': 'I didn\'t buy the phone. It was too expensive. (because)<br>→ {0}', 'blanks': [["I didn't buy the phone because it was too expensive.", 'I did not buy the phone because it was too expensive.', "Because it was too expensive, I didn't buy the phone."]],
     'exp': '結果 because 原因。'},
    {'q': 'I tried on the shoes. Then I paid for them. (before)<br>→ {0}', 'blanks': [['I tried on the shoes before I paid for them.', 'Before I paid for the shoes, I tried them on.', 'Before I paid for them, I tried on the shoes.']],
     'exp': 'before + 後發生的事。'},
    {'q': 'This shirt is cheap. That shirt is cheaper. (than)<br>→ {0}', 'blanks': [['That shirt is cheaper than this shirt.', 'That shirt is cheaper than this one.', 'That shirt is cheaper than this.']],
     'exp': '比較級 + than。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'The hat costs two hundred dollars.（針對 two hundred dollars 用 How much 問）<br>→ {0}', 'blanks': [['How much does the hat cost?', 'How much is the hat?']],
     'exp': 'How much does + 主詞 + cost？'},
    {'q': 'I bought a new watch.（改成否定句）<br>→ {0}', 'blanks': [["I didn't buy a new watch.", 'I did not buy a new watch.']],
     'exp': "didn't + 原形 buy。"},
    {'q': 'These jeans are expensive.（用 too 改寫：These jeans are … for me.）<br>→ {0}', 'blanks': [['These jeans are too expensive for me.']],
     'exp': 'too + 形容詞＝太…。'},
    {'q': 'She spent three hundred dollars on a book.（改成 It cost her … 開頭）<br>→ {0}', 'blanks': [['It cost her three hundred dollars to buy a book.', 'It cost her three hundred dollars to buy the book.']],
     'exp': '人 spend 錢 on 東西 ＝ It cost 人 錢 to 原形。'},
    {'q': 'Can I try on this dress?（換成 Could 讓語氣更客氣）<br>→ {0}', 'blanks': [['Could I try on this dress?', 'Could I try this dress on?']],
     'exp': 'Could I…? 比 Can I…? 更有禮貌。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'much / How / these / are / shoes<br>→ {0}', 'blanks': [['How much are these shoes?']], 'exp': 'How much are + 複數名詞？'},
    {'q': 'it / smaller / Do / have / in / a / you / size<br>→ {0}', 'blanks': [['Do you have it in a smaller size?']], 'exp': 'have it in a … size＝有…尺寸。'},
    {'q': 'sale / is / on / Everything / today<br>→ {0}', 'blanks': [['Everything is on sale today.']], 'exp': 'on sale＝特價中。'},
    {'q': 'well / The / me / fits / jacket<br>→ {0}', 'blanks': [['The jacket fits me well.']], 'exp': 'fit + 人＝合身。'},
    {'q': 'card / pay / I / Can / by / credit<br>→ {0}', 'blanks': [['Can I pay by credit card?']], 'exp': 'pay by card／in cash。'},
  ]},
]
