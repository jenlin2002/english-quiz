from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '分辨可數名詞和不可數名詞',
    '正確寫出名詞的複數',
    '記住容易混淆的名詞：news、people、police、family',
    '用 many / much、a few / a little、There is / are',
    '用計量單位和所有格'])),
  card('暖身 3 題', qas([
    ('I have a lot of ____. (homework / homeworks)', 'homework'),
    ('How ____ money do you have? (many / much)', 'much'),
    ('There ____ two cats here. (is / are)', 'are')]), 'o'))),

section('可數名詞與不可數名詞', table(['種類', '說明', '例子'], [
  ['可數：普通名詞', '一個一個的人或東西', 'book, apple, student'],
  ['可數：集合名詞', '一群組成的整體', 'family, class, team, police'],
  ['不可數：物質名詞', '材料、液體、食物', 'water, milk, rice, bread, money'],
  ['不可數：抽象名詞', '看不到的概念', 'love, fun, homework, advice, information'],
  ['不可數：專有名詞', '特定的名字（大寫）', 'Taipei, Amy, Christmas'],
]) + note('不可數名詞：① 不加 a / an　② 沒有複數　③ 當主詞用單數動詞。易錯：homework、information、advice、furniture、news')),

section('可數名詞變複數', cards(2,
  card('規則', table(['字尾', '規則'], [
    ['一般', '加 -s：books'], ['s, x, sh, ch', '加 -es：boxes, dishes'], ['子音 + o', '加 -es：tomatoes'],
    ['子音 + y', '去 y 加 -ies：babies'], ['f / fe', '去 f(e) 加 -ves：leaves, knives']]), sub='regular'),
  card('不規則與同形', table(['單數', '複數'], [
    ['man / woman', 'men / women'], ['child', 'children'], ['foot / tooth', 'feet / teeth'],
    ['mouse', 'mice'], ['fish / sheep / deer', '不變']]) +
    ex('My new jeans <i>are</i> too long.', '→ jeans、shoes、glasses 常用複數', 'o'), 'o', sub='irregular'), tight=True)),

section('容易混淆的名詞', cards(2,
  card('字尾有 s 卻是單數', ex('The news <b>is</b> surprising.', '→ news 不可數') +
    ex('Math <b>is</b> my favorite subject.', '→ math、physics 單數'), sub='news, math, physics'),
  card('people、police、family', ex('There <i>are</i> five people in my family.', '→ people 是 person 的複數', 'o') +
    ex('The police <i>are</i> looking for the thief.', '→ police 一定用複數', 'o') +
    ex('My family <i>is</i> big.', '→ 看成整體用單數', 'o'), 'o', sub='集合名詞'))),

section('數量詞：many、much、few、little', table(['意思', '可數（複數）', '不可數', '兩種都可以'], [
  ['很多', 'many', 'much', 'a lot of / lots of'],
  ['一些（還有）', 'a few', 'a little', 'some / any'],
  ['很少（幾乎沒有）', 'few', 'little', '—'],
  ['問多少', 'How many…?', 'How much…?', '—'],
]) + '<div style="height:calc(var(--u)*1.4)"></div>' + cards(2,
  card('a few 和 few', ex('I have <b>a few</b> friends here.', '→ 有幾個（正面）') +
    ex('He has <b>few</b> friends.', '→ 幾乎沒有（負面）')),
  card('a little 和 little', ex('There is <i>a little</i> milk left.', '→ 還有一點', 'o') +
    ex('We have <i>little</i> time.', '→ 沒什麼時間了', 'o'), 'o'), tight=True)),

section('There is / There are', cards(2,
  card('動詞看後面第一個名詞', ex('There <b>is</b> some milk in the fridge.', '→ 不可數用 is') +
    ex('There <b>are</b> a few eggs in the basket.', '→ 複數用 are') +
    ex('There <b>is</b> a pen and two books on the desk.', '→ 緊接的是 a pen'), sub='There + be'),
  card('問句和否定句用 any', ex('<i>Is</i> there <i>any</i> juice?', '→ 不可數', 'o') +
    ex('<i>Are</i> there <i>any</i> apples?', '→ 複數', 'o') +
    ex('There <i>aren\'t any</i> chairs.', '→ 否定', 'o'), 'o', sub='some → any'))),

section('不可數名詞的計量單位', table(['單位', '例子', '例句'], [
  ['a glass of / a cup of', 'two glasses of water', ('I drink <b>two glasses of water</b> every morning.', '我每天早上喝兩杯水')],
  ['a bottle of / a bowl of', 'a bowl of rice', ('He ate <b>two bowls of rice</b>.', '他吃了兩碗飯')],
  ['a piece of / a slice of', 'a piece of cake', ('Can I have <b>a piece of cake</b>?', '我可以吃一塊蛋糕嗎？')],
  ['a pair of', 'a pair of shoes', ('I need <b>a new pair of shoes</b>.', '我需要一雙新鞋')],
], audio_col=2) + note('變複數的是單位，不是名詞：two cups of tea（不是 teas）')),

section('名詞的所有格', table(['情況', '寫法', '例子'], [
  ['單數名詞', '加 \'s', 'the boy\'s hat'],
  ['字尾有 s 的複數', '只加 \'', 'my parents\' car'],
  ['不規則複數', '加 \'s', 'the children\'s toys'],
  ['共同擁有', '最後一個加 \'s', 'Tom and Amy\'s mother'],
  ['各自擁有', '每個都加 \'s', 'Tom\'s and Amy\'s bikes'],
  ['時間', '加 \'s', 'today\'s newspaper'],
  ['無生物', 'the … of …', 'the name of the school'],
])),

section('學生最常錯的 5 句', top5([
  ('I have a lot of homeworks.', 'I have a lot of homework.', 'homework 不可數。'),
  ('The news are exciting.', 'The news is exciting.', 'news 用單數動詞。'),
  ('How many money do you have?', 'How much money do you have?', 'money 不可數用 much。'),
  ('I\'d like two cups of teas.', 'I\'d like two cups of tea.', '單位變複數，tea 不變。'),
  ('This is my parent\'s car.（爸媽的）', 'This is my parents\' car.', 'parents 字尾有 s，只加 \'。'),
])),

section('快問快答 8 題', qas([
  ('two ____ (knife)', 'knives'),
  ('three ____ (child)', 'children'),
  ('some ____ (advice)', 'advice'),
  ('How ____ eggs? (many / much)', 'many'),
  ('There ____ some bread. (is / are)', 'is'),
  ('He has ____ friends. He\'s lonely. (few / a few)', 'few'),
  ('a piece of ____ (paper / papers)', 'paper'),
  ('the ____ room (girls / girls\')', 'girls\''),
])),

section('改寫練習與下一步', two(div(lead('依照提示改寫'), qas([
  ('There is a box. （改成三個）', 'There are three boxes.'),
  ('There is some milk.（改成問句）', 'Is there any milk?'),
  ('I have three cousins.（問數量）', 'How many cousins do you have?'),
  ('He has almost no time.', 'He has little time.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的規則表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 7 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 8, 'zh': '名詞', 'en': 'Nouns', 'c1': '可數', 'c2': '不可數', 'slides': S}
