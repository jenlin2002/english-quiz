# 寫作園地 Unit 3 My Family 我的家人（內容全部自編）

UNIT = {
  'no': 3, 'en': 'My Family', 'zh': '我的家人',
  'intro': '介紹你的家人：有誰、做什麼工作、長什麼樣子、你們一起做什麼。',
  'tense': '介紹家人用現在式（My dad is… / She likes…）；說家人常做的事加 always、usually、often。',
  'dialog': [
    ('Amy', 'Is this a picture of your family?'),
    ('Ben', 'Yes. There are five people in my family.'),
    ('Amy', 'Who is the tall man?'),
    ('Ben', 'That\'s my dad. He is a bus driver. He is funny and kind.'),
    ('Amy', 'And the woman next to him?'),
    ('Ben', 'That\'s my mom. She works at a bank. She is a great cook, too.'),
    ('Amy', 'What do you do together on weekends?'),
    ('Ben', 'We usually go hiking or visit my grandparents in Tainan.'),
  ],
  'speak': [
    ('How many people are there in your family?', '你家有幾個人？', 'There are four people in my family.'),
    ('Who are they?', '他們是誰？', 'My dad, my mom, my sister, and me.'),
    ('What does your dad or mom do?', '你爸爸或媽媽做什麼工作？', 'My mom is a nurse. / My dad works in an office.'),
    ('What do you do together?', '你們一起做什麼？', 'We often eat dinner together and watch TV.'),
  ],
  'words': [
    ('family', '家人；家庭', 'I love my family very much.', '我很愛我的家人。', r'famil(y|ies)'),
    ('parents', '父母', 'My parents both work in Taipei.', '我爸媽都在台北工作。', r'parents?'),
    ('grandparents', '祖父母', 'I visit my grandparents every month.', '我每個月去看祖父母。', r'grand(parents?|ma|pa|mother|father)'),
    ('older brother', '哥哥', 'My older brother is in high school.', '我哥哥讀高中。', r'(older|younger|big|little) (brother|sister)'),
    ('only child', '獨生子／女', 'I am an only child.', '我是獨生子。', r'only child'),
    ('kind', '親切的', 'My grandma is kind to everyone.', '我奶奶對每個人都很親切。', r'kind'),
    ('funny', '好笑的；風趣的', 'My uncle is very funny.', '我叔叔很風趣。', r'funny'),
    ('hard-working', '努力的', 'My mom is hard-working.', '我媽媽工作很努力。', r'hard[- ]?working|work(s)? hard'),
    ('look like', '長得像', 'I look like my dad.', '我長得像我爸爸。', r'looks? like'),
    ('be good at', '擅長', 'My sister is good at drawing.', '我姊姊很會畫畫。', r'(is|are|am|was|were) good at'),
    ('work as', '擔任…工作', 'My aunt works as a teacher.', '我阿姨是當老師。', r'works? as'),
    ('spend time with', '和…共度時光', 'I like to spend time with my family.', '我喜歡和家人在一起。', r'spends? (time|the weekend|weekends)'),
    ('take care of', '照顧', 'My grandpa takes care of me after school.', '放學後我爺爺照顧我。', r'(take|takes|took) care of'),
    ('get along with', '和…處得好', 'I get along well with my sister.', '我和我妹妹處得很好。', r'gets? along'),
  ],
  'frames': [
    ('There are ____ people in my family.', '我家有……個人', 'There are four people in my family.'),
    ('My ____ is a ____.', '我的……是……（職業）', 'My mom is a nurse.'),
    ('He / She is ____ and ____.', '他／她很……又很……（個性）', 'She is kind and hard-working.'),
    ('I look like my ____.', '我長得像我的……', 'I look like my dad.'),
    ('My ____ is good at ____.', '我的……很會……', 'My sister is good at singing.'),
    ('On weekends, we often ____.', '週末我們常常……', 'On weekends, we often go to the night market.'),
  ],
  'write': {
    'prompt': 'Write about your family.',
    'zh': '介紹你的家人：家裡有誰、他們是怎樣的人、你們常一起做什麼。',
    'qs': [('How many people are there in your family?', '家裡有幾個人？'), ('What are they like? What do they do?', '他們是怎樣的人？做什麼工作？'),
           ('What do you do together?', '你們常一起做什麼？'), ('Why do you love your family?', '你為什麼愛你的家人？')],
    'model': {
      1: 'There are four people in my family. My dad is a bus driver, and my mom is a nurse. '
         'My sister is good at drawing. On weekends, we often go to the park. I love my family.',
      2: 'There are five people in my family: my parents, my grandma, my little brother, and me. '
         'My dad works as an engineer. He is tall and funny. My mom is a teacher, and she is very hard-working. '
         'My grandma takes care of us after school, and she cooks delicious food. '
         'I get along well with my brother, but sometimes we fight over the TV. '
         'On Sundays, we usually eat lunch together. I feel lucky because my family always helps me.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'My dad is tall. My dad is funny. (and)<br>→ {0}', 'blanks': [['My dad is tall and funny.']],
     'exp': '主詞一樣時，兩個形容詞用 and 接起來。'},
    {'q': 'My mom is a nurse. My aunt is a nurse, too. (Both … and …)<br>→ {0}', 'blanks': [['Both my mom and my aunt are nurses.', 'Both my mom and aunt are nurses.']],
     'exp': 'Both A and B 是兩個人，動詞用 are，nurse 要變複數。'},
    {'q': 'I have a brother. I don\'t have a sister. (but)<br>→ {0}', 'blanks': [['I have a brother, but I don\'t have a sister.', 'I have a brother but I don\'t have a sister.', 'I have a brother, but I do not have a sister.']],
     'exp': 'but 連接意思相反的兩句。'},
    {'q': 'My grandma lives with us. She cooks dinner every day. (who)<br>→ {0}', 'blanks': [['My grandma, who lives with us, cooks dinner every day.', 'My grandma who lives with us cooks dinner every day.']],
     'exp': 'who 代替人，把「跟我們住」放在 grandma 後面說明她。'},
    {'q': 'My sister practices every day. She is good at the piano. (so)<br>→ {0}', 'blanks': [['My sister practices every day, so she is good at the piano.', 'My sister practices every day so she is good at the piano.']],
     'exp': '原因, so 結果。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'My brother is older than me.（改成 I am … than my brother.）<br>→ {0}', 'blanks': [['I am younger than my brother.', "I'm younger than my brother."]],
     'exp': '他比我大 ＝ 我比他小：older → younger。'},
    {'q': 'There are four people in my family.（針對 four 用 How many 問）<br>→ {0}', 'blanks': [['How many people are there in your family?']],
     'exp': 'How many + 複數名詞 + are there…？my 要改成 your。'},
    {'q': 'My father works in a hospital.（改成 Does 開頭的問句）<br>→ {0}', 'blanks': [['Does your father work in a hospital?']],
     'exp': 'Does + 主詞 + 原形動詞；my 改 your。'},
    {'q': 'We visit our grandparents every Sunday.（把 every Sunday 改成 last Sunday）<br>→ {0}', 'blanks': [['We visited our grandparents last Sunday.']],
     'exp': 'last Sunday 是過去，visit → visited。'},
    {'q': 'My uncle is a pilot.（針對 a pilot 用 What 問）<br>→ {0}', 'blanks': [['What does your uncle do?', 'What is your uncle?', "What's your uncle?"]],
     'exp': '問職業最常用 What does + 人 + do？'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'look / I / my / like / mother<br>→ {0}', 'blanks': [['I look like my mother.']], 'exp': 'look like＝長得像。'},
    {'q': 'good / is / at / My / cooking / dad<br>→ {0}', 'blanks': [['My dad is good at cooking.']], 'exp': 'be good at + V-ing / 名詞。'},
    {'q': 'with / along / I / get / my / well / cousins<br>→ {0}', 'blanks': [['I get along well with my cousins.']], 'exp': 'get along well with＝和…處得很好。'},
    {'q': 'as / works / My / a / aunt / cook<br>→ {0}', 'blanks': [['My aunt works as a cook.']], 'exp': 'work as + 職業。'},
    {'q': 'spend / with / I / my / like / to / time / family<br>→ {0}', 'blanks': [['I like to spend time with my family.']], 'exp': 'spend time with＋人。'},
  ]},
]
