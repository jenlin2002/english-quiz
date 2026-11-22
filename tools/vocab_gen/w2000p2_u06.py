# 主題 2000 字 PART 2 Unit 6：Family 家庭（字表依課本 PART 2 印刷頁 148，6 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 6, 'en': 'Family', 'zh': '家庭',
  'intro': '進階的家庭用字，共 6 個：哥哥姊姊、孫子孫女、姪子姪女，以及結婚。',
  'words': [
    W('elder', 'adj.', '年紀較大的', 'elder brother／sister 哥哥／姊姊（只放名詞前）', 'My elder sister is in senior high school.', '我姊姊讀高中。', '👫'),
    W('granddaughter', 'n.', '孫女；外孫女', 'grand + daughter', 'Grandma knits a sweater for her granddaughter.', '奶奶幫孫女織毛衣。', '👵'),
    W('grandson', 'n.', '孫子；外孫', 'grand + son', 'The old man plays chess with his grandson.', '那位老先生和孫子下棋。', '👴'),
    W('nephew', 'n.', '姪子；外甥', '兄弟姊妹的兒子', 'My uncle\'s son is my cousin, not my nephew.', '我叔叔的兒子是我的堂兄弟，不是姪子。', '👦'),
    W('niece', 'n.', '姪女；外甥女', '兄弟姊妹的女兒', 'Aunt Mary bought a doll for her niece.', '瑪莉阿姨買了一個娃娃給她的姪女。', '👧'),
    W('marry', 'v.', '和…結婚；嫁；娶', 'marry + 人（不加 with）；get married 結婚；married 已婚的', 'My cousin will marry his girlfriend next spring.', '我表哥明年春天要和女朋友結婚。', '💍'),
  ],
  'focus': [
    {'title': '家人怎麼叫', 'head': ('關係', '英文', ''),
     'rows': [('兒子的兒子／女兒', 'grandson／granddaughter', ''), ('兄弟姊妹的兒子', 'nephew', ''), ('兄弟姊妹的女兒', 'niece', ''), ('叔伯姑舅的孩子', 'cousin', '')],
     'note': 'marry 後面直接接人：She married Tom.（不說 married with）；「結婚了」說 be married／get married。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=6, n_ce=5, n_ec=4, n_sp=4, fill=[
  F('My brother\'s daughter is my ______.', ['niece', 'nephew', 'granddaughter', 'cousin'], 0, '兄弟的女兒 → niece。'),
  F('My sister\'s son is my ______.', ['grandson', 'nephew', 'niece', 'uncle'], 1, '姊妹的兒子 → nephew。'),
  F('Will you ______ me?', ['marry', 'married', 'marry with', 'get'], 0, 'marry + 人，不加 with。'),
  F('Mr. and Mrs. Wang have been ______ for twenty years.', ['marry', 'married', 'marrying', 'elder'], 1, 'be married 已婚。'),
  F('Tom is three years older than me. He is my ______ brother.', ['elder', 'younger', 'grand', 'little'], 0, '比我大 → elder brother 哥哥。'),
])
