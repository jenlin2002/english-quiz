# 寫作園地 Unit 11 My Dream 我的夢想（內容全部自編）

UNIT = {
  'no': 11, 'en': 'My Dream', 'zh': '我的夢想',
  'intro': '寫你的夢想：長大想做什麼工作、想去哪裡、想完成什麼事，為什麼，以及你現在怎麼努力。',
  'tense': '說夢想用 I want to be… / I hope to… / I would like to…；說將來的事用 will；說現在怎麼努力用現在式。',
  'dialog': [
    ('Amy', 'What do you want to be in the future?'),
    ('Ben', 'I want to be a game designer.'),
    ('Amy', 'Why?'),
    ('Ben', 'Because I love games, and I want to make people happy.'),
    ('Amy', 'What are you doing now to reach your dream?'),
    ('Ben', 'I\'m learning to code, and I draw characters in my free time.'),
    ('Amy', 'That\'s cool. My dream is to be a doctor and help sick children.'),
    ('Ben', 'You\'re good at science, so I\'m sure you can do it!'),
  ],
  'speak': [
    ('What do you want to be in the future?', '你將來想做什麼？', 'I want to be a teacher.'),
    ('Why do you want to do that?', '為什麼？', 'Because I like to help others.'),
    ('What do you need to learn?', '你需要學什麼？', 'I need to learn English and science.'),
    ('What are you doing now for your dream?', '你現在為夢想做什麼？', 'I study hard and read a lot of books.'),
  ],
  'words': [
    ('dream', '夢想', 'My dream is to travel around the world.', '我的夢想是環遊世界。', r'dreams?'),
    ('future', '未來', 'I want to be a pilot in the future.', '我將來想當飛行員。', r'future'),
    ('want to be', '想成為', 'She wants to be a singer.', '她想當歌手。', r'wants? to be|would like to be'),
    ('hope', '希望', 'I hope to live by the sea.', '我希望住在海邊。', r'hop(e|es|ed|ing)'),
    ('job', '工作', 'Being a nurse is a hard job.', '當護理師是很辛苦的工作。', r'jobs?|career'),
    ('help people', '幫助人', 'Doctors help people every day.', '醫生每天幫助人。', r'help(s|ing)? (people|others|children|animals|sick)'),
    ('practice', '練習', 'I practice the piano every day.', '我每天練鋼琴。', r'practic(e|es|ed|ing)'),
    ('study hard', '用功讀書', 'I need to study hard.', '我需要用功讀書。', r'stud(y|ies|ied) hard|work(s|ed)? hard'),
    ('skill', '技能', 'Drawing is an important skill for designers.', '畫圖是設計師很重要的技能。', r'skills?'),
    ('reach my dream', '實現夢想', 'I will work hard to reach my dream.', '我會努力實現我的夢想。', r'(reach|achieve|realize|make) (my|your|his|her) dream( come true)?|come true'),
    ('interested in', '對…有興趣', 'I am interested in animals.', '我對動物有興趣。', r'interested in'),
    ('someday', '有一天', 'Someday I will open my own café.', '有一天我會開自己的咖啡店。', r'some ?day|one day'),
    ('give up', '放棄', 'Never give up on your dream.', '永遠不要放棄你的夢想。', r'giv(e|es|ing) up|gave up'),
    ('because', '因為', 'I want to be a vet because I love animals.', '我想當獸醫，因為我愛動物。', r'because'),
  ],
  'frames': [
    ('My dream is to ____.', '我的夢想是……', 'My dream is to be a vet.'),
    ('I want to be a ____ because ____.', '我想當……，因為……', 'I want to be a chef because I love cooking.'),
    ('I am interested in ____.', '我對……有興趣', 'I am interested in computers.'),
    ('To reach my dream, I need to ____.', '為了實現夢想，我需要……', 'To reach my dream, I need to study science.'),
    ('Now, I ____ every day.', '現在我每天……', 'Now, I practice drawing every day.'),
    ('Someday, I will ____.', '有一天我會……', 'Someday, I will open my own animal hospital.'),
  ],
  'write': {
    'prompt': 'Write about your dream.',
    'zh': '寫你的夢想：將來想做什麼、為什麼、需要學什麼、現在怎麼努力。',
    'qs': [('What is your dream?', '你的夢想是什麼？'), ('Why do you have this dream?', '為什麼有這個夢想？'),
           ('What do you need to learn or do?', '需要學什麼、做什麼？'), ('What are you doing now?', '現在你在做什麼努力？')],
    'model': {
      1: 'My dream is to be a vet. I love animals, and I want to help them. '
         'I need to study hard. Now, I read books about animals every day. I hope my dream comes true.',
      2: 'My dream is to become a pilot. When I was little, I took a plane to Japan, and I was interested in flying from that day. '
         'Pilots can see the world from the sky and visit many countries. '
         'To reach my dream, I need to be healthy, study science, and speak good English. '
         'So now I run every morning and practice English with this website. '
         'It will not be easy, but I will never give up. Someday, I will fly a big plane.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'I want to be a doctor. I want to help sick people. (because)<br>→ {0}', 'blanks': [['I want to be a doctor because I want to help sick people.']],
     'exp': '結果 because 原因。'},
    {'q': 'My dream is hard. I will not give up. (but)<br>→ {0}', 'blanks': [['My dream is hard, but I will not give up.', "My dream is hard, but I won't give up.", 'My dream is hard but I will not give up.', "My dream is hard but I won't give up."]],
     'exp': 'but 接相反的兩句。'},
    {'q': 'I practice every day. I want to be a good singer. (so that)<br>→ {0}', 'blanks': [['I practice every day so that I can be a good singer.', 'I practice every day so that I will be a good singer.']],
     'exp': 'so that + 主詞 + can／will＝為了能…。'},
    {'q': 'I was young. I wanted to be a police officer. (When)<br>→ {0}', 'blanks': [['When I was young, I wanted to be a police officer.', 'I wanted to be a police officer when I was young.']],
     'exp': 'When + 過去的時候, 主要句子。'},
    {'q': 'Cooking is fun. I want to be a chef. (so)<br>→ {0}', 'blanks': [['Cooking is fun, so I want to be a chef.', 'Cooking is fun so I want to be a chef.']],
     'exp': '原因, so 結果。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'I want to be an artist.（改成問對方的 Do 問句）<br>→ {0}', 'blanks': [['Do you want to be an artist?']],
     'exp': 'Do you want to…？'},
    {'q': 'She wants to be a singer.（針對 a singer 用 What 問）<br>→ {0}', 'blanks': [['What does she want to be?']],
     'exp': 'What does + 主詞 + want to be？'},
    {'q': 'I will open a café.（改成否定句）<br>→ {0}', 'blanks': [["I won't open a café.", 'I will not open a café.', "I won't open a cafe.", 'I will not open a cafe.']],
     'exp': "will 的否定：won't／will not。"},
    {'q': 'Being a doctor is hard.（改成 It is … to 開頭）<br>→ {0}', 'blanks': [['It is hard to be a doctor.', "It's hard to be a doctor."]],
     'exp': 'V-ing 當主詞 ＝ It is + 形容詞 + to + 原形。'},
    {'q': 'I am interested in science.（改成 Science is … to me. 用 interesting）<br>→ {0}', 'blanks': [['Science is interesting to me.']],
     'exp': '人 be interested in 東西 ＝ 東西 is interesting。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'is / dream / My / be / to / a / pilot<br>→ {0}', 'blanks': [['My dream is to be a pilot.']], 'exp': 'My dream is to + 原形。'},
    {'q': 'up / Never / your / give / dream / on<br>→ {0}', 'blanks': [['Never give up on your dream.']], 'exp': 'Never + 原形＝永遠不要…。'},
    {'q': 'want / What / you / to / do / be<br>→ {0}', 'blanks': [['What do you want to be?']], 'exp': 'What do you want to be?'},
    {'q': 'come / will / I / my / true / hope / dream<br>→ {0}', 'blanks': [['I hope my dream will come true.']], 'exp': 'come true＝實現。'},
    {'q': 'need / I / to / English / study / hard<br>→ {0}', 'blanks': [['I need to study English hard.']], 'exp': 'need to + 原形；hard（努力地）放在受詞 English 後面。'},
  ]},
]
