from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '用不定詞當名詞、形容詞、副詞',
    '記住後面接 to V 的動詞，和「動詞 + 人 + to V」',
    '用「疑問詞 + to V」說「該…」',
    '會用 It is…to V、too…to、enough to',
    '分清楚什麼時候用 to V、什麼時候用 V-ing'])),
  card('暖身 3 題', qas([
    ('I want ____ a pilot. (be / to be)', 'to be'),
    ('Is there anything ____? (eat / to eat)', 'to eat'),
    ('She went out ____ some bread. (buy / to buy)', 'to buy')]), 'o'))),

section('不定詞的三種用法', lead('不定詞 = to + 原形動詞。to 後面一定是原形。') + cards(3,
  card('① 當名詞', row('做某件事', '') +
    ex('Leo wants <b>to be</b> a doctor.', '→ 當受詞') +
    ex('<b>It</b> takes time <b>to learn</b> a language.', '→ 主詞常用 It 代替'), sub='做某件事'),
  card('② 當形容詞', row('放在名詞後面', '') +
    ex('Is there anything <i>to eat</i>?', '→ 可以吃的東西', 'o') +
    ex('I have a lot of homework <i>to do</i>.', '→ 要做的功課', 'o'), 'o', sub='用來做…的'),
  card('③ 當副詞', row('目的、情緒的原因', '') +
    ex('I got up early <b>to catch</b> the bus.', '→ 為了趕公車') +
    ex('We were happy <b>to hear</b> the news.', '→ 因為聽到而高興'), sub='為了…、因為…'), tight=True) +
  note('當形容詞時，介系詞要保留：a chair to sit on、someone to talk to、paper to write on')),

section('後面接 to V 的動詞', cards(2,
  card('常考動詞', table(['動詞', '意思'], [
    ['want / would like', '想要'], ['hope', '希望'], ['decide', '決定'], ['plan', '計畫'],
    ['agree / refuse', '同意／拒絕'], ['promise', '答應']]), sub='打算、還沒做的事'),
  card('例句', ex('They <b>decided to stay</b> home.', '→ 決定待在家') +
    ex('He <i>refused to answer</i> the question.', '→ 拒絕回答', 'o') +
    ex('Dad <b>promised to take</b> us to the zoo.', '→ 答應帶我們去'), 'o', sub='examples'), tight=True) +
  note('對照記：enjoy、finish、mind、keep、avoid 接 V-ing（Unit 3）。')),

section('動詞 + 人 + to V', cards(2,
  card('要別人去做', row('ask、tell、want、would like、expect、teach、remind', '') +
    ex('Mom <b>asked me to buy</b> some eggs.', '→ 媽媽叫我去買蛋') +
    ex('The coach <b>wants us to practice</b> more.', '→ 教練要我們多練習'), sub='人放中間'),
  card('否定：not 放在 to 前面', ex('The teacher <i>told us not to run</i>.', '→ 叫我們不要跑', 'o') +
    ex('Please <i>remind me not to forget</i> my key.', '→ 提醒我別忘了鑰匙', 'o') +
    row('例外：', 'make、let、have、see、hear + 人 + 原形（不加 to，見 Unit 5）'), 'o', sub='not to V'))),

section('疑問詞 + to V：該…', cards(2,
  card('what / how / where / when / which', ex('I don\'t know <b>what to say</b>.', '→ 不知道該說什麼') +
    ex('Can you show me <b>how to use</b> this app?', '→ 怎麼用') +
    ex('We haven\'t decided <b>where to go</b>.', '→ 要去哪裡'), sub='常接在 know、decide、show、tell 後面'),
  card('改寫成名詞子句', row('疑問詞 + to V = 疑問詞 + 主詞 + should + V', '') +
    ex('I don\'t know <i>what I should say</i>.', '→ 和 what to say 意思一樣', 'o') +
    row('注意：', 'why 不能接 to V') +
    '<div class="ex o"><div class="en"><span class="bad">I don\'t know why to go.</span></div><div class="zh">→ 要說 why I should go</div></div>', 'o', sub='should'))),

section('It is…to V 與 too…to', cards(2,
  card('It is + 形容詞 + (for 人) + to V', ex('<b>It is</b> important <b>to wear</b> a helmet.', '→ 戴安全帽很重要') +
    ex('<b>It is</b> hard <b>for me to</b> wake up early.', '→ 對我來說早起很難'), sub='It 代替後面的 to V'),
  card('too + 形容詞 + to V：太…而不能', ex('The box is <i>too heavy</i> for me <i>to carry</i>.', '→ 太重了，搬不動', 'o') +
    ex('= The box is <i>so</i> heavy <i>that</i> I <i>can\'t</i> carry it.', '→ 改成 so…that 要補 can\'t 和 it', 'o'), 'o', sub='沒有 not，卻是否定意思'))),

section('enough 的位置與 need + V-ing', cards(2,
  card('enough', row('形容詞 + enough + to V：', '夠…可以…') + row('enough + 名詞 + to V：', '有足夠的…可以…') +
    ex('Tim is <b>old enough to</b> ride the roller coaster.', '→ enough 在形容詞後面') +
    ex('We don\'t have <b>enough time to</b> finish.', '→ enough 在名詞前面') +
    ex('He is too young to drive. = He is not old enough to drive.', '→ 互換'), sub='放前面還是後面？'),
  card('need + V-ing = need to be p.p.', row('主詞是「東西」，意思是被動', '') +
    ex('My bike <i>needs fixing</i>.', '→ 腳踏車需要修理', 'o') +
    ex('= My bike <i>needs to be fixed</i>.', '→ 被動的寫法', 'o') +
    ex('I <i>need to fix</i> my bike.', '→ 主詞是人：need to V', 'o'), 'o', sub='主動的樣子、被動的意思'), tight=True)),

section('不定詞 vs 動名詞', table(['用法', 'to V', 'V-ing'], [
  ['當主詞', 'To travel is fun.（常改 It is fun to travel.）', 'Traveling is fun.'],
  ['當動詞受詞', 'want、hope、decide、plan、agree', 'enjoy、finish、mind、keep、avoid'],
  ['介系詞後面', '✗', '✓ good at singing'],
  ['當形容詞', '✓ something to drink', '✗'],
  ['表示目的', '✓ I went there to study.', '✗'],
  ['兩種都可以、意思一樣', 'like、love、hate、begin、start、continue', ''],
  ['兩種都可以、意思不同', 'stop、remember、forget、try：to V＝要去做', 'V-ing＝已經做'],
]) + note('判斷順序：① 前面是介系詞嗎？→ V-ing　② 前面的動詞是哪一組？　③ 是不是「為了…」或「…的東西」？→ to V')),

section('學生最常錯的 5 句', top5([
  ('I want to buying a new phone.', 'I want to buy a new phone.', 'to 後面一定是原形。'),
  ('She decided going to Japan.', 'She decided to go to Japan.', 'decide 後面接 to V。'),
  ('Mom asked me buy some milk.', 'Mom asked me to buy some milk.', 'ask + 人 + to V。'),
  ('The teacher told us to not talk.', 'The teacher told us not to talk.', 'not 放在 to 前面。'),
  ('She is enough old to go alone.', 'She is old enough to go alone.', 'enough 放在形容詞後面。'),
])),

section('快問快答 8 題', qas([
  ('We hope ____ you soon. (to see / seeing)', 'to see'),
  ('He enjoys ____ soccer. (to play / playing)', 'playing'),
  ('I need a pen ____ with. (write / to write)', 'to write'),
  ('I don\'t know ____ to go. (where / why)', 'where'),
  ('It\'s too late ____ the bus. (to catch / catching)', 'to catch'),
  ('She isn\'t ____ to vote. (old enough / enough old)', 'old enough'),
  ('The room needs ____. (to clean / cleaning)', 'cleaning'),
  ('Dad told me ____ worry. (not to / to not)', 'not to'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('To swim in this lake is dangerous.', 'It is dangerous to swim in this lake.'),
  ('I don\'t know what I should do.', 'I don\'t know what to do.'),
  ('He is so tired that he can\'t walk.', 'He is too tired to walk.'),
  ('She is too short to reach the shelf.', 'She is not tall enough to reach the shelf.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和比較表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '第一期 Week 9 的週測驗可以當 to V 和 V-ing 的綜合練習']), 'o'))),
]

UNIT = {'no': 4, 'zh': '不定詞', 'en': 'Infinitives', 'c1': 'to V', 'c2': '用途最廣', 'slides': S}
