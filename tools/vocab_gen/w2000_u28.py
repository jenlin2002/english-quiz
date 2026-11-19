# 主題 2000 字 Unit 28：Pronouns & reflexives 代名詞與反身代名詞（字表依課本單元；詞性、中文、例句、題目為本站自編）
# 功能詞沒有適合的照片，全部用 emoji。課本這單元另有人稱代名詞表，放在重點整理。
def W(w, pos, zh, note, ex, exzh, pic, exsay=None):
    d = {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}
    if exsay:
        d['exsay'] = exsay
    return d

UNIT = {
  'book': 'w2000', 'no': 28, 'en': 'Pronouns & reflexives', 'zh': '代名詞與反身代名詞',
  'intro': '代替名詞的字：all、both、each、some、any、something、nobody……加上 I／me／my／mine／myself 這套人稱代名詞表。重點：every-、some-、any-、no- 開頭的字都當單數。',
  'words': [
    W('all', 'adj./pron.', '全部的；全部', '', 'All the students are in the classroom.', '所有學生都在教室裡。', '💯'),
    W('another', 'adj./pron.', '另一個；再一個', '後面接單數', 'Can I have another cookie?', '我可以再吃一塊餅乾嗎？', '🍪'),
    W('any', 'adj./pron.', '任何的；一些', '多用在問句、否定句', 'Do you have any questions?', '你們有任何問題嗎？', '❓'),
    W('anyone', 'pron.', '任何人', '同 anybody', 'Is anyone at home?', '有人在家嗎？', '🙋'),
    W('anybody', 'pron.', '任何人', '同 anyone', "I didn't see anybody in the park.", '我在公園裡沒看到任何人。', '🌳'),
    W('anything', 'pron.', '任何事；任何東西', '', 'Do you want anything to drink?', '你想喝點什麼嗎？', '🥤'),
    W('both', 'adj./pron.', '兩者都', '', 'Both my parents are teachers.', '我爸媽兩個都是老師。', '👫'),
    W('each', 'adj./pron.', '每一個；各自', 'each of + 複數名詞，動詞用單數', 'Each student has a desk.', '每個學生都有一張書桌。', '🪑'),
    W('everyone', 'pron.', '每個人；大家', '同 everybody，動詞用單數', 'Everyone is happy today.', '今天大家都很開心。', '😄'),
    W('everybody', 'pron.', '每個人；大家', '同 everyone', 'Good morning, everybody!', '大家早安！', '👋'),
    W('everything', 'pron.', '每件事；一切', '', 'Everything is ready for the party.', '派對的一切都準備好了。', '🎉'),
    W('many', 'adj./pron.', '許多（可數）', '比較級 more、最高級 most', 'There are many books in the library.', '圖書館裡有很多書。', '📚'),
    W('most', 'adj./pron.', '大部分；最多', '', 'Most of my friends like basketball.', '我大部分的朋友都喜歡籃球。', '🏀'),
    W('nobody', 'pron.', '沒有人', '動詞用單數', 'Nobody is in the classroom now.', '現在教室裡沒有人。', '🚫'),
    W('nothing', 'pron.', '沒有東西；沒有事', '', 'There is nothing in the box.', '箱子裡什麼都沒有。', '📦'),
    W('other', 'adj./pron.', '其他的；另一個', 'one…the other… 一個…另一個…', 'I have two pens. One is red, and the other is blue.', '我有兩支筆，一支紅的，另一支藍的。', '🖊️'),
    W('part', 'n.', '部分', '', 'Part of the cake is gone.', '蛋糕有一部分不見了。', '🍰'),
    W('some', 'adj./pron.', '一些', '多用在肯定句', 'There is some milk in the glass.', '杯子裡有一些牛奶。', '🥛'),
    W('someone', 'pron.', '某人', '同 somebody', 'Someone is knocking at the door.', '有人在敲門。', '🚪'),
    W('somebody', 'pron.', '某人', '同 someone', 'Somebody left a bag on the bus.', '有人把一個包包留在公車上。', '👜'),
    W('something', 'pron.', '某事；某物', 'something + 形容詞：something new', "I want to eat something sweet.", '我想吃點甜的東西。', '🍬'),
  ],
  'focus': [
    {'title': '人稱代名詞一覽表', 'head': ('主格／受格', '所有格／所有格代名詞', '反身代名詞'), 'rows': [
      ('I／me', 'my／mine', 'myself'),
      ('you／you', 'your／yours', 'yourself（你們 yourselves）'),
      ('he／him', 'his／his', 'himself'),
      ('she／her', 'her／hers', 'herself'),
      ('it／it', 'its／its', 'itself'),
      ('we／us', 'our／ours', 'ourselves'),
      ('they／them', 'their／theirs', 'themselves'),
    ], 'note': '主格當主詞（I like him.）、受格放動詞或介系詞後面（Help me.）、所有格代名詞＝所有格＋名詞（This bag is mine.）、反身代名詞：主詞和受詞是同一個人（She looked at herself.）。'},
    {'title': 'some-、any-、every-、no- 家族', 'head': ('', '人', '東西'), 'rows': [
      ('some-（肯定句）', 'someone／somebody 某人', 'something 某物'),
      ('any-（問句、否定句）', 'anyone／anybody 任何人', 'anything 任何東西'),
      ('every-', 'everyone／everybody 每個人', 'everything 每件事'),
      ('no-', 'nobody 沒有人', 'nothing 沒有東西'),
    ], 'note': '這些字都當單數：Everyone is here. Nobody knows. 形容詞放後面：something cold、nothing new。'},
    {'title': '兩個、全部、每一個', 'head': ('說法', '意思', '例句'), 'rows': [
      ('both', '兩者都', 'Both of them are tall.'),
      ('all', '（三個以上）全部', 'All of us like music.'),
      ('each', '每一個（單數）', 'Each of the boys has a ball.'),
      ('one… the other…', '（兩個）一個…另一個…', 'One is mine, and the other is yours.'),
      ('another', '另一個；再一個', 'Try another one.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '沒有人', 'opts': ['nothing', 'nobody', 'anyone', 'none'], 'answer': 1, 'exp': 'nobody 沒有人；nothing 沒有東西。'},
    {'type': 'mc', 'q': '兩者都', 'opts': ['both', 'each', 'all', 'most'], 'answer': 0, 'exp': 'both 兩者都。'},
    {'type': 'mc', 'q': '某物', 'opts': ['anything', 'everything', 'something', 'nothing'], 'answer': 2, 'exp': 'something 某物。'},
    {'type': 'mc', 'q': '部分', 'opts': ['part', 'party', 'past', 'path'], 'answer': 0, 'exp': 'part 部分。'},
  ]},
  {'title': '② 人稱代名詞：選出正確的形式', 'items': [
    {'type': 'mc', 'q': 'This bag is not yours. It is ______.', 'opts': ['my', 'me', 'mine', 'myself'], 'answer': 2, 'exp': 'mine ＝ my bag。'},
    {'type': 'mc', 'q': 'Please help ______. I can\'t open the door.', 'opts': ['I', 'me', 'my', 'mine'], 'answer': 1, 'exp': '動詞後面用受格 me。'},
    {'type': 'mc', 'q': 'She looked at ______ in the mirror.', 'opts': ['her', 'hers', 'herself', 'she'], 'answer': 2, 'exp': '主詞和受詞同一人 → herself。'},
    {'type': 'mc', 'q': 'We cleaned the house by ______.', 'opts': ['us', 'ours', 'ourself', 'ourselves'], 'answer': 3, 'exp': 'by ourselves 我們自己。'},
    {'type': 'mc', 'q': 'Those are not our books. They are ______.', 'opts': ['their', 'theirs', 'them', 'they'], 'answer': 1, 'exp': 'theirs ＝ their books。'},
  ]},
  {'title': '③ 寫出反身代名詞', 'items': [
    {'q': 'I → {0}', 'blanks': [['myself']], 'exp': 'myself。'},
    {'q': 'he → {0}', 'blanks': [['himself']], 'exp': 'himself（不是 hisself）。'},
    {'q': 'they → {0}', 'blanks': [['themselves']], 'exp': 'themselves。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Do you have {0} questions? （任何的）', 'blanks': [['any']], 'exp': '問句用 any。'},
    {'q': 'There is {0} milk in the glass. （一些）', 'blanks': [['some']], 'exp': '肯定句用 some。'},
    {'q': 'Can I have {0} cookie? （再一個）', 'blanks': [['another']], 'exp': 'another 再一個。'},
    {'q': '{0} is ready for the party. （一切）', 'blanks': [['Everything', 'everything']], 'exp': 'everything 一切，當單數。'},
    {'q': '{0} is knocking at the door. （某人）', 'blanks': [['Someone', 'someone', 'Somebody', 'somebody']], 'exp': 'someone／somebody 某人。'},
    {'q': 'There are {0} books in the library. （許多）', 'blanks': [['many']], 'exp': 'many + 可數複數。'},
  ]},
  {'title': '⑤ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Everyone ______ here today.', 'opts': ['are', 'is', 'be', 'were'], 'answer': 1, 'exp': 'everyone 當單數 → is。'},
    {'type': 'mc', 'q': 'I have two cats. One is black, and ______ is white.', 'opts': ['another', 'other', 'the other', 'others'], 'answer': 2, 'exp': '兩個中的另一個 → the other。'},
    {'type': 'mc', 'q': 'I didn\'t see ______ in the park.', 'opts': ['somebody', 'anybody', 'everybody', 'nobody'], 'answer': 1, 'exp': '否定句用 anybody。'},
    {'type': 'mc', 'q': 'I want to drink ______.', 'opts': ['cold something', 'something cold', 'cold anything', 'nothing cold'], 'answer': 1, 'exp': '形容詞放在 something 後面。'},
    {'type': 'mc', 'q': '______ of my friends like basketball. Only two of them don\'t.', 'opts': ['Most', 'Nobody', 'Each', 'Both'], 'answer': 0, 'exp': '大部分 → most。'},
    {'type': 'mc', 'q': 'Each of the boys ______ a ball.', 'opts': ['have', 'has', 'are', 'having'], 'answer': 1, 'exp': 'each 當單數 → has。'},
    {'type': 'mc', 'q': 'The box is empty. There is ______ in it.', 'opts': ['something', 'everything', 'nothing', 'all'], 'answer': 2, 'exp': '空的 → nothing。'},
  ]},
]
