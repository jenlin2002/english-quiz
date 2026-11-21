# 寫作園地 Unit 2 My Pet 我的寵物（內容全部自編）

UNIT = {
  'no': 2, 'en': 'My Pet', 'zh': '我的寵物',
  'intro': '介紹你的寵物；沒有養寵物的話，就寫你想養的寵物。',
  'tense': '描述寵物的樣子和習慣用現在式（It is… / It likes…）；「想養」的寵物可以用 I want… / I will…。',
  'dialog': [
    ('Amy', 'Is that your dog in the photo?'),
    ('Ben', 'Yes! His name is Lucky. He is three years old.'),
    ('Amy', 'He\'s so cute! What does he like to do?'),
    ('Ben', 'He loves to run in the park and catch balls.'),
    ('Amy', 'Who takes care of him?'),
    ('Ben', 'I feed him every morning, and my brother walks him after dinner.'),
    ('Amy', 'I want a pet, too. Maybe a cat.'),
    ('Ben', 'Cats are great! They are quiet and clean.'),
  ],
  'speak': [
    ('Do you have a pet? What is it?', '你有養寵物嗎？是什麼？', 'Yes, I have a dog. / No, but I want a cat.'),
    ('What does it look like?', '牠長什麼樣子？', 'It is small and white. It has big eyes.'),
    ('What does it like to do?', '牠喜歡做什麼？', 'It likes to sleep. / It likes to play with a ball.'),
    ('How do you take care of it?', '你怎麼照顧牠？', 'I feed it every day. / I walk it after school.'),
  ],
  'words': [
    ('pet', '寵物', 'Do you have a pet at home?', '你家有養寵物嗎？', r'pets?'),
    ('cute', '可愛的', 'The little rabbit is so cute.', '那隻小兔子好可愛。', r'cute'),
    ('fluffy', '毛茸茸的', 'My cat has fluffy white fur.', '我的貓有毛茸茸的白毛。', r'fluffy'),
    ('tail', '尾巴', 'The dog is wagging its tail.', '那隻狗在搖尾巴。', r'tails?'),
    ('feed', '餵', 'I feed my fish twice a day.', '我一天餵魚兩次。', r'feed(s|ing)?|fed'),
    ('walk the dog', '遛狗', 'Dad walks the dog after dinner.', '爸爸晚餐後去遛狗。', r'walk(s|ed|ing)? (the|my|our|him|her|it)'),
    ('take care of', '照顧', 'I take care of my hamster every day.', '我每天照顧我的倉鼠。', r'(take|takes|took|taking) care of'),
    ('play with', '和…玩', 'My cat likes to play with a ball.', '我的貓喜歡玩球。', r'play(s|ed|ing)? with'),
    ('smart', '聰明的', 'Parrots are smart birds.', '鸚鵡是很聰明的鳥。', r'smart'),
    ('friendly', '友善的', 'Our dog is friendly to everyone.', '我們的狗對每個人都很友善。', r'friendly'),
    ('noisy', '吵鬧的', 'The puppy is noisy at night.', '小狗晚上很吵。', r'noisy'),
    ('give … a bath', '幫…洗澡', 'We give our dog a bath every Sunday.', '我們每個星期天幫狗洗澡。', r'bath'),
    ('vet', '獸醫', 'We took our cat to the vet.', '我們帶貓去看獸醫。', r'vets?'),
    ('best friend', '最好的朋友', 'My dog is my best friend.', '我的狗是我最好的朋友。', r'best friends?'),
  ],
  'frames': [
    ('I have a ____. Its name is ____.', '我有一隻……，牠的名字是……（沒有寵物就寫：I want a ____.）', 'I have a cat. Its name is Mimi.'),
    ('It is ____ and ____.', '牠很……又很……', 'It is small and fluffy.'),
    ('It has ____.', '牠有……（身體的特徵）', 'It has big eyes and a short tail.'),
    ('It likes to ____.', '牠喜歡……', 'It likes to sleep on my bed.'),
    ('Every day, I ____.', '每天我會……（怎麼照顧牠）', 'Every day, I feed it and play with it.'),
    ('My pet is like my ____ because ____.', '我的寵物像我的……，因為……', 'My pet is like my best friend because it always makes me happy.'),
  ],
  'write': {
    'prompt': 'Write about your pet or the pet you want.',
    'zh': '介紹你的寵物，或是你想養的寵物（為什麼想養、會怎麼照顧牠）。',
    'qs': [('What is your pet? What is its name?', '是什麼寵物？叫什麼名字？'), ('What does it look like?', '長什麼樣子？'),
           ('What does it like to do?', '喜歡做什麼？'), ('How do you take care of it? Why do you love it?', '你怎麼照顧牠？為什麼喜歡牠？')],
    'model': {
      1: 'I have a dog. His name is Lucky. He is brown and very cute. He likes to run and catch balls. '
         'I feed him every morning. I love Lucky very much.',
      2: 'I don\'t have a pet now, but I really want a cat. I want a white cat with fluffy fur and big blue eyes. '
         'Cats are quiet and clean, so they are good pets for my family. If I have a cat, I will feed it every day '
         'and play with it after school. I will also take it to the vet when it is sick. '
         'I think a cat can be my best friend because it will always stay with me.',
    },
  },
}

QUIZ = [
  {'title': '① 句子合併：用括號裡的字把兩句合成一句', 'note': '英檢初級寫作第一部分的題型。整句寫出來，句尾的標點可以不用打。', 'items': [
    {'q': 'I have a dog. It is very smart. (and)<br>→ {0}', 'blanks': [['I have a dog, and it is very smart.', 'I have a dog and it is very smart.']],
     'exp': 'and 連接兩個完整的句子：句子, and 句子。'},
    {'q': 'My cat is small. My cat is fluffy. (and)<br>→ {0}', 'blanks': [['My cat is small and fluffy.']],
     'exp': '主詞一樣時，只要把兩個形容詞用 and 接起來。'},
    {'q': 'I want a pet. My mom says no. (but)<br>→ {0}', 'blanks': [['I want a pet, but my mom says no.', 'I want a pet but my mom says no.']],
     'exp': 'but 連接意思相反的兩句。'},
    {'q': 'Dogs are friendly. Many people love them. (so)<br>→ {0}', 'blanks': [['Dogs are friendly, so many people love them.', 'Dogs are friendly so many people love them.']],
     'exp': '原因, so 結果。'},
    {'q': 'We took our dog to the vet. He was sick. (because)<br>→ {0}', 'blanks': [['We took our dog to the vet because he was sick.', 'Because he was sick, we took our dog to the vet.']],
     'exp': '結果 because 原因。'},
  ]},
  {'title': '② 句子改寫：照括號的要求改寫', 'items': [
    {'q': 'My brother feeds the fish every day.（改成否定句）<br>→ {0}', 'blanks': [['My brother doesn\'t feed the fish every day.', 'My brother does not feed the fish every day.']],
     'exp': '第三人稱單數的否定：doesn\'t + 原形（feeds → feed）。'},
    {'q': 'Your rabbit likes carrots.（改成 Does 開頭的問句）<br>→ {0}', 'blanks': [['Does your rabbit like carrots?']],
     'exp': 'Does 開頭，動詞改回原形：likes → like。'},
    {'q': 'I walk my dog every day.（把 every day 改成 yesterday）<br>→ {0}', 'blanks': [['I walked my dog yesterday.']],
     'exp': 'yesterday 是過去的時間，動詞用過去式 walked。'},
    {'q': 'The cat is sleeping on the sofa.（針對 on the sofa 用 Where 問）<br>→ {0}', 'blanks': [['Where is the cat sleeping?']],
     'exp': 'Where + is + 主詞 + V-ing？'},
    {'q': 'My puppy is very cute.（用 How 改成感嘆句）<br>→ {0}', 'blanks': [['How cute my puppy is!']],
     'exp': 'How + 形容詞 + 主詞 + 動詞！'},
  ]},
  {'title': '③ 重組句子：把字詞排成正確的句子', 'note': '第一個字的大寫已經幫你標好了。', 'items': [
    {'q': 'a / have / pet / you / Do<br>→ {0}', 'blanks': [['Do you have a pet?']], 'exp': 'Do you have…? 你有…嗎？'},
    {'q': 'name / What\'s / dog\'s / your<br>→ {0}', 'blanks': [['What\'s your dog\'s name?', 'What is your dog\'s name?']], 'exp': 'your dog\'s name 你的狗的名字。'},
    {'q': 'likes / My / cat / to / sleep / sun / in / the<br>→ {0}', 'blanks': [['My cat likes to sleep in the sun.']], 'exp': 'like to + 原形動詞。'},
    {'q': 'take / of / care / I / my / every day / hamster<br>→ {0}', 'blanks': [['I take care of my hamster every day.']], 'exp': 'take care of + 照顧的對象。'},
    {'q': 'can / your / A / be / friend / best / pet<br>→ {0}', 'blanks': [['A pet can be your best friend.']], 'exp': 'can + be + 名詞。'},
  ]},
]
