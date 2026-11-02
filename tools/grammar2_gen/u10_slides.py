from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '把形容詞放在正確的位置（something cold、a ten-year-old boy）',
    '寫出比較級和最高級（含不規則變化）',
    '用 as…as、比較級 than、the 最高級 in / of',
    '用 than any other、one of the 最高級 表達「最…」',
    '用 much 修飾比較級、說「越來越…」「越…越…」'])),
  card('暖身 3 題', qas([
    ('A cat is ____ than a mouse. (big / bigger)', 'bigger'),
    ('He is the ____ in his class. (tallest / taller)', 'tallest'),
    ('I want something ____. (hot / hotly)', 'hot')]), 'o'))),

section('形容詞的位置', cards(2,
  card('三個位置', row('① 名詞前面', '') + ex('This is an <b>easy</b> question.', '→ 最常見') +
    row('② be、連綴動詞後面', '') + ex('You look <b>tired</b>.', '→ look、feel、get…') +
    row('③ something、anything 後面', '') + ex('I want something <b>cold</b>.', '→ 不說 cold something'), sub='position'),
  card('數字 + 名詞當形容詞', row('名詞用單數、加連字號', '') +
    ex('a <i>ten-year-old</i> boy', '→ 不說 ten-years-old', 'o') +
    ex('a <i>two-week</i> vacation', '→ 兩週的假期', 'o') +
    ex('The boy is <i>ten years old</i>.', '→ 放在後面才用複數', 'o'), 'o', sub='a ten-year-old boy'))),

section('分詞當形容詞與形容詞片語', cards(2,
  card('V-ing 和 p.p.', row('V-ing：', '主動、正在…') + row('p.p.：', '被動、已經…') +
    ex('a <b>crying</b> baby', '→ 正在哭的寶寶') +
    ex('a <b>broken</b> window', '→ 被打破的窗戶') +
    ex('The girl <b>playing the piano</b> is my sister.', '→ 分詞片語放名詞後面'), sub='participles'),
  card('be + 形容詞 + 介系詞', table(['片語', '意思'], [
    ['be proud of', '以…為傲'], ['be famous for', '以…聞名'], ['be late for', '…遲到'],
    ['be different from', '和…不同'], ['be full of', '充滿'], ['be kind to', '對…好']]), 'o', sub='常考片語'), tight=True)),

section('原級、比較級、最高級', cards(2,
  card('規則變化', table(['規則', '例子'], [
    ['加 -er / -est', 'tall → taller → tallest'], ['e 結尾加 -r / -st', 'nice → nicer → nicest'],
    ['子音 + y → -ier / -iest', 'easy → easier → easiest'], ['重複字尾', 'big → bigger → biggest'],
    ['多音節 more / most', 'beautiful → more beautiful']]), sub='regular'),
  card('不規則變化', table(['原級', '比較級', '最高級'], [
    ['good / well', 'better', 'best'], ['bad', 'worse', 'worst'], ['many / much', 'more', 'most'],
    ['little', 'less', 'least'], ['far', 'farther', 'farthest']]), 'o', sub='一定要背'), tight=True)),

section('原級與比較級', cards(2,
  card('as … as：一樣', ex('Ken is <b>as tall as</b> his father.', '→ 一樣高') +
    ex('This test is <b>not as hard as</b> the last one.', '→ 沒有那麼難') +
    ex('My room is <b>twice as big as</b> yours.', '→ 倍數放 as 前面'), sub='中間用原級'),
  card('比較級 than：兩個比', ex('Tom is <i>taller than</i> Ben.', '→ 比較高', 'o') +
    ex('Math is <i>more difficult than</i> English.', '→ 多音節用 more', 'o') +
    ex('Amy is <i>the taller of the two</i>.', '→ 兩者中比較高的', 'o') +
    ex('Taipei is hotter than <i>that</i> in Tokyo.', '→ 比同類：that = the weather', 'o'), 'o', sub='comparative'))),

section('最高級的各種說法', table(['句型', '例句'], [
  ['the + 最高級 + in / of', ('Jade Mountain is <b>the highest</b> mountain <b>in</b> Taiwan.', '玉山是台灣最高的山')],
  ['比較級 + than any other + 單數', ('He is <b>taller than any other boy</b> in our class.', '他比班上其他男生都高')],
  ['No other + 單數 + 比較級 + than', ('<b>No other boy</b> in our class <b>is taller than</b> he.', '班上沒有男生比他高')],
  ['one of the + 最高級 + 複數', ('She is <b>one of the best singers</b> in Taiwan.', '她是台灣最棒的歌手之一')],
], audio_col=1) + note('than any other 後面接單數名詞，而且一定要有 other（不能和自己比）。')),

section('修飾比較級、越來越、越…越…', cards(2,
  card('much / far / a lot + 比較級', ex('Today is <b>much colder</b> than yesterday.', '→ 冷得多') +
    ex('I feel <b>a little better</b> now.', '→ 好一點') +
    row('注意：', 'very 只能修飾原級：very cold ✓　very colder ✗'), sub='…得多'),
  card('越來越、越…越…', ex('It\'s getting <i>colder and colder</i>.', '→ 越來越冷', 'o') +
    ex('English is <i>more and more</i> important.', '→ 越來越重要', 'o') +
    ex('<i>The more</i> you practice, <i>the better</i> you get.', '→ 越練越好', 'o'), 'o', sub='比較級 and 比較級'))),

section('It is + 形容詞 + of / for + 人 + to V', table(['介系詞', '形容詞描述', '例句'], [
  ['of', '人的個性：kind、nice、polite、careless', ('It is <b>kind of you</b> to help me.', '你真好心幫我')],
  ['for', '事情的性質：easy、hard、important', ('It is <b>hard for me</b> to wake up early.', '對我來說早起很難')],
], audio_col=2) + note('判斷方法：You are kind. 說得通 → of；I am hard. 說不通 → for。')),

section('學生最常錯的 5 句', top5([
  ('She is more taller than me.', 'She is taller than me.', '-er 和 more 不能一起用。'),
  ('He is as taller as his brother.', 'He is as tall as his brother.', 'as…as 中間用原級。'),
  ('Today is very hotter than yesterday.', 'Today is much hotter than yesterday.', '比較級用 much 修飾。'),
  ('He is taller than any boy in his class.', 'He is taller than any other boy in his class.', '要加 other。'),
  ('She is one of the best singer.', 'She is one of the best singers.', 'one of the 最高級 + 複數。'),
])),

section('快問快答 8 題', qas([
  ('This box is ____ than that one. (heavy / heavier)', 'heavier'),
  ('She is the ____ girl in her class. (prettier / prettiest)', 'prettiest'),
  ('My score is ____ than yours. (good / better)', 'better'),
  ('He is as ____ as me. (busy / busier)', 'busy'),
  ('It\'s ____ warmer today. (very / much)', 'much'),
  ('a ____ girl (five-years-old / five-year-old)', 'five-year-old'),
  ('It\'s nice ____ you to come. (of / for)', 'of'),
  ('The ____ you eat, the fatter you get. (more / most)', 'more'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('Tom is shorter than Ben.', 'Ben is taller than Tom.'),
  ('Amy is not as tall as Lily.', 'Lily is taller than Amy.'),
  ('He is the fastest on the team.', 'He is faster than any other player on the team.'),
  ('You practice more. You get better.', 'The more you practice, the better you get.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的比較句型表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 4 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 10, 'zh': '形容詞', 'en': 'Adjectives', 'c1': '比較級', 'c2': '最高級', 'slides': S}
