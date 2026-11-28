# 寫作園地 Unit 4 A Day at School 學校的一天（內容全部自編）

UNIT = {
  'no': 4, 'en': 'A Day at School', 'zh': '學校的一天',
  'intro': '照時間順序寫你在學校的一天：幾點到校、上什麼課、午餐和下課做什麼、放學後去哪。',
  'tense': '寫「平常」的一天用現在式（I get to school at…）；寫「昨天」的一天就全部改過去式（I got…）。用 first、then、after that 排順序。',
  'dialog': [
    ('Amy', 'What time do you get to school every day?'),
    ('Ben', 'At seven thirty. My first class starts at eight.'),
    ('Amy', 'What\'s your favorite class?'),
    ('Ben', 'P.E.! We play basketball on Tuesdays. What about you?'),
    ('Amy', 'I like art. I\'m not good at math, though.'),
    ('Ben', 'What do you do at lunchtime?'),
    ('Amy', 'I eat lunch with my classmates, and then I take a short nap.'),
    ('Ben', 'Me too. After school, I go to the library to do my homework.'),
  ],
  'speak': [
    ('What time do you get to school?', '你幾點到學校？', 'I get to school at seven forty.'),
    ('What is your favorite subject? Why?', '你最喜歡哪一科？為什麼？', 'I like English because it is fun.'),
    ('What do you do at lunchtime?', '你午餐時間做什麼？', 'I eat lunch and then take a nap.'),
    ('What do you do after school?', '你放學後做什麼？', 'I go to cram school. / I play basketball.'),
  ],
  'words': [
    ('get to school', '到學校', 'I get to school at seven thirty.', '我七點半到學校。', r'(get|gets|got) to school'),
    ('class', '課；班級', 'We have seven classes a day.', '我們一天有七堂課。', r'class(es)?'),
    ('subject', '科目', 'Science is my favorite subject.', '自然是我最喜歡的科目。', r'subjects?'),
    ('classmate', '同學', 'My classmates are friendly.', '我的同學都很友善。', r'classmates?'),
    ('break', '下課時間', 'We play ball during the break.', '我們下課時打球。', r'breaks?|recess'),
    ('lunchtime', '午餐時間', 'At lunchtime, I eat with my friends.', '午餐時間我和朋友一起吃飯。', r'lunch ?time|lunch'),
    ('take a nap', '午睡', 'We take a nap after lunch.', '我們午餐後午睡。', r'(take|takes|took) a nap|nap'),
    ('P.E. class', '體育課', 'We run a lot in P.E. class.', '體育課我們跑很多。', r'p\.?\s?e\.?|gym class'),
    ('homework', '功課', 'I do my homework after dinner.', '我晚餐後寫功課。', r'homework'),
    ('quiz', '小考', 'We have an English quiz today.', '我們今天有英文小考。', r'quiz(zes)?|tests?|exams?'),
    ('clean the classroom', '打掃教室', 'We clean the classroom at four.', '我們四點打掃教室。', r'clean(s|ed)? (the|our) (classroom|school)'),
    ('club', '社團', 'I am in the science club.', '我參加自然科學社。', r'clubs?'),
    ('first … then …', '先……然後……', 'First, I wash my hands. Then, I eat lunch.', '我先洗手，然後吃午餐。', r'first|then|after that|finally'),
    ('after school', '放學後', 'I go to cram school after school.', '我放學後去補習班。', r'after school'),
  ],
  'frames': [
    ('I get to school at ____.', '我……點到學校', 'I get to school at seven thirty.'),
    ('My first class is ____.', '我第一堂課是……', 'My first class is math.'),
    ('My favorite subject is ____ because ____.', '我最喜歡的科目是……，因為……', 'My favorite subject is science because I like doing experiments.'),
    ('During the break, I ____.', '下課時我……', 'During the break, I chat with my friends.'),
    ('After lunch, we ____.', '午餐後我們……', 'After lunch, we take a nap.'),
    ('After school, I ____.', '放學後我……', 'After school, I go to the library.'),
  ],
  'write': {
    'prompt': 'Write about a day at your school.',
    'zh': '照時間順序寫你在學校的一天。可以寫平常的一天，或是特別的一天（例如運動會、校外教學）。',
    'qs': [('What time do you get to school?', '幾點到學校？'), ('What classes do you have? Which one do you like?', '上什麼課？喜歡哪一科？'),
           ('What do you do at lunch and during breaks?', '午餐和下課做什麼？'), ('What do you do after school?', '放學後做什麼？')],
    'model': {
      1: 'I get to school at seven thirty. My first class is English. My favorite subject is P.E. '
         'At lunchtime, I eat with my classmates. After school, I do my homework. I like my school.',
      2: 'My school day starts early. I get to school at seven twenty and clean the classroom with my classmates. '
         'First, we have math and Chinese. Then, during the break, I play ball with my friends. '
         'My favorite subject is science because our teacher lets us do experiments. '
         'After lunch, we take a short nap, so I feel awake in the afternoon. '
         'After school, I go to the art club. It is a busy day, but I always have fun.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'I eat lunch. Then I take a nap. (after)<br>→ {0}', 'blanks': [['After I eat lunch, I take a nap.', 'I take a nap after I eat lunch.', 'After lunch, I take a nap.', 'I take a nap after lunch.']],
     'exp': 'after + 先發生的事：After I eat lunch, I take a nap.'},
    {'q': 'I like math. I like science. (both … and …)<br>→ {0}', 'blanks': [['I like both math and science.']],
     'exp': 'like both A and B＝A 和 B 都喜歡。'},
    {'q': 'The test was hard. I passed it. (but)<br>→ {0}', 'blanks': [['The test was hard, but I passed it.', 'The test was hard but I passed it.']],
     'exp': 'but 接意思相反的兩句。'},
    {'q': 'I was late for school. I missed the bus. (because)<br>→ {0}', 'blanks': [['I was late for school because I missed the bus.', 'Because I missed the bus, I was late for school.']],
     'exp': '結果 because 原因。'},
    {'q': 'We have P.E. on Tuesday. We have P.E. on Friday. (and)<br>→ {0}', 'blanks': [['We have P.E. on Tuesday and Friday.', 'We have P.E. on Tuesday and on Friday.', 'We have PE on Tuesday and Friday.']],
     'exp': '一樣的部分不用重複，只把兩個時間用 and 接起來。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'I get to school at seven thirty.（針對 at seven thirty 用 What time 問）<br>→ {0}', 'blanks': [['What time do you get to school?']],
     'exp': 'What time + do + 主詞 + 原形動詞？I 改成 you。'},
    {'q': 'We have a quiz today.（把 today 改成 tomorrow，用 will）<br>→ {0}', 'blanks': [['We will have a quiz tomorrow.', "We'll have a quiz tomorrow."]],
     'exp': 'will + 原形動詞 表示未來。'},
    {'q': 'Tom cleans the classroom every day.（把 every day 改成 now）<br>→ {0}', 'blanks': [['Tom is cleaning the classroom now.']],
     'exp': 'now 用現在進行式：is + V-ing。'},
    {'q': 'My favorite subject is art.（針對 art 用 What 問）<br>→ {0}', 'blanks': [['What is your favorite subject?', "What's your favorite subject?"]],
     'exp': 'What is your favorite subject?'},
    {'q': 'She did her homework at school.（改成否定句）<br>→ {0}', 'blanks': [["She didn't do her homework at school.", 'She did not do her homework at school.']],
     'exp': '過去式否定：didn\'t + 原形（did → do）。'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'starts / class / at / My / first / eight<br>→ {0}', 'blanks': [['My first class starts at eight.']], 'exp': '主詞 My first class + starts。'},
    {'q': 'after / a / We / nap / lunch / take<br>→ {0}', 'blanks': [['We take a nap after lunch.']], 'exp': 'take a nap＝午睡。'},
    {'q': 'is / subject / What / favorite / your<br>→ {0}', 'blanks': [['What is your favorite subject?']], 'exp': 'What is + 名詞？'},
    {'q': 'go / I / library / school / to / after / the<br>→ {0}', 'blanks': [['I go to the library after school.', 'After school I go to the library.']], 'exp': 'after school 放句尾或句首都可以。'},
    {'q': 'are / my / friendly / All / classmates / of<br>→ {0}', 'blanks': [['All of my classmates are friendly.']], 'exp': 'All of my classmates＝我所有的同學。'},
  ]},
]
