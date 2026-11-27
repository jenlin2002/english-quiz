# 寫作園地 Unit 6 A Birthday Party 生日派對（內容全部自編）

UNIT = {
  'no': 6, 'en': 'A Birthday Party', 'zh': '生日派對',
  'intro': '寫一場你參加過或辦過的生日派對：誰的生日、在哪裡、有誰來、做了什麼、收到或送了什麼禮物。',
  'tense': '寫已經發生的派對全部用過去式（It was… / We ate… / I got…）。',
  'dialog': [
    ('Amy', 'How was your birthday party last Saturday?'),
    ('Ben', 'It was great! We had it at a pizza restaurant.'),
    ('Amy', 'Who came?'),
    ('Ben', 'Eight of my friends and my cousins. We played games and sang songs.'),
    ('Amy', 'Did you get any nice presents?'),
    ('Ben', 'Yes! My parents gave me a new basketball, and my friends gave me some comic books.'),
    ('Amy', 'What kind of cake did you have?'),
    ('Ben', 'A chocolate cake with thirteen candles. I made a wish and blew them out.'),
  ],
  'speak': [
    ('When is your birthday?', '你的生日是什麼時候？', 'My birthday is on May 3rd.'),
    ('How did you celebrate your last birthday?', '你上次生日怎麼慶祝？', 'I had dinner with my family.'),
    ('What presents did you get?', '你收到什麼禮物？', 'I got a new watch.'),
    ('What did you wish for?', '你許了什麼願？', 'I wished for good grades. / It\'s a secret!'),
  ],
  'words': [
    ('birthday party', '生日派對', 'I went to Amy\'s birthday party.', '我去了 Amy 的生日派對。', r'birthday( party)?'),
    ('celebrate', '慶祝', 'We celebrated at home.', '我們在家慶祝。', r'celebrat(e|es|ed|ing)'),
    ('invite', '邀請', 'She invited ten friends.', '她邀請了十個朋友。', r'invit(e|es|ed|ing)'),
    ('guest', '客人', 'The guests arrived at six.', '客人六點到。', r'guests?'),
    ('present', '禮物', 'I got a lot of presents.', '我收到很多禮物。', r'presents?|gifts?'),
    ('candle', '蠟燭', 'There were twelve candles on the cake.', '蛋糕上有十二根蠟燭。', r'candles?'),
    ('make a wish', '許願', 'Close your eyes and make a wish.', '閉上眼睛許個願。', r'(make|made|makes) a wish|wish(ed)?'),
    ('blow out', '吹熄', 'He blew out the candles.', '他吹熄了蠟燭。', r'(blow|blew|blows) out'),
    ('decorate', '裝飾', 'We decorated the room with balloons.', '我們用氣球裝飾房間。', r'decorat(e|es|ed|ing)'),
    ('balloon', '氣球', 'There were colorful balloons everywhere.', '到處都是彩色氣球。', r'balloons?'),
    ('surprise', '驚喜', 'The party was a surprise for my mom.', '這個派對是給我媽媽的驚喜。', r'surprised?'),
    ('have fun', '玩得開心', 'Everyone had fun at the party.', '大家在派對上都玩得很開心。', r'(have|had|has) (a lot of |so much )?fun'),
    ('sing', '唱歌', 'We sang "Happy Birthday" together.', '我們一起唱生日快樂歌。', r'sing|sang|sung'),
    ('wrap', '包裝', 'I wrapped the present in red paper.', '我用紅色的紙包禮物。', r'wrap(s|ped|ping)?'),
  ],
  'frames': [
    ('Last ____, I went to ____\'s birthday party.', '上個……，我去了……的生日派對', 'Last Sunday, I went to my cousin\'s birthday party.'),
    ('The party was at ____.', '派對在……舉行', 'The party was at her house.'),
    ('We ____ and ____.', '我們……還有……', 'We played games and ate pizza.'),
    ('I gave him / her ____.', '我送他／她……', 'I gave her a storybook.'),
    ('The cake was ____.', '蛋糕是……的', 'The cake was big and full of strawberries.'),
    ('It was a ____ day because ____.', '那是……的一天，因為……', 'It was a happy day because all my friends were there.'),
  ],
  'write': {
    'prompt': 'Write about a birthday party you went to or had.',
    'zh': '寫一場你參加過或自己辦過的生日派對：在哪裡、有誰、做了什麼、心情如何。',
    'qs': [('Whose birthday party was it? When and where was it?', '誰的生日？什麼時候、在哪裡？'), ('Who came to the party?', '誰來了？'),
           ('What did you do and eat?', '做了什麼、吃了什麼？'), ('How did you feel?', '你覺得怎麼樣？')],
    'model': {
      1: 'Last Saturday, I went to Amy\'s birthday party. The party was at her house. '
         'We ate cake and played games. I gave her a book. We had a lot of fun.',
      2: 'Last month, my family had a surprise party for my mom\'s fortieth birthday. '
         'My sister and I decorated the living room with balloons while Mom was at work. '
         'We also invited her best friends. When she opened the door, everyone shouted, "Surprise!" '
         'She was so happy that she almost cried. After dinner, she made a wish and blew out the candles. '
         'I gave her a card that I made myself. It was the best party ever.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'We ate pizza. We played games. (and)<br>→ {0}', 'blanks': [['We ate pizza and played games.', 'We ate pizza, and we played games.', 'We ate pizza and we played games.']],
     'exp': '主詞一樣，兩個動作用 and 接。'},
    {'q': 'She opened the present. She smiled. (when)<br>→ {0}', 'blanks': [['When she opened the present, she smiled.', 'She smiled when she opened the present.']],
     'exp': 'when 帶出「…的時候」。放句首要加逗號。'},
    {'q': 'I wanted to go to the party. I was sick. (but)<br>→ {0}', 'blanks': [['I wanted to go to the party, but I was sick.', 'I wanted to go to the party but I was sick.']],
     'exp': 'but 接相反的兩句。'},
    {'q': 'The party was fun. Nobody wanted to go home. (so … that …)<br>→ {0}', 'blanks': [['The party was so fun that nobody wanted to go home.', 'The party was so much fun that nobody wanted to go home.']],
     'exp': 'so + 形容詞 + that + 結果＝太…以致於…。'},
    {'q': 'This is the card. I made it for my mom. (that)<br>→ {0}', 'blanks': [['This is the card that I made for my mom.']],
     'exp': 'that 代替 it（the card），後面不要再寫 it。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'We have a party every year.（把 every year 改成 last year）<br>→ {0}', 'blanks': [['We had a party last year.']],
     'exp': 'have 的過去式是 had。'},
    {'q': 'She got a new bike for her birthday.（改成 Did 開頭的問句）<br>→ {0}', 'blanks': [['Did she get a new bike for her birthday?']],
     'exp': 'Did + 主詞 + 原形：got → get。'},
    {'q': 'My birthday is on June 5th.（針對 on June 5th 用 When 問）<br>→ {0}', 'blanks': [['When is your birthday?', "When's your birthday?"]],
     'exp': 'When is + 名詞？my → your。'},
    {'q': 'Ben blew out the candles.（改成否定句）<br>→ {0}', 'blanks': [["Ben didn't blow out the candles.", 'Ben did not blow out the candles.']],
     'exp': "didn't + 原形 blow。"},
    {'q': 'Let\'s sing a song for her.（改成 How about 開頭）<br>→ {0}', 'blanks': [['How about singing a song for her?']],
     'exp': 'How about + V-ing？'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'wish / a / Make / blow / and / the / out / candles<br>→ {0}', 'blanks': [['Make a wish and blow out the candles.']], 'exp': '祈使句：動詞原形開頭。'},
    {'q': 'party / invited / She / to / me / her<br>→ {0}', 'blanks': [['She invited me to her party.']], 'exp': 'invite 人 to 活動。'},
    {'q': 'the / with / We / room / balloons / decorated<br>→ {0}', 'blanks': [['We decorated the room with balloons.']], 'exp': 'decorate A with B。'},
    {'q': 'you / for / Thank / the / present / lovely<br>→ {0}', 'blanks': [['Thank you for the lovely present.']], 'exp': 'Thank you for + 東西。'},
    {'q': 'fun / Everyone / a / of / had / lot<br>→ {0}', 'blanks': [['Everyone had a lot of fun.']], 'exp': 'have a lot of fun＝玩得很開心。'},
  ]},
]
