from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '分辨國中會用到的 7 種時態',
    '看到時間線索（every day、now、yesterday、since…）就知道用哪個時態',
    '正確寫出 -s、-ed、-ing 和過去分詞',
    '分清楚 will / be going to、when / while、for / since',
    '知道什麼時候「不能」用進行式和現在完成式'])),
  card('暖身 3 題', qas([
    ('Look! The dog ____ the ball. (chases / is chasing)', 'is chasing'),
    ('We ____ to Kenting last summer. (go / went)', 'went'),
    ('I ____ this movie twice. (saw / have seen)', 'have seen')]), 'o'))),

section('先看全貌：時間 × 樣子', lead('時態＝「什麼時候」加上「什麼樣子」。國中先學這 7 種。') + table(
  ['時態', '公式', '例句'], [
  ['現在簡單式', '原形 / V-s', ('She <b>plays</b> tennis every Sunday.', '她每週日打網球')],
  ['過去簡單式', '過去式 V-ed', ('She <b>played</b> tennis yesterday.', '她昨天打網球')],
  ['未來式', 'will + 原形', ('She <b>will play</b> tennis tomorrow.', '她明天會打網球')],
  ['現在進行式', 'am / is / are + V-ing', ('She <b>is playing</b> tennis now.', '她現在正在打網球')],
  ['過去進行式', 'was / were + V-ing', ('She <b>was playing</b> tennis at 5 yesterday.', '她昨天五點正在打網球')],
  ['現在完成式', 'have / has + p.p.', ('She <b>has played</b> tennis for six years.', '她打網球打了六年')],
  ['過去完成式', 'had + p.p.', ('She <b>had played</b> tennis before she went home.', '她回家前已經打過網球')],
], audio_col=2)),

section('現在簡單式：習慣、事實、真理', cards(2,
  card('什麼時候用', row('① 習慣：', 'usually、often、every day') + row('② 現在的狀態、事實', '') + row('③ 不變的真理', '') +
    ex('Ken <b>rides</b> his bike to school every morning.', '→ 每天的習慣') +
    ex('My aunt <b>lives</b> in Kaohsiung.', '→ 現在的狀態') +
    ex('The earth <b>goes</b> around the sun.', '→ 科學事實'), sub='Simple Present'),
  card('第三人稱單數要加 -s', row('一般：', 'read → reads') + row('s, x, sh, ch, o：', '加 -es：watches、goes') +
    row('子音 + y：', 'study → studies（play → plays）') + row('特殊：', 'have → has') +
    ex('She <i>doesn\'t</i> eat meat.', '→ 有 does，動詞變回原形', 'o') +
    ex('<i>Does</i> he <i>like</i> dogs?', '→ 不是 Does he likes', 'o'), 'o', sub='he / she / it / 單數名詞'))),

section('現在簡單式也可以講未來', cards(2,
  card('① 照時刻表的行程', row('火車、公車、節目、課表', '') +
    ex('The last bus <b>leaves</b> at 10:30 tonight.', '→ 末班公車今晚 10:30 開') +
    ex('The concert <b>starts</b> at seven.', '→ 演唱會七點開始'), sub='timetable'),
  card('② 時間、條件子句', row('when、before、after、until、as soon as、if、unless', '') +
    ex('I will call you <i>when</i> I <i>get</i> home.', '→ 不是 when I will get home', 'o') +
    ex('<i>If</i> it <i>rains</i> tomorrow, we will stay inside.', '→ 主要子句才用 will', 'o'), 'o', sub='考試最愛考')) +
  note('口訣：when / if 子句「現在代未來」，另一半才放 will。')),

section('過去簡單式：已經結束的事', cards(2,
  card('什麼時候用', row('時間線索：', 'yesterday、last week、two days ago、in 2020、when I was young') +
    ex('We <b>visited</b> the science museum last Saturday.', '→ 上週六，已經結束') +
    ex('When Dad was a boy, he <b>walked</b> to school.', '→ 小時候的事') +
    ex('I <i>didn\'t see</i> the movie. <i>Did</i> you <i>see</i> it?', '→ 有 did，動詞用原形', 'o'), sub='Simple Past'),
  card('-ed 的四條規則', row('一般：', 'clean → cleaned') + row('e 結尾：', 'like → liked（只加 d）') +
    row('子音 + y：', 'cry → cried（play → played）') + row('短母音 + 單一子音：', 'stop → stopped、plan → planned'), 'o', sub='規則動詞'))),

section('-ed 怎麼念？常考的不規則動詞', two(
  card('-ed 的三種念法', row('/ɪd/：', '字尾是 t、d 音 → wanted、needed') + row('/t/：', '字尾是 p、k、s、sh、ch、f 音 → helped、cooked、washed') +
    row('/d/：', '其他有聲音 → played、called、lived') +
    ex('She <b>wanted</b> to help, so she <b>cooked</b> and <b>cleaned</b>.', '→ /ɪd/、/t/、/d/ 都出現了')),
  card('不規則動詞（一定要背）', table(['原形', '過去式', '過去分詞'], [
    ['go', 'went', 'gone'], ['see', 'saw', 'seen'], ['eat', 'ate', 'eaten'], ['write', 'wrote', 'written'],
    ['buy', 'bought', 'bought'], ['teach', 'taught', 'taught'], ['leave', 'left', 'left'], ['put', 'put', 'put']]), 'o'), tight=True)),

section('未來式：will 和 be going to', cards(2,
  card('will + 原形', row('① 說話當下才決定', '') + row('② 個人的猜測、承諾', '') +
    ex('The phone is ringing. I\'<b>ll get</b> it.', '→ 聽到電話響，當下決定') +
    ex('I think it <b>will be</b> sunny tomorrow.', '→ 我覺得、我猜'), sub='當下決定'),
  card('be going to + 原形', row('① 事先就計畫好', '') + row('② 眼前有明顯跡象', '') +
    ex('I\'<i>m going to visit</i> Grandma this weekend.', '→ 早就計畫好', 'o') +
    ex('Look at those clouds. It\'<i>s going to rain</i>.', '→ 看到烏雲', 'o'), 'o', sub='早有計畫')) +
  note('已經安排好的行程，也可以用現在進行式：My cousin is arriving tomorrow.（come、go、leave、arrive 最常見）')),

section('現在進行式：此刻正在做', cards(2,
  card('什麼時候用', row('時間線索：', 'now、right now、at the moment、Look!、Listen!') +
    ex('Listen! Someone <b>is knocking</b> on the door.', '→ 此刻正在敲門') +
    ex('Jenny <b>is learning</b> to swim this summer.', '→ 這段期間正在學'), sub='Present Progressive'),
  card('V-ing 怎麼加', row('一般：', 'read → reading') + row('不發音的 e：', 'make → making（see → seeing）') +
    row('ie 結尾：', 'die → dying、lie → lying') + row('短母音 + 單一子音：', 'run → running、sit → sitting') +
    ex('The kids <i>are swimming</i> and <i>writing</i> postcards.', '→ 重複 m；去 e', 'o'), 'o', sub='拼字規則'))),

section('這些動詞通常不用進行式', lead('描述「狀態」（心裡的感覺、知道、擁有）而不是動作，就算有 now 也用簡單式。') + table(
  ['類別', '動詞', '例句'], [
  ['喜好、情緒', 'like、love、hate、want、need', ('I <b>want</b> some water now.', '不說 I am wanting')],
  ['想法、知道', 'know、understand、believe、remember', ('I <b>know</b> the answer.', '不說 I am knowing')],
  ['擁有', 'have（擁有）、own、belong to', ('This bag <b>belongs</b> to Amy.', '這個包包是 Amy 的')],
  ['感官', 'see、hear、smell、taste', ('This soup <b>smells</b> great.', '這湯聞起來很棒')],
], audio_col=2) + note('例外：have 當「吃、度過」是動作，可以用進行式 → We are having lunch.')),

section('過去進行式：when 和 while', cards(2,
  card('過去某一刻正在做', row('公式：', 'was / were + V-ing') +
    ex('At nine last night, I <b>was doing</b> my homework.', '→ 昨晚九點那一刻') +
    ex('I <b>was taking</b> a shower <b>when</b> the phone <b>rang</b>.', '→ 長的動作用進行式，突然的用過去式'), sub='Past Progressive'),
  card('兩件事同時進行', row('while 後面常接「一段時間」', '') +
    ex('<i>While</i> Mom <i>was cooking</i>, the lights <i>went</i> out.', '→ 煮飯中突然停電', 'o') +
    ex('<i>While</i> Dad <i>was washing</i> the dishes, I <i>was cleaning</i> the table.', '→ 兩邊都是進行式', 'o'), 'o', sub='while = 在…的期間'))),

section('現在完成式：過去的事和現在有關', cards(3,
  card('① 經驗', row('ever、never、once、twice、before', '') +
    ex('Have you <b>ever tried</b> stinky tofu?', '→ 到現在有沒有吃過') +
    ex('I\'<b>ve never been</b> to Japan.', '→ 從來沒去過'), sub='做過幾次'),
  card('② 完成', row('just、already、yet', '') +
    ex('I\'<i>ve already finished</i> my report.', '→ already 放中間', 'o') +
    ex('Has the bus <i>come yet</i>?', '→ yet 放句尾', 'o'), 'o', sub='做完了沒'),
  card('③ 持續', row('for、since、How long', '') +
    ex('We\'<b>ve lived</b> here <b>for</b> ten years.', '→ 一直住到現在') +
    ex('She\'<b>s taught</b> here <b>since</b> 2018.', '→ 從 2018 年到現在'), sub='一直到現在'), tight=True)),

section('現在完成式的四個陷阱', cards(2,
  card('for 和 since', row('for + 一段時間：', 'for three days、for a long time') + row('since + 起點：', 'since Monday、since I was ten') +
    ex('I have known her <b>for</b> five years.', '→ 五年＝一段時間'), sub='多久 vs 從何時'),
  card('been to 和 gone to', ex('Amy <i>has been to</i> Japan.', '→ 去過，人已經回來', 'o') +
    ex('Amy <i>has gone to</i> Japan.', '→ 去了，人現在不在這裡', 'o'), 'o', sub='回來了沒'),
  card('不和「明確的過去時間」連用', row('yesterday、last year、ago、in 2019、When…? → 用過去式', '') +
    ex('I <b>lost</b> my key yesterday.', '→ 不說 have lost … yesterday'), sub='過去式 vs 完成式'),
  card('短暫動詞不能接 for / since', row('die、buy、leave、come → 改成狀態', '') +
    ex('His dog <i>has been dead</i> for two years.', '→ 不說 has died for', 'o'), 'o', sub='改用 be dead、have'), tight=True)),

section('過去完成式：過去的過去', lead('兩件過去的事，比較早發生的那一件用 had + p.p.。') + cards(2,
  card('看時間線排先後', row('較早的事：', 'had + p.p.') + row('較晚的事：', '過去簡單式') +
    ex('When we got to the theater, the movie <b>had</b> already <b>started</b>.', '→ 開演（先）→ 到達（後）') +
    ex('She told me she <b>had lost</b> her wallet.', '→ 掉錢包（先）→ 告訴我（後）'), sub='Past Perfect'),
  card('常見搭配', row('by the time + 過去式', '') + row('before / when + 過去式', '') + row('never…before', '') +
    ex('By the time the police arrived, the thief <i>had run</i> away.', '→ 警察到之前，小偷已經跑了', 'o') +
    ex('I <i>had never seen</i> snow before I went to Hokkaido.', '→ 去北海道以前沒看過雪', 'o'), 'o', sub='時間線索'))),

section('時間線索總整理', table(['時態', '常見的時間線索'], [
  ['現在簡單式', 'every day、usually、often、always、sometimes、never、on Sundays'],
  ['過去簡單式', 'yesterday、last…、…ago、in 2020、just now、then、When…?'],
  ['未來式', 'tomorrow、next…、soon、tonight、in + 一段時間（…之後）'],
  ['現在進行式', 'now、right now、at the moment、Look!、Listen!、these days'],
  ['過去進行式', 'at 8 last night、at that time、when + 過去式、while'],
  ['現在完成式', 'already、yet、just、ever、never、before、for、since、so far、recently'],
  ['過去完成式', 'by the time + 過去式、before / when + 過去式（較早的事）'],
]) + note('解題順序：① 找時間線索 → ② 決定時態 → ③ 看主詞決定單複數 → ④ 檢查動詞形式（-s、-ed、-ing、p.p.）')),

section('學生最常錯的 5 句', top5([
  ('She don\'t like carrots.', 'She doesn\'t like carrots.', '第三人稱單數用 does。'),
  ('I didn\'t went to school yesterday.', 'I didn\'t go to school yesterday.', 'did 後面用原形。'),
  ('I will tell him when he will come back.', 'I will tell him when he comes back.', 'when 子句用現在式代替未來式。'),
  ('I have seen him two days ago.', 'I saw him two days ago.', 'ago 是明確的過去時間，用過去式。'),
  ('We have lived here since three years.', 'We have lived here for three years.', '一段時間用 for，since 接起點。'),
])),

section('快問快答 8 題', qas([
  ('My sister usually ____ to bed at ten. (go / goes)', 'goes'),
  ('Listen! Someone ____ the piano. (plays / is playing)', 'is playing'),
  ('I ____ my keys yesterday. (lost / have lost)', 'lost'),
  ('We will go out if it ____ sunny. (is / will be)', 'is'),
  ('Ms. Lee has taught here ____ 2019. (for / since)', 'since'),
  ('I ____ the answer now. (know / am knowing)', 'know'),
  ('While I ____ TV, the lights went out. (watched / was watching)', 'was watching'),
  ('The train ____ when we got to the station. (left / had left)', 'had left'),
])),

section('挑錯練習與下一步', two(div(lead('挑錯：每句有一個錯'), qas([
  ('Does he likes ice cream?', 'likes → like'),
  ('Amy is wanting a new phone.', 'is wanting → wants'),
  ('He has gone to Japan twice.（他去過兩次）', 'has gone → has been'),
  ('My grandpa has died for ten years.', 'has died → has been dead'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整說明和更多例句',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」：選擇 → 填空 → 找錯 → 改寫，錯題要訂正到全對',
  '第一期 Week 1、2、3、11 的週測驗可以當綜合練習']), 'o'))),
]

UNIT = {'no': 1, 'zh': '時態', 'en': 'Tenses', 'c1': '什麼時候', 'c2': '什麼樣子', 'slides': S}
