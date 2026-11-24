# WORD UP 複習區 Unit 29（WORD UP「M-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 29, 'en': 'M-I', 'zh': 'M 開頭（一）',
  'intro': 'WORD UP「M-I」的 38 個字（ma\'am 到 maximum）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('ma\'am', 'n.', '女士（尊稱）', '= madam', 'Can I help you, ma\'am?', '女士，需要幫忙嗎？', '👩‍🦳'),
    W('machine', 'n.', '機器', 'washing machine 洗衣機', 'Put the clothes in the washing machine.', '把衣服放進洗衣機。', '🤖'),
    W('mad', 'adj.', '生氣的；瘋狂的', 'be mad at + 人', 'Mom is mad at me.', '媽媽在生我的氣。', '😡'),
    W('magazine', 'n.', '雜誌', '', 'I read a science magazine every month.', '我每個月看一本科學雜誌。', '📰'),
    W('magic', 'n./adj.', '魔術；魔法的', '', 'He can do magic tricks.', '他會變魔術。', '🪄'),
    W('magician', 'n.', '魔術師', '', 'The magician pulled a rabbit out of a hat.', '魔術師從帽子裡變出一隻兔子。', '🎩'),
    W('mail', 'n./v.', '郵件；郵寄', '', 'Did you check the mail?', '你看過信箱了嗎？', '📬'),
    W('mailman', 'n.', '郵差', '= mail carrier', 'The mailman comes at ten every day.', '郵差每天十點來。', '📮'),
    W('main', 'adj.', '主要的', '', 'What\'s the main idea of this story?', '這個故事的主旨是什麼？', '🎯'),
    W('maintain', 'v.', '維持；保養', '', 'It\'s important to maintain good health.', '維持健康很重要。', '🛠️'),
    W('major', 'adj./n.', '主要的；主修', 'minor 次要的', 'Traffic is a major problem in big cities.', '交通是大城市的主要問題。', '🏆'),
    W('make', 'v.', '做；製造；使', '三態 make-made-made；make + 人 + 原形', 'The movie made me cry.', '那部電影讓我哭了。', '🛠️'),
    W('male', 'adj./n.', '男性的；雄性', 'female 女性的', 'The male lion has a mane.', '公獅有鬃毛。', '♂️'),
    W('mall', 'n.', '購物中心', '', 'Let\'s go to the mall this weekend.', '我們這週末去購物中心吧。', '🛍️'),
    W('man', 'n.', '男人', '複數 men', 'Two men are talking.', '兩個男人在聊天。', '👨'),
    W('manager', 'n.', '經理', '', 'I want to speak to the manager.', '我想跟經理談談。', '🧑‍💼'),
    W('Mandarin', 'n.', '國語；華語', '', 'Mandarin is spoken in Taiwan.', '台灣說國語。', '🀄'),
    W('mango', 'n.', '芒果', '複數 mangoes', 'Mango shaved ice is my favorite.', '芒果冰是我的最愛。', '🥭'),
    W('manner', 'n.', '方式；禮貌', 'manners 禮貌（複數）', 'Good manners are important.', '良好的禮貌很重要。', '🙇'),
    W('many', 'adj.', '許多', '接可數名詞；How many…?', 'How many brothers do you have?', '你有幾個兄弟？', '🔢'),
    W('map', 'n.', '地圖', '', 'Look at the map. We are here.', '看地圖，我們在這裡。', '🗺️'),
    W('March', 'n.', '三月', '', 'Spring starts in March.', '春天從三月開始。', '🌸'),
    W('mark', 'n./v.', '記號；分數；標記', '', 'Mark the right answer with a check.', '在正確答案上打勾。', '✔️'),
    W('marker', 'n.', '麥克筆；記號筆', '', 'Write your name with a marker.', '用麥克筆寫你的名字。', '🖊️'),
    W('market', 'n.', '市場', 'night market 夜市', 'Let\'s go to the night market.', '我們去夜市吧。', '🏮'),
    W('marriage', 'n.', '婚姻', '', 'They have a happy marriage.', '他們的婚姻很幸福。', '💍'),
    W('married', 'adj.', '已婚的', 'be married to + 人；get married 結婚', 'My aunt got married last year.', '我阿姨去年結婚了。', '💒'),
    W('marry', 'v.', '和…結婚', 'marry + 人（不加 with）', 'Will you marry me?', '你願意嫁給我嗎？', '💐'),
    W('marvelous', 'adj.', '令人驚嘆的；很棒的', '', 'We had a marvelous time.', '我們玩得很開心。', '🤩'),
    W('mask', 'n.', '面具；口罩', '', 'Wear a mask when you have a cold.', '感冒時要戴口罩。', '😷'),
    W('mass', 'n./adj.', '大量；團；大眾的', 'mass media 大眾傳播', 'A mass of people waited outside.', '一大群人在外面等。', '👥'),
    W('master', 'n./v.', '主人；大師；精通', '', 'He wants to master English.', '他想精通英文。', '🥋'),
    W('mat', 'n.', '墊子', '', 'Wipe your shoes on the mat.', '在腳踏墊上擦擦鞋。', '🧘'),
    W('match', 'n./v.', '比賽；火柴；相配', '', 'Your shoes match your dress.', '你的鞋子和洋裝很搭。', '🔥'),
    W('material', 'n.', '材料；資料', '', 'What material is this bag made of?', '這個包包是什麼材質做的？', '🧵'),
    W('math', 'n.', '數學', '= mathematics', 'Math is my best subject.', '數學是我最拿手的科目。', '➗'),
    W('matter', 'n./v.', '事情；要緊', 'What\'s the matter? 怎麼了', 'What\'s the matter with you?', '你怎麼了？', '❓'),
    W('maximum', 'n./adj.', '最大量；最大的', 'minimum 最小量', 'The maximum speed here is 50 km per hour.', '這裡最高速限是時速 50 公里。', '🔝'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('make + 人 + 原形 / 形容詞', '使某人…', 'make me laugh ／ make me happy'),
      ('marry + 人 / get married', '和某人結婚 ／ 結婚', 'marry Tom ／ get married in June'),
      ('be mad at + 人', '生某人的氣', 'mad at his brother'),
      ('What\'s the matter?', '怎麼了？', 'What\'s the matter with you?'),
      ('male / female', '男性的 ／ 女性的', 'a male nurse'),
      ('manner / manners', '方式 ／ 禮貌', 'good manners'),
      ('How many + 複數名詞', '多少個', 'How many apples?'),
    ], 'note': 'man → men、mango → mangoes。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '雜誌', 'opts': ['magic', 'magazine', 'machine', 'marker'], 'answer': 1, 'exp': 'magazine 雜誌。'},
    {'type': 'mc', 'q': '婚姻', 'opts': ['marriage', 'married', 'market', 'master'], 'answer': 0, 'exp': 'marriage 婚姻。'},
    {'type': 'mc', 'q': '維持', 'opts': ['major', 'match', 'maintain', 'manager'], 'answer': 2, 'exp': 'maintain 維持。'},
    {'type': 'mc', 'q': '材料', 'opts': ['matter', 'maximum', 'manner', 'material'], 'answer': 3, 'exp': 'material 材料。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '魔術師（m＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['magician']], 'exp': 'magician。'},
    {'q': '機器（m＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['machine']], 'exp': 'machine。'},
    {'q': '經理（m＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['manager']], 'exp': 'manager。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The sad story {0} me cry. （使，過去式）', 'blanks': [['made']], 'exp': 'make 的過去式 made。'},
    {'q': 'There are three {0} in the room. （男人，複數）', 'blanks': [['men']], 'exp': 'man 的複數 men。'},
    {'q': 'You look sad. What\'s the {0}? （事情）', 'blanks': [['matter']], 'exp': 'What\'s the matter? 怎麼了？'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'My uncle married ______ last year.', 'opts': ['with Amy', 'Amy', 'to Amy', 'for Amy'], 'answer': 1, 'exp': 'marry + 人，不加 with。'},
    {'type': 'mc', 'q': 'The teacher made us ______ the classroom.', 'opts': ['to clean', 'cleaning', 'clean', 'cleaned'], 'answer': 2, 'exp': 'make + 人 + 原形。'},
    {'type': 'mc', 'q': 'How ______ students are there in your class?', 'opts': ['many', 'much', 'long', 'old'], 'answer': 0, 'exp': 'students 可數，用 How many。'},
    {'type': 'mc', 'q': 'Don\'t be mad ______ me. It was an accident.', 'opts': ['with', 'to', 'of', 'at'], 'answer': 3, 'exp': 'be mad at + 人。'},
  ]},
]
