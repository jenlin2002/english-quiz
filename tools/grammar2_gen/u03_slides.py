from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '知道動名詞（V-ing）可以放在哪些位置',
    '記住後面只能接 V-ing 的動詞',
    '介系詞後面一律接 V-ing（包括 look forward to）',
    '分清楚 be used to V-ing 和 used to V',
    '知道 stop、remember、forget、try 接 to V 和 V-ing 的不同'])),
  card('暖身 3 題', qas([
    ('I enjoy ____ music. (listen / listening to)', 'listening to'),
    ('____ is good exercise. (Swim / Swimming)', 'Swimming'),
    ('Thank you for ____ me. (help / helping)', 'helping')]), 'o'))),

section('什麼是動名詞？', lead('一個句子通常只有一個主要動詞。想再放進另一個動作，就把它變成名詞：V-ing。') + table(
  ['位置', '說明', '例句'], [
  ['主詞', '動詞用單數', ('<b>Swimming</b> in the sea <b>is</b> fun.', '在海裡游泳很好玩')],
  ['補語', '放在 be 後面', ('My hobby is <b>collecting</b> stamps.', '我的嗜好是收集郵票')],
  ['動詞的受詞', 'enjoy、finish…', ('Ella enjoys <b>baking</b> cookies.', 'Ella 喜歡烤餅乾')],
  ['介系詞的受詞', 'for、at、in…', ('Thank you for <b>helping</b> me.', '謝謝你幫我')],
  ['禁止告示', 'No + V-ing', ('No <b>parking</b>.', '禁止停車')],
], audio_col=2) + note('進行式也是 V-ing，但前面有 be 動詞、表示「正在做」：He is reading.（進行式）／His job is reading news.（動名詞當補語）')),

section('後面只能接 V-ing 的動詞', cards(2,
  card('常考動詞', table(['動詞', '意思'], [
    ['enjoy', '喜歡、享受'], ['finish', '做完'], ['mind', '介意'], ['keep', '一直'],
    ['avoid', '避免'], ['quit / give up', '戒掉、放棄']]), sub='已經在做、做過的事'),
  card('例句', ex('We <b>enjoy camping</b> by the river.', '→ 喜歡露營') +
    ex('Do you <i>mind opening</i> the window?', '→ 介意開窗嗎？', 'o') +
    ex('The baby <b>kept crying</b> all night.', '→ 一直哭'), 'o', sub='examples'), tight=True) +
  note('口訣：享受完成、介意練習、一直避免、放棄討厭、承認否認、考慮懷念、建議 ＋ V-ing')),

section('介系詞後面一律接 V-ing', cards(2,
  card('介系詞 + V-ing', row('in、on、at、of、for、about、without、before、after', '') +
    ex('Wash your hands <b>before eating</b>.', '→ 吃東西前') +
    ex('She left <b>without saying</b> goodbye.', '→ 沒說再見就走了'), sub='preposition + V-ing'),
  card('形容詞 + 介系詞', table(['片語', '意思'], [
    ['be good at', '擅長'], ['be interested in', '對…有興趣'], ['be tired of', '厭倦'],
    ['be afraid of', '害怕'], ['be worried about', '擔心'], ['be worth', '值得']]) +
    ex('Ken <i>is good at drawing</i>.', '→ 擅長畫畫', 'o'), 'o', sub='常考片語'), tight=True)),

section('陷阱：這些 to 是介系詞', cards(2,
  card('to + V-ing', row('look forward to、be used to、the key to', '') +
    ex('I\'m <b>looking forward to seeing</b> you.', '→ 不是 to see') +
    ex('Amy <b>is used to getting</b> up at six.', '→ 習慣六點起床'), sub='to 後面接 V-ing'),
  card('be used to 和 used to', row('be used to + V-ing：', '習慣於（現在）') + row('used to + 原形：', '以前常常（現在不會）') +
    ex('I <i>am used to walking</i> to school.', '→ 我習慣走路上學', 'o') +
    ex('I <i>used to walk</i> to school.', '→ 我以前都走路上學', 'o'), 'o', sub='意思完全不同'))),

section('接 V-ing 的常用片語', table(['片語', '意思', '例句'], [
  ['feel like + V-ing', '想要', ('I don\'t <b>feel like going</b> out tonight.', '我今晚不想出門')],
  ['can\'t help + V-ing', '忍不住', ('We <b>couldn\'t help laughing</b>.', '我們忍不住笑了')],
  ['spend 時間 (in) + V-ing', '花時間做…', ('He <b>spends</b> two hours <b>practicing</b> the piano.', '他花兩小時練鋼琴')],
  ['have fun (in) + V-ing', '…得很開心', ('We <b>had fun playing</b> in the snow.', '我們在雪裡玩得很開心')],
  ['have trouble (in) + V-ing', '做…有困難', ('I <b>have trouble remembering</b> names.', '我很難記住名字')],
  ['How about + V-ing?', '…如何？', ('<b>How about going</b> hiking?', '去爬山如何？')],
  ['go + V-ing', '去做（休閒活動）', ('Let\'s <b>go swimming</b>.', '我們去游泳吧')],
], audio_col=2)),

section('接 to V 和 V-ing 意思不同', lead('大原則：V-ing 是「已經做的事」，to V 是「還沒做、要去做的事」。') + cards(2,
  card('stop', ex('He <b>stopped talking</b>.', '→ 停止說話') +
    ex('He <i>stopped to talk</i> to me.', '→ 停下來去跟我說話', 'o'), sub='停止 vs 停下來去做'),
  card('remember', ex('I <b>remember locking</b> the door.', '→ 記得鎖過了') +
    ex('<i>Remember to lock</i> the door.', '→ 記得要去鎖', 'o'), 'o', sub='做過 vs 要去做'),
  card('forget', ex('I\'ll never <b>forget meeting</b> you.', '→ 忘不了遇見你') +
    ex('Don\'t <i>forget to call</i> Grandma.', '→ 別忘了要打電話', 'o'), sub='做過 vs 要去做'),
  card('try', ex('<b>Try adding</b> some salt.', '→ 試試看加鹽') +
    ex('I <i>tried to open</i> the box.', '→ 努力想打開', 'o'), 'o', sub='試試看 vs 努力設法'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('I enjoy to play basketball.', 'I enjoy playing basketball.', 'enjoy 後面只能接 V-ing。'),
  ('Playing video games are fun.', 'Playing video games is fun.', '動名詞當主詞用單數動詞。'),
  ('She is good at swim.', 'She is good at swimming.', '介系詞後面接 V-ing。'),
  ('I\'m looking forward to see you.', 'I\'m looking forward to seeing you.', 'look forward to 的 to 是介系詞。'),
  ('Remember turning off the lights when you leave.', 'Remember to turn off the lights when you leave.', '「要去做」還沒做的事用 to V。'),
])),

section('快問快答 8 題', qas([
  ('Have you finished ____ the book? (read / reading)', 'reading'),
  ('Do you mind ____ me? (helping / to help)', 'helping'),
  ('He is afraid of ____ alone. (stay / staying)', 'staying'),
  ('____ English is fun. (Learn / Learning)', 'Learning'),
  ('I can\'t help ____. (cry / crying)', 'crying'),
  ('I used to ____ late. (sleep / sleeping)', 'sleep'),
  ('I\'m used to ____ late. (sleep / sleeping)', 'sleeping'),
  ('Let\'s stop ____ lunch. It\'s noon. (to have / having)', 'to have'),
])),

section('挑錯練習與下一步', two(div(lead('挑錯：每句有一個錯'), qas([
  ('He spends an hour to read every day.', 'to read → reading'),
  ('This book is worth to read.', 'to read → reading'),
  ('How about to go to the zoo?', 'to go → going'),
  ('I remember to see him last year.', 'to see → seeing'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和動詞表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '接著學 Unit 4 不定詞，把 to V 和 V-ing 一起比較']), 'o'))),
]

UNIT = {'no': 3, 'zh': '動名詞', 'en': 'Gerunds', 'c1': 'V-ing', 'c2': '當名詞', 'slides': S}
