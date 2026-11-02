from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '知道什麼時候要用被動語態',
    '用四個步驟把主動句改成被動句',
    '寫出各種時態的被動（being、been、助動詞 + be）',
    '處理疑問句、授與動詞、使役／感官動詞的被動',
    '背熟不用 by 的被動片語'])),
  card('暖身 3 題', qas([
    ('This cake ____ by my mom. (made / was made)', 'was made'),
    ('English ____ in many countries. (speaks / is spoken)', 'is spoken'),
    ('I am interested ____ science. (in / by)', 'in')]), 'o'))),

section('什麼時候用被動？', lead('公式：be 動詞 + 過去分詞（p.p.）（+ by 做動作的人）') + cards(3,
  card('① 不知道是誰做的', ex('My bike <b>was stolen</b> last night.', '→ 不知道小偷是誰'), sub='unknown'),
  card('② 誰做的不重要', ex('English <i>is spoken</i> in many countries.', '→ 說英語的人不用講', 'o'), 'o', sub='not important'),
  card('③ 想強調「東西」', ex('This temple <b>was built</b> 200 years ago.', '→ 重點是這座廟'), sub='focus on the thing'), tight=True) +
  note('只有後面有受詞的「及物動詞」才有被動。happen、arrive、die、sleep 沒有被動：The accident happened at noon.（不說 was happened）')),

section('主動改被動：四個步驟', two(
  card('步驟', ul([
    '① 受詞搬到最前面當主詞',
    '② 時態看「原來的句子」',
    '③ 單複數看「新的主詞」',
    '④ 動詞改 p.p.，原主詞放到 by 後面（代名詞改受格）']), sub='口訣：時態看舊句，單複數看新主詞'),
  card('跟著做一次',
    ex('Kevin <b>cleans</b> the classroom.', '→ 主動：現在式') +
    ex('The classroom <b>is cleaned</b> by Kevin.', '→ 被動：classroom 單數 → is') +
    ex('They <i>planted</i> these trees.', '→ 主動：過去式', 'o') +
    ex('These trees <i>were planted</i> by them.', '→ 複數 → were；they → them', 'o'), 'o'))),

section('各時態的被動', table(['時態', '被動公式', '例句'], [
  ['現在簡單式', 'am / is / are + p.p.', ('The store <b>is opened</b> at nine every day.', '這家店每天九點開門')],
  ['過去簡單式', 'was / were + p.p.', ('The windows <b>were broken</b> by the storm.', '窗戶被暴風雨打破了')],
  ['未來式', 'will be + p.p.', ('The results <b>will be announced</b> tomorrow.', '結果明天公布')],
  ['現在進行式', 'am / is / are being + p.p.', ('The road <b>is being repaired</b> now.', '這條路正在整修')],
  ['過去進行式', 'was / were being + p.p.', ('The dog <b>was being washed</b> when I came in.', '我進來時狗正在被洗澡')],
  ['現在完成式', 'have / has been + p.p.', ('The tickets <b>have been sold</b> out.', '票已經賣完了')],
  ['過去完成式', 'had been + p.p.', ('The cake <b>had been eaten</b> before we arrived.', '我們到之前蛋糕已經被吃光')],
  ['助動詞', 'can / must / should + be + p.p.', ('Phones <b>must be turned</b> off in class.', '上課手機一定要關機')],
], audio_col=2)),

section('看出規律：being、been、be', cards(3,
  card('進行式 → being', row('be + being + p.p.', '') +
    ex('The bridge <b>is being built</b>.', '→ 橋正在被蓋') +
    ex('The room <b>was being cleaned</b>.', '→ 房間當時正在被打掃'), sub='正在被…'),
  card('完成式 → been', row('have / has / had + been + p.p.', '') +
    ex('My wallet <i>has been found</i>.', '→ 錢包已經被找到了', 'o') +
    ex('The work <i>had been done</i> by noon.', '→ 中午前已經做完', 'o'), 'o', sub='已經被…'),
  card('助動詞 → be', row('can / will / must / should + be + p.p.', '') +
    ex('This problem <b>can be solved</b>.', '→ 這問題可以被解決') +
    ex('Homework <b>should be handed</b> in on time.', '→ 作業應該準時交'), sub='可以／應該被…'), tight=True) +
  note('檢查方法：被動一定有「be 的某個樣子」+ p.p.。只有 p.p. 沒有 be，或 be 後面接 V-ing，都不是被動。')),

section('疑問句與祈使句的被動', cards(2,
  card('疑問句：先改肯定句，再把 be 搬前面', row('Yes / No 問句', '') +
    ex('Did Ann make this card?', '→ 主動問句') +
    ex('<b>Was</b> this card <b>made</b> by Ann?', '→ 被動問句') +
    row('疑問詞 Who', '') +
    ex('Who invented the telephone?', '→ 主動') +
    ex('<b>By whom was</b> the telephone <b>invented</b>?', '→ who 變成 by whom'), sub='Questions'),
  card('祈使句：Let + 受詞 + be + p.p.', row('比較正式，考試偶爾出現', '') +
    ex('Close the door.', '→ 主動', 'o') +
    ex('<i>Let</i> the door <i>be closed</i>.', '→ 被動', 'o'), 'o', sub='Commands'), tight=True)),

section('授與動詞：兩種被動都可以', lead('give、send、show、teach、tell 後面有「人」和「東西」兩個受詞，哪一個都能當新主詞。') + two(
  card('「人」當主詞',
    ex('Grandma gave me a watch.', '→ 主動') +
    ex('<b>I was given</b> a watch by Grandma.', '→ 我被給了一支手錶') +
    ex('<b>Tom was shown</b> the way by a police officer.', '→ Tom 被指引了方向'), sub='人 + be + p.p. + 東西'),
  card('「東西」當主詞：人前面補介系詞',
    ex('<i>A watch was given to</i> me by Grandma.', '→ give、send、show、teach 用 to', 'o') +
    ex('<i>A cake was made for</i> me by Mom.', '→ make、buy、cook 用 for', 'o'), 'o', sub='東西 + be + p.p. + to / for + 人'))),

section('使役動詞、感官動詞的被動：要補 to', cards(2,
  card('主動接原形 → 被動補 to', row('make、see、hear', '') +
    ex('The teacher <b>made</b> us <b>clean</b> the room.', '→ 主動：make + 人 + 原形') +
    ex('We <b>were made to clean</b> the room.', '→ 被動：be made + to + 原形') +
    ex('I <b>heard</b> him <b>sing</b>. → He <b>was heard to sing</b>.', '→ 感官動詞也一樣'), sub='最容易漏掉的 to'),
  card('主動接 V-ing → 被動照用 V-ing', ex('I <i>saw</i> him <i>crossing</i> the street.', '→ 主動', 'o') +
    ex('He <i>was seen crossing</i> the street.', '→ 被動：照用 crossing', 'o'), 'o', sub='V-ing 不用改'))),

section('by 可以省略，與不用 by 的被動片語', cards(2,
  card('by 什麼時候省略', row('做動作的是 people、someone、they 這種泛指的人，或不知道是誰', '') +
    ex('Rice <b>is grown</b> in Taiwan.', '→ 不說 by people') +
    ex('My umbrella <b>has been taken</b>.', '→ 不知道誰拿走'), sub='by + 泛指的人'),
  card('固定片語（要整組背）', table(['片語', '意思'], [
    ['be interested in', '對…有興趣'], ['be surprised at', '對…感到驚訝'], ['be pleased / satisfied with', '對…滿意'],
    ['be covered with', '被…覆蓋'], ['be filled with', '充滿…']]), 'o', sub='不用 by'))),

section('made 與 known 的不同介系詞', table(['片語', '意思', '例句'], [
  ['be made of', '由…製成（看得出原料）', ('This table <b>is made of</b> wood.', '這張桌子是木頭做的')],
  ['be made from', '由…製成（看不出原料）', ('Paper <b>is made from</b> trees.', '紙是用樹做的')],
  ['be made in', '在…（地方）製造', ('This phone <b>was made in</b> Taiwan.', '這支手機是台灣製造的')],
  ['be known to', '為…（人）所知', ('The singer <b>is known to</b> everyone.', '大家都認識這位歌手')],
  ['be known for', '因…而有名', ('Tainan <b>is known for</b> its snacks.', '台南以小吃聞名')],
  ['be known as', '以…（身分、名字）為人所知', ('Hualien <b>is known as</b> a great place to hike.', '花蓮是有名的登山好地方')],
], audio_col=2)),

section('對比頁：容易搞混的四組', two(
  card('interested 與 interesting', ex('I <b>am interested</b> in music.', '→ 人「感到」有興趣：-ed') +
    ex('The book <i>is interesting</i>.', '→ 東西「令人」覺得有趣：-ing', 'o')),
  card('happened 與 was happened', ex('The accident <b>happened</b> last night.', '→ happen 沒有被動') +
    ex('The car <i>was hit</i> by a bus.', '→ hit 是及物動詞，可以被動', 'o'), 'o'), tight=True) + two(
  card('is building 與 is being built', ex('The workers <b>are building</b> a bridge.', '→ 工人在蓋：主動') +
    ex('A bridge <i>is being built</i>.', '→ 橋被蓋：被動', 'o')),
  card('made us clean 與 were made to clean', ex('Mom <b>made</b> us <b>clean</b> up.', '→ 主動：原形') +
    ex('We <i>were made to clean</i> up.', '→ 被動：補 to', 'o'), 'o'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('The car washed by my dad.', 'The car was washed by my dad.', '被動一定要有 be 動詞。'),
  ('These cookies was made by Amy.', 'These cookies were made by Amy.', '單複數看新主詞 these cookies。'),
  ('The letter is sent by she.', 'The letter is sent by her.', 'by 後面用受格。'),
  ('The bridge is building now.', 'The bridge is being built now.', '進行式被動是 is being + p.p.。'),
  ('We were made clean the room.', 'We were made to clean the room.', '使役動詞改被動要補 to。'),
])),

section('快問快答 8 題', qas([
  ('The window ____ by Tom yesterday. (broke / was broken)', 'was broken'),
  ('These songs ____ by kids every year. (are sung / is sung)', 'are sung'),
  ('A new school ____ next year. (will build / will be built)', 'will be built'),
  ('The road ____ now. (is repairing / is being repaired)', 'is being repaired'),
  ('The tickets have ____ sold out. (be / been)', 'been'),
  ('The accident ____ at noon. (happened / was happened)', 'happened'),
  ('This shirt is made ____ cotton. (of / from)', 'of'),
  ('She was made ____ the dishes. (wash / to wash)', 'to wash'),
])),

section('改寫練習與下一步', two(div(lead('主動改被動'), qas([
  ('Mr. Lin teaches math.', 'Math is taught by Mr. Lin.'),
  ('Did your sister draw this picture?', 'Was this picture drawn by your sister?'),
  ('Dad gave me a new bike.', 'I was given a new bike by Dad. / A new bike was given to me by Dad.'),
  ('Somebody has taken my pen.', 'My pen has been taken.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和片語表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」：選擇 → 填空 → 找錯 → 改寫，錯題要訂正到全對',
  '第一期 Week 12 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 2, 'zh': '被動語態', 'en': 'The Passive Voice', 'c1': '主動', 'c2': '被動', 'slides': S}
