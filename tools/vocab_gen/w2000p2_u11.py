# 主題 2000 字 PART 2 Unit 11：Tableware 餐具（字表依課本 PART 2 印刷頁 151，3 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 11, 'en': 'Tableware', 'zh': '餐具',
  'intro': '吃飯、喝飲料會用到的 3 樣小東西：餐巾、小碟子、吸管。',
  'words': [
    W('napkin', 'n.', '餐巾；餐巾紙', 'paper napkin 紙巾', 'Use a napkin to wipe your mouth.', '用餐巾擦嘴巴。', '🧻'),
    W('saucer', 'n.', '茶碟；小碟子', 'cup and saucer 杯子和杯盤；flying saucer 飛碟', 'She put the cup on the saucer.', '她把杯子放在杯盤上。', '☕'),
    W('straw', 'n.', '吸管；稻草', 'a paper straw 紙吸管', 'Bubble tea needs a big straw.', '珍珠奶茶要用粗吸管。', '🥤'),
  ],
  'focus': [],
}

QUIZ = auto_quiz(UNIT['words'], seed=11, n_ce=3, n_ec=3, n_sp=3, fill=[
  F('Here is a ______. You have some ketchup on your face.', ['napkin', 'straw', 'saucer', 'fork'], 0, '擦臉上的番茄醬 → napkin。'),
  F('Can I have a ______ for my cola?', ['straw', 'saucer', 'napkin', 'spoon'], 0, '喝可樂用 straw 吸管。'),
  F('Grandma serves tea in a cup with a ______.', ['saucer', 'straw', 'napkin', 'knife'], 0, 'cup and saucer 杯子和杯盤。'),
  F('Some people say they saw a flying ______ in the sky.', ['saucer', 'napkin', 'straw', 'plate'], 0, 'flying saucer 飛碟。'),
])
