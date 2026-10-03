from sl import *

W = 18
T = '主詞動詞一致、代名詞與限定詞'

S = [
title(W, T, 'Agreement, Pronouns &amp; Determiners', 'Everyone is…', 'the other / others'),

section('本週目標與暖身', cards(2,
  card('本週目標', ul([
    '判斷主詞是單數還是複數：each、every、everyone、a number of、the number of',
    '主詞後面有 with、as well as、along with 時，動詞看前面的主詞',
    '金額、時間、距離、科目名稱當成單數；the + 形容詞當成複數',
    '分清楚 another、the other、others、the others，以及 one / ones',
    '數量詞：few / a few、little / a little、both / all / either / neither / none'])),
  card('暖身 3 題', qas([
    ('Everyone ____ here. (is / are)', 'is'),
    ('A number of students ____ absent. (was / were)', 'were'),
    ('I have two pens. One is red, and ____ is blue. (the other / another)', 'the other')]), 'o'))),

section('回收：第 17 週的倒裝與強調', lead('倒裝句的主詞跑到動詞後面，更要看清楚主詞是單數還是複數。') + cards(2,
  card('第 17 週回顧',
    ex('<b>Never have I</b> seen such a big dog.', '→ 否定副詞倒裝') +
    ex('<i>It was</i> my mother <i>who</i> cooked dinner.', '→ 強調句', 'o')),
  card('這週的延伸',
    ex('Here <b>comes</b> the bus. Here <b>come</b> the students.', '→ 動詞看後面的主詞：bus 單數、students 複數') +
    ex('<i>Each</i> of the students <i>has</i> a book.', '→ each 當主詞，動詞用單數', 'o'), 'o'))),

section('一定用單數的主詞', cards(2,
  card('each、every、-one、-body、-thing', row('單數：', 'each、every + 名詞、everyone、somebody、nothing…') + row('each of + 複數名詞：', '動詞還是單數') +
    ex('<b>Everyone is</b> ready for the trip.', '→ 每個人都準備好了') +
    ex('<b>Each of the students has</b> a laptop.', '→ 每個學生都有一台筆電') +
    ex('<b>Every boy and girl needs</b> love.', '→ every A and B 也用單數'), sub='看起來很多，其實是「每一個」'),
  card('金額、時間、距離、學科', row('一個整體：', 'Ten dollars、Two hours、Five kilometers → 單數') + row('-s 結尾但是單數：', 'news、mathematics、physics') +
    ex('<i>Ten dollars is</i> too much for a pen.', '→ 十元買一支筆太貴了', 'o') +
    ex('<i>Two hours is</i> enough for the test.', '→ 兩小時考試夠了', 'o') +
    ex('<i>The news was</i> surprising.', '→ news 是不可數名詞', 'o'), 'o', sub='當成一個整體'))),

section('一定用複數，或要看情況的主詞', table(['主詞', '動詞', '例句'], [
  ['a number of + 複數名詞', '複數（很多）', ('<b>A number of</b> students <b>are</b> absent today.', '今天很多學生缺席')],
  ['the number of + 複數名詞', '單數（數目）', ('<b>The number of</b> students <b>is</b> forty.', '學生的人數是四十人')],
  ['the + 形容詞', '複數（一群人）', ('<b>The rich are</b> not always happy.', '有錢人不一定快樂')],
  ['police、people、cattle', '複數', ('<b>The police are</b> looking for the thief.', '警察正在找小偷')],
  ['family、team、class', '當整體用單數', ('My <b>family is</b> large.', '我家是個大家庭')],
], audio_col=2) + note('口訣：a number of 是「很多」→ 複數；the number of 是「數目」→ 單數。')),

section('主詞後面有修飾語：動詞看「真正的主詞」', cards(2,
  card('with、as well as、along with', row('規則：', '動詞看前面的主詞，後面的人不算') +
    ex('The teacher, <b>as well as</b> the students, <b>is</b> excited.', '→ 主詞是 the teacher') +
    ex('Tom, <b>along with</b> his friends, <b>was</b> late.', '→ 主詞是 Tom') +
    ex('The box <b>of</b> apples <b>is</b> heavy.', '→ 主詞是 the box，不是 apples'), sub='插入語不影響動詞'),
  card('就近原則（第 16 週回收）', row('either…or / neither…nor：', '動詞看最近的主詞') + row('There is / are：', '動詞看後面第一個名詞') +
    ex('<i>Neither</i> my parents <i>nor</i> my sister <i>is</i> at home.', '→ 看 my sister', 'o') +
    ex('<i>There is</i> a pen and two books on the desk.', '→ 看 a pen', 'o') +
    ex('<i>There are</i> two books and a pen on the desk.', '→ 看 two books', 'o'), 'o', sub='看最靠近動詞的那一個'))),

section('another、the other、others、the others', table(['用法', '意思', '例句'], [
  ['one…the other', '兩個中的一個…另一個', ('I have two cats. <b>One</b> is white, and <b>the other</b> is black.', '我有兩隻貓，一隻白的，另一隻黑的')],
  ['another', '（不特定的）另一個', ('This cake is great. Can I have <b>another</b>?', '這蛋糕很好吃，可以再一個嗎？')],
  ['some…others', '一些…另一些（不是全部）', ('<b>Some</b> students like math; <b>others</b> like English.', '有些學生喜歡數學，有些喜歡英文')],
  ['some…the others', '一些…其餘全部', ('Five boys came. Two stayed, and <b>the others</b> left.', '五個男生來了，兩個留下，其餘的離開')],
], audio_col=2) + note('有 the 就是「剩下的全部」：兩個用 the other，三個以上剩下的全部用 the others。')),

section('代名詞 one / ones、it 與反身代名詞', cards(2,
  card('one / ones 與 it', row('one / ones：', '同類的另一個（複數用 ones）') + row('it：', '就是「那一個」（同一個）') +
    ex('I lost my umbrella. I need to buy a new <b>one</b>.', '→ 買一把新的（不是同一把）') +
    ex('I lost my umbrella, but I found <b>it</b> later.', '→ 找到的是同一把') +
    ex('I don\'t like the red shoes. I like the black <b>ones</b>.', '→ ones = shoes'), sub='同一個還是同一類'),
  card('反身代名詞與 each other', row('反身：', 'myself、yourself、himself、themselves…') + row('each other：', '彼此（兩者以上都可以）') +
    ex('She taught <i>herself</i> to play the guitar.', '→ 她自學吉他', 'o') +
    ex('Help <i>yourself</i> to some cake.', '→ 自己拿蛋糕吃', 'o') +
    ex('The two friends help <i>each other</i>.', '→ 兩個朋友互相幫忙', 'o'), 'o', sub='主詞和受詞是同一人'), tight=True)),

section('限定詞：few、little、both、all、either、neither、none', cards(2,
  card('few / a few、little / a little', row('可數：', 'a few（一些）、few（幾乎沒有）') + row('不可數：', 'a little（一點）、little（幾乎沒有）') +
    ex('I have <b>a few</b> friends here.', '→ 我在這裡有幾個朋友（正面）') +
    ex('<b>Few</b> people came to the party.', '→ 幾乎沒什麼人來（負面）') +
    ex('There is <b>little</b> milk left.', '→ 幾乎沒剩牛奶了'), sub='有 a 正面、沒 a 負面'),
  card('兩個 vs 三個以上', row('兩個：', 'both（都）、either（任一）、neither（都不）') + row('三個以上：', 'all（都）、any（任一）、none（都不）') +
    ex('<i>Both</i> of my parents <i>are</i> teachers.', '→ 兩個都', 'o') +
    ex('<i>Neither</i> of the answers <i>is</i> correct.', '→ 兩個都不對（neither of + 複數，動詞常用單數）', 'o') +
    ex('<i>None</i> of the five students <i>was</i> late.', '→ 五個學生中沒有人遲到', 'o'), 'o', sub='先數一數有幾個'))),

section('對比頁：容易搞混的四組', two(
  card('a number of 與 the number of', ex('<b>A number of</b> cars <b>are</b> on the road.', '→ 很多車，複數') + ex('<i>The number of</i> cars <i>is</i> growing.', '→ 車的數目，單數', 'o')),
  card('the other 與 another', ex('One is mine; <b>the other</b> is yours.', '→ 兩個中剩下的那個') + ex('Can I have <i>another</i> cookie?', '→ 再一個（不特定）', 'o'), 'o'), tight=True) + two(
  card('a few 與 few', ex('I have <b>a few</b> questions.', '→ 我有幾個問題') + ex('<i>Few</i> students knew the answer.', '→ 幾乎沒有學生知道', 'o')),
  card('one 與 it', ex('I need a pen. Can you lend me <b>one</b>?', '→ 任何一支筆') + ex('Where is my pen? I can\'t find <i>it</i>.', '→ 就是我那支筆', 'o'), 'o'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('Everyone are happy today.', 'Everyone is happy today.', 'everyone 是單數，動詞用 is。'),
  ('The number of students are forty.', 'The number of students is forty.', 'the number of 指「數目」，動詞用單數。'),
  ('The teacher, as well as the students, are here.', 'The teacher, as well as the students, is here.', 'as well as 不影響動詞，主詞是 the teacher。'),
  ('I have two sisters. One is a nurse, and another is a cook.', 'I have two sisters. One is a nurse, and the other is a cook.', '兩個中的另一個用 the other。'),
  ('There is little apples in the box.', 'There are few apples in the box.', 'apples 可數，要用 few，動詞也要用 are。'),
])),

section('快問快答 8 題', qas([
  ('Each of the boys ____ a bike. (has / have)', 'has'),
  ('The police ____ coming. (is / are)', 'are'),
  ('Mathematics ____ my favorite subject. (is / are)', 'is'),
  ('The young ____ full of energy. (is / are)', 'are'),
  ('Some like tea; ____ like coffee. (others / the other)', 'others'),
  ('My phone is old. I want a new ____. (one / it)', 'one'),
  ('There is ____ water in the bottle. (a few / a little)', 'a little'),
  ('____ of my two brothers can swim. (Neither / None)', 'Neither'),
])),

section('挑錯練習與句型轉換', two(div(lead('挑錯：每句有一個錯'), qas([
  ('Five hundred dollars are too expensive.', 'are → is'),
  ('Tom, along with his parents, are coming.', 'are → is'),
  ('None of the two answers is correct.', 'None → Neither'),
])), div(lead('依提示改寫'), qas([
  ('Many students are absent.（用 A number of）', 'A number of students are absent.'),
  ('I have three pens: one red pen and two blue pens.（用 the others）', 'One is red, and the others are blue.'),
  ('There are almost no people in the park.（用 few）', 'There are few people in the park.'),
])))),

section('在閱讀與聽力裡找到它', passage(
  '<span class="hl">The number of</span> students who walk to school <span class="hl">is</span> falling. <span class="hl">A number of</span> parents <span class="hl">drive</span> their children every day. <span class="hl2">Each</span> of these trips <span class="hl2">adds</span> to the traffic. Some families have started walking groups; <span class="hl2">others</span> share cars. <span class="hl">Neither</span> idea <span class="hl">is</span> perfect, but both help.') +
  cards(2,
    card('閱讀怎麼用', ul(['先找真正的主詞，跳過 of…、as well as…、with… 這些修飾語', 'The number of 常出現在報告和圖表題', 'some…others 表示兩種不同的人，題目常考「其他人做什麼」'])),
    card('聽力怎麼用', ul(['聽到 a few / a little 是「有一些」，few / little 是「幾乎沒有」', '聽到 neither / none，表示都沒有', '聽到 the other，就是兩個中的另一個']), 'o'))),

section('口說句型跟讀', lead('先按 🔊 聽，再跟著大聲念，最後換成自己的句子。') + two(div(
  ex('<b>Everyone</b> in my family <b>loves</b> music.', '→ everyone + 單數動詞'),
  ex('<b>A number of</b> my classmates <b>play</b> basketball.', '→ a number of + 複數動詞'),
  ex('I have two hobbies. <b>One</b> is reading, and <b>the other</b> is swimming.', '→ one…the other')), div(
  ex('<i>Some</i> of my friends like rock music; <i>others</i> like pop.', '→ some…others', 'o'),
  ex('I have <i>a few</i> good friends, and we help <i>each other</i>.', '→ a few、each other', 'o')))),

section('重點整理與測驗說明', two(div(
  table(['重點', '規則'], [
    ['單數主詞', 'each、every、-one、-body、金額、時間、news、學科'],
    ['複數主詞', 'a number of、the + 形容詞、police、people'],
    ['插入語', 'as well as、with、along with 不影響動詞'],
    ['the other / others', '有 the 是剩下全部；兩個用 the other'],
    ['one / it', 'one 是同類，it 是同一個'],
    ['few / little', '有 a 正面、沒 a 負面；few 可數、little 不可數']]),
  note('口訣：找主詞、跳插入；每一個用單數；剩下全部加 the；有 a 是有、沒 a 是沒有。')), div(
  card('本週測驗：64 題', row('題型：', '文法 20．閱讀 10．克漏字 4．單字 10．聽力 15．口說 5') + ul(['文法 20 題中，16 題是本週新教，4 題回收第 17 週倒裝與強調句']), 'o'),
  card('回家作業', ol(['用 Everyone in my family… 和 A number of… 各寫一句。', '用 one…the other 介紹你的兩樣東西。', '用 a few 和 little 各寫一句，描述你的房間。']))))),
]
