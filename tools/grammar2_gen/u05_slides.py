from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '感官動詞後面接原形、V-ing、p.p. 的不同',
    '分清楚 -ed（感到）和 -ing（令人）',
    'make、have、let 接原形；get 接 to V',
    '用 have / get + 物 + p.p. 說「請人處理」',
    '連綴動詞後面接形容詞，或 like + 名詞'])),
  card('暖身 3 題', qas([
    ('The soup tastes ____. (good / well)', 'good'),
    ('Mom made me ____ my room. (clean / to clean)', 'clean'),
    ('I\'m ____ in music. (interested / interesting)', 'interested')]), 'o'))),

section('感官動詞：原形、V-ing、p.p.', lead('see、watch、notice、hear、listen to、feel + 受詞 + …') + table(
  ['後面接', '意思', '例句'], [
  ['原形', '看到整個動作', ('I saw Ken <b>cross</b> the street.', '我看到 Ken 過了馬路')],
  ['V-ing', '看到動作正在進行', ('I saw Ken <b>crossing</b> the street.', '我看到 Ken 正在過馬路')],
  ['p.p.', '受詞「被」怎麼了', ('I saw my bike <b>stolen</b>.', '我看到我的腳踏車被偷了')],
  ['V-ing', '聽到正在發生', ('We heard someone <b>knocking</b> on the door.', '我們聽到有人在敲門')],
], audio_col=2) + note('主動句不能接 to V：I saw him to cross ✗。改成被動才補 to：He was seen to cross the street.')),

section('情緒動詞：-ed 和 -ing', cards(2,
  card('-ed：人「感到」…', table(['形容詞', '意思'], [
    ['interested', '感到有興趣'], ['excited', '感到興奮'], ['bored', '感到無聊'], ['surprised', '感到驚訝'], ['tired', '感到疲倦']]) +
    ex('We were <b>bored</b>.', '→ 我們覺得無聊'), sub='感覺到的人'),
  card('-ing：「令人」感到…', table(['形容詞', '意思'], [
    ['interesting', '有趣的'], ['exciting', '令人興奮的'], ['boring', '無聊的'], ['surprising', '令人驚訝的'], ['tiring', '令人疲倦的']]) +
    ex('The movie was <i>boring</i>.', '→ 電影很無聊', 'o'), 'o', sub='帶來感覺的東西'), tight=True)),

section('-ed 還是 -ing？怎麼判斷', cards(2,
  card('問自己：在說誰的感覺？', row('感覺到的人 → -ed', '') + row('帶來感覺的東西、人 → -ing', '') +
    ex('I\'m <b>interested</b> in science.', '→ 我感到有興趣') +
    ex('Science is <b>interesting</b> to me.', '→ 科學令我感興趣') +
    ex('He is a <b>boring</b> speaker.', '→ 他說話讓人覺得無聊'), sub='判斷方法'),
  card('-ed 常搭配的介系詞', table(['片語', '意思'], [
    ['be interested in', '對…有興趣'], ['be surprised at', '對…驚訝'], ['be excited about', '對…興奮'],
    ['be bored with', '對…厭煩'], ['be pleased with', '對…滿意']]), 'o', sub='要整組背'), tight=True)),

section('使役動詞：叫別人去做', table(['句型', '意思', '例句'], [
  ['make + 人 + 原形', '強迫、使得', ('The sad movie <b>made</b> me <b>cry</b>.', '那部電影讓我哭了')],
  ['have + 人 + 原形', '叫、交代', ('I\'ll <b>have</b> him <b>call</b> you back.', '我會請他回你電話')],
  ['let + 人 + 原形', '允許、讓', ('Mom <b>let</b> me <b>stay</b> up late.', '媽媽讓我晚睡')],
  ['get + 人 + to V', '說服、叫', ('I <b>got</b> my brother <b>to help</b> me.', '我說服弟弟幫我')],
  ['help + 人 + (to) V', '幫忙', ('She <b>helped</b> me <b>carry</b> the box.', '她幫我搬箱子')],
], audio_col=2) + note('口訣：make、have、let 接原形；get 很特別，接 to V；help 兩種都可以。')),

section('請人處理與使役動詞的被動', cards(2,
  card('have / get + 物 + p.p.', row('東西是「被」處理的', '') +
    ex('I <b>had my hair cut</b> yesterday.', '→ 理髮師剪的，不是自己剪') +
    ex('We need to <b>get the car fixed</b>.', '→ 把車拿去修'), sub='請別人把東西弄好'),
  card('使役動詞的被動', ex('The teacher made us run.', '→ 主動', 'o') +
    ex('We <i>were made to run</i>.', '→ make 的被動要補 to', 'o') +
    ex('Dad let me go. → I <i>was allowed to go</i>.', '→ let 改用 be allowed to', 'o'), 'o', sub='補 to'))),

section('連綴動詞：look、sound、smell、taste、feel', table(['動詞', '+ 形容詞', '+ like + 名詞'], [
  ['look 看起來', ('You look <b>tired</b>.', '你看起來很累'), 'He looks like his dad.'],
  ['sound 聽起來', ('That sounds <b>great</b>!', '聽起來很棒'), 'It sounds like a good plan.'],
  ['smell 聞起來', ('The bread smells <b>good</b>.', '麵包聞起來很香'), 'This soap smells like lemon.'],
  ['taste 嚐起來', ('The soup tastes <b>salty</b>.', '湯嚐起來很鹹'), 'It tastes like chicken.'],
  ['feel 感覺', ('I feel <b>sick</b>.', '我覺得不舒服'), 'The fabric feels like silk.'],
], audio_col=1) + note('後面是形容詞直接接；後面是名詞要加 like。')),

section('變得、保持：也接形容詞', cards(2,
  card('become / get / turn / grow', ex('It\'s <b>getting dark</b>.', '→ 天色變暗了') +
    ex('The leaves <b>turn red</b> in fall.', '→ 葉子變紅') +
    ex('She <b>became famous</b> after the show.', '→ 她出名了'), sub='變得…'),
  card('keep / stay / remain', ex('Please <i>keep quiet</i> in the library.', '→ 保持安靜', 'o') +
    ex('<i>Stay calm</i> during an earthquake.', '→ 保持冷靜', 'o') +
    row('注意：', 'look、smell 是「主動去做」時，是一般動詞，用副詞：She looked carefully at the map.'), 'o', sub='保持…'))),

section('學生最常錯的 5 句', top5([
  ('I saw him to enter the room.', 'I saw him enter the room.', '主動的感官動詞不接 to V。'),
  ('The game was so excited.', 'The game was so exciting.', '比賽「令人」興奮用 -ing。'),
  ('My mom made me to clean my room.', 'My mom made me clean my room.', 'make + 人 + 原形。'),
  ('I got my sister help me.', 'I got my sister to help me.', 'get + 人 + to V。'),
  ('The soup tastes well.', 'The soup tastes good.', '連綴動詞接形容詞。'),
])),

section('快問快答 8 題', qas([
  ('I heard her ____ in the shower. (sing / to sing)', 'sing'),
  ('The trip was ____. (tiring / tired)', 'tiring'),
  ('We were ____ at the news. (surprised / surprising)', 'surprised'),
  ('Dad let me ____ his car. (drive / to drive)', 'drive'),
  ('I got him ____ the door. (open / to open)', 'to open'),
  ('I had my phone ____. (fix / fixed)', 'fixed'),
  ('She looks ____ a model. (like / as)', 'like'),
  ('It\'s getting ____. (hot / hotly)', 'hot'),
])),

section('改寫練習與下一步', two(div(lead('同義改寫'), qas([
  ('The movie bored me.', 'I was bored with the movie. / The movie was boring.'),
  ('The coach made us practice.（改被動）', 'We were made to practice.'),
  ('Mom let me go out.（改被動）', 'I was allowed to go out.'),
  ('A mechanic fixed my bike.', 'I had my bike fixed.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和整理表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '感官、使役動詞的被動可以回 Unit 2 複習']), 'o'))),
]

UNIT = {'no': 5, 'zh': '特殊動詞句型', 'en': 'Special Verb Patterns', 'c1': '感官・使役', 'c2': '情緒・連綴', 'slides': S}
