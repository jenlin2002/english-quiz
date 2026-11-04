# 主題 2000 字 Unit 13：Colors 顏色（字表依課本單元；詞性、中文、例句、題目為本站自編）
def C(w, zh, note, ex, exzh, pic, pos='adj./n.'):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 13, 'en': 'Colors', 'zh': '顏色',
  'intro': '12 個顏色的字。顏色可以當形容詞（a red apple），也可以當名詞（Red is my favorite.），還有幾個常用的片語。',
  'words': [
    C('black', '黑色（的）', 'black sheep 害群之馬', 'My cat is black, so it is hard to see at night.', '我的貓是黑色的，所以晚上很難看到牠。', '⚫'),
    C('blue', '藍色（的）', 'feel blue 心情低落', 'The sea looks so blue on a sunny day.', '晴天時大海看起來好藍。', '🔵'),
    C('brown', '咖啡色（的）；棕色（的）', 'brown sugar 黑糖', 'He put on his brown shoes.', '他穿上他的咖啡色鞋子。', '🟤'),
    C('color', '顏色', 'What color…? 什麼顏色', 'What color is your new bike?', '你的新腳踏車是什麼顏色？', '🎨', pos='n.'),
    C('gray', '灰色（的）', 'gray hair 白頭髮', 'The sky turned gray before the rain.', '下雨前天空變成灰色。', '🩶'),
    C('green', '綠色（的）', 'green hand 新手', 'Traffic lights turn green, and we can cross the street.', '紅綠燈變綠了，我們可以過馬路。', '🟢'),
    C('orange', '橘色（的）', '也當名詞「柳橙」', 'The leaves turn orange in the fall.', '秋天葉子變成橘色。', '🟠'),
    C('pink', '粉紅色（的）', '', 'She has a pink umbrella.', '她有一把粉紅色的雨傘。', '🩷'),
    C('purple', '紫色（的）', '', 'Grapes can be green or purple.', '葡萄可能是綠色或紫色的。', '🟣'),
    C('red', '紅色（的）', 'turn red 臉紅', 'Stop! The light is red.', '停！現在是紅燈。', '🔴'),
    C('white', '白色（的）', 'white lie 善意的謊言', 'Snow is white and cold.', '雪又白又冷。', '⚪'),
    C('yellow', '黃色（的）', '', 'Bananas turn yellow when they are ripe.', '香蕉熟了會變黃色。', '🟡'),
  ],
  'focus': [
    {'title': '顏色的兩種用法', 'head': ('用法', '例子', '中文'), 'rows': [
      ('形容詞：放在名詞前', 'a red apple', '一顆紅蘋果'),
      ('形容詞：放在 be 動詞後', 'The apple is red.', '這顆蘋果是紅的。'),
      ('名詞：當主詞', 'Blue is my favorite color.', '藍色是我最喜歡的顏色。'),
      ('問顏色', 'What color is it? — It is green.', '它是什麼顏色？——綠色。'),
    ], 'note': '問顏色用 What color…?，回答時顏色前面不加 a：It is green.（不是 a green）'},
    {'title': '和顏色有關的片語', 'head': ('片語', '意思', ''), 'rows': [
      ('black sheep', '害群之馬', ''),
      ('feel blue', '心情低落', ''),
      ('brown sugar', '黑糖', ''),
      ('green hand', '新手', ''),
      ('turn red', '臉紅；變紅', ''),
      ('white lie', '善意的謊言', ''),
    ], 'note': '這些片語不能照字面翻譯，要整個記起來。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '紫色', 'opts': ['pink', 'purple', 'brown', 'gray'], 'answer': 1, 'exp': 'purple 紫色；pink 是粉紅色。'},
    {'type': 'mc', 'q': '灰色', 'opts': ['green', 'yellow', 'gray', 'white'], 'answer': 2, 'exp': 'gray 灰色。'},
    {'type': 'mc', 'q': '咖啡色；棕色', 'opts': ['brown', 'black', 'orange', 'blue'], 'answer': 0, 'exp': 'brown 咖啡色、棕色。'},
    {'type': 'mc', 'q': '顏色', 'opts': ['colder', 'cooler', 'collar', 'color'], 'answer': 3, 'exp': 'color 顏色。'},
    {'type': 'mc', 'q': '粉紅色', 'opts': ['purple', 'pink', 'red', 'white'], 'answer': 1, 'exp': 'pink 粉紅色。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'yellow', 'opts': ['綠色', '橘色', '黃色', '白色'], 'answer': 2, 'exp': 'yellow 黃色。'},
    {'type': 'mc', 'q': 'orange', 'opts': ['橘色；柳橙', '紅色', '咖啡色', '紫色'], 'answer': 0, 'exp': 'orange 橘色；也當名詞「柳橙」。'},
    {'type': 'mc', 'q': 'black', 'opts': ['藍色', '灰色', '白色', '黑色'], 'answer': 3, 'exp': 'black 黑色。'},
    {'type': 'mc', 'q': 'green', 'opts': ['藍色', '綠色', '黃色', '灰色'], 'answer': 1, 'exp': 'green 綠色。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '紫色（p＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['purple']], 'exp': 'purple。'},
    {'q': '黃色（y＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['yellow']], 'exp': 'yellow。'},
    {'q': '白色（w＿＿＿＿，5 個字母）：{0}', 'blanks': [['white']], 'exp': 'white，h 不太發音。'},
    {'q': '咖啡色（b＿＿＿＿，5 個字母）：{0}', 'blanks': [['brown']], 'exp': 'brown。'},
    {'q': '灰色（g＿＿＿，4 個字母）：{0}', 'blanks': [['gray', 'grey']], 'exp': 'gray（英式拼法 grey 也對）。'},
  ]},
  {'title': '④ 例句填空：寫出正確的顏色', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Stop! The traffic light is {0}. （紅色的）', 'blanks': [['red']], 'exp': '紅燈 → red。'},
    {'q': 'The sky is {0} and clear today. （藍色的）', 'blanks': [['blue']], 'exp': '藍天 → blue。'},
    {'q': 'Snow is {0}. （白色的）', 'blanks': [['white']], 'exp': '雪是白色的 → white。'},
    {'q': 'What {0} is your schoolbag? （顏色）', 'blanks': [['color', 'colour']], 'exp': '問顏色 What color…?'},
    {'q': 'Leaves are {0} in spring. （綠色的）', 'blanks': [['green']], 'exp': '春天的葉子是綠色 → green。'},
  ]},
  {'title': '⑤ 片語與用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Tom is new here. He is still a ______ hand.', 'opts': ['red', 'green', 'white', 'black'], 'answer': 1, 'exp': 'green hand 新手。'},
    {'type': 'mc', 'q': 'I told a ______ lie because I didn\'t want to hurt her feelings.', 'opts': ['white', 'black', 'blue', 'gray'], 'answer': 0, 'exp': 'white lie 善意的謊言。'},
    {'type': 'mc', 'q': 'Her face ______ red when everyone looked at her.', 'opts': ['made', 'took', 'turned', 'gave'], 'answer': 2, 'exp': 'turn red 臉紅。'},
    {'type': 'mc', 'q': 'A: What color is your cat?  B: It is ______.', 'opts': ['a black', 'blacks', 'the black', 'black'], 'answer': 3, 'exp': '回答顏色不加 a：It is black.'},
    {'type': 'mc', 'q': 'Mom puts ______ sugar in the ginger tea.', 'opts': ['brown', 'pink', 'purple', 'green'], 'answer': 0, 'exp': 'brown sugar 黑糖。'},
  ]},
]
