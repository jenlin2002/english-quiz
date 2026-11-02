from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section

S = [
section('本單元目標與暖身', cards(2,
  card('學完這個單元，你會', ul([
    '分辨「動詞 + 副詞」和「動詞 + 介系詞」',
    '代名詞 it / them 放對位置：turn it on、look for it',
    '記住常考的片語動詞和意思',
    '分清楚 put off / call off、hand in / hand out、put on / wear'])),
  card('暖身 3 題', qas([
    ('It\'s dark. Turn ____ the light. (on / off)', 'on'),
    ('I\'m looking ____ my phone. (at / for)', 'for'),
    ('Here\'s your coat. Put ____. (on it / it on)', 'it on')]), 'o'))),

section('兩種片語動詞：受詞放哪裡？', table(['', '動詞 + 副詞（可分開）', '動詞 + 介系詞（不可分開）'], [
  ['例子', 'turn on、pick up、give up', 'look at、listen to、wait for'],
  ['名詞受詞', 'turn on the light ✓ / turn the light on ✓', 'look at the bird ✓'],
  ['代名詞受詞', 'turn it on ✓ / turn on it ✗', 'look at it ✓ / look it at ✗'],
]) + '<div style="height:calc(var(--u)*1.4)"></div>' + cards(2,
  card('副詞型：代名詞夾中間', ex('Turn the light on. → Turn <b>it</b> on.', '→ it 放中間')),
  card('介系詞型：受詞永遠在後面', ex('Look at the bird. → Look at <i>it</i>.', '→ it 放後面', 'o'), 'o'), tight=True)),

section('動詞 + 副詞：開關、穿脫', table(['片語', '意思', '例句'], [
  ['turn on / off', '打開／關掉', ('It\'s dark. <b>Turn it on</b>.', '太暗了，把它打開')],
  ['turn up / down', '開大聲／關小聲', ('The music is too loud. <b>Turn it down</b>.', '音樂太大聲，關小聲一點')],
  ['put on / take off', '穿上／脫掉', ('It\'s cold. <b>Put your coat on</b>.', '很冷，把外套穿上')],
  ['try on', '試穿', ('Can I <b>try these shoes on</b>?', '我可以試穿這雙鞋嗎？')],
  ['wake up', '叫醒', ('Please <b>wake me up</b> at six.', '請六點叫我起床')],
], audio_col=2)),

section('動詞 + 副詞：放、給、找、交', table(['片語', '意思', '例句'], [
  ['pick up', '撿起；接人', ('Dad will <b>pick me up</b> at five.', '爸爸五點來接我')],
  ['put away', '收好', ('<b>Put your toys away</b>.', '把玩具收好')],
  ['give up / give back', '放棄／歸還', ('Don\'t <b>give it up</b>.', '不要放棄')],
  ['look up / find out', '查／查出', ('<b>Look the word up</b> in a dictionary.', '在字典裡查這個字')],
  ['hand in / hand out', '繳交／分發', ('Please <b>hand in</b> your homework.', '請交作業')],
  ['put off / call off', '延後／取消', ('They <b>called the game off</b>.', '他們取消了比賽')],
], audio_col=2) + note('沒有受詞的：get up、grow up、come back、go out、sit down、hurry up')),

section('動詞 + 介系詞：不可分開', table(['片語', '意思', '例句'], [
  ['look at / look for', '看／找', ('I\'m <b>looking for</b> my keys.', '我在找鑰匙')],
  ['look after / take care of', '照顧', ('Can you <b>look after</b> my cat?', '你可以照顧我的貓嗎？')],
  ['listen to', '聽', ('I like <b>listening to</b> music.', '我喜歡聽音樂')],
  ['wait for', '等', ('We\'re <b>waiting for</b> the bus.', '我們在等公車')],
  ['belong to', '屬於', ('This bag <b>belongs to</b> Lisa.', '這個包包是 Lisa 的')],
  ['get on / get off', '上車／下車', ('<b>Get off</b> at the next stop.', '下一站下車')],
], audio_col=2)),

section('三個字的片語動詞', cards(2,
  card('不可分開', table(['片語', '意思'], [
    ['run out of', '用完'], ['look forward to', '期待（接 V-ing）'], ['get along with', '和…相處'],
    ['catch up with', '趕上'], ['come up with', '想出（點子）']]), sub='受詞放最後面'),
  card('例句', ex('We\'ve <b>run out of</b> milk.', '→ 牛奶用完了') +
    ex('Do you <i>get along with</i> your classmates?', '→ 和同學處得好嗎？', 'o') +
    ex('She <b>came up with</b> a great idea.', '→ 想出好點子'), 'o', sub='examples'), tight=True)),

section('容易混淆的幾組', two(
  card('put off 和 call off', ex('<b>Put off</b> the meeting.', '→ 延後，之後還會開') +
    ex('<i>Call off</i> the meeting.', '→ 取消，不開了', 'o')),
  card('hand in 和 hand out', ex('<b>Hand in</b> your work.', '→ 交上去') +
    ex('<i>Hand out</i> the papers.', '→ 發下去', 'o'), 'o'), tight=True) + two(
  card('put on 和 wear', ex('<b>Put on</b> your coat.', '→ 穿上的動作') +
    ex('She <i>is wearing</i> a red coat.', '→ 穿著的狀態', 'o')),
  card('look at / for / after / up', ex('Look <b>at</b> me. / Look <b>for</b> it.', '→ 看／找') +
    ex('Look <i>after</i> the baby. / Look it <i>up</i>.', '→ 照顧／查', 'o'), 'o'), tight=True)),

section('學生最常錯的 5 句', top5([
  ('Please turn off it.', 'Please turn it off.', '副詞型，代名詞夾中間。'),
  ('I\'m looking it for.', 'I\'m looking for it.', '介系詞型，受詞放後面。'),
  ('I\'m listening music.', 'I\'m listening to music.', 'listen 要加 to。'),
  ('We are waiting the bus.', 'We are waiting for the bus.', 'wait for + 受詞。'),
  ('She is putting on a red dress in the photo.', 'She is wearing a red dress.', '穿著的狀態用 wear。'),
])),

section('快問快答 8 題', qas([
  ('Please take ____ your shoes. (off / on)', 'off'),
  ('Don\'t give ____! (up / off)', 'up'),
  ('Here\'s your hat. Put ____. (on it / it on)', 'it on'),
  ('I\'m looking ____ my cat. (for it / it for)', 'for'),
  ('The music is loud. Turn it ____. (up / down)', 'down'),
  ('We\'ve run out ____ eggs. (of / off)', 'of'),
  ('Please hand ____ your test now. (in / out)', 'in'),
  ('The trip was ____ because of the typhoon. It\'s canceled. (put off / called off)', 'called off'),
])),

section('改寫練習與下一步', two(div(lead('把名詞換成代名詞'), qas([
  ('Turn on the fan.', 'Turn it on.'),
  ('He gave up his plan.', 'He gave it up.'),
  ('I\'m looking for my shoes.', 'I\'m looking for them.'),
  ('Pick up the toys.', 'Pick them up.'),
])), card('學完了！接下來', ul([
  '回到「📘 講解」頁看完整的片語表',
  '做講解頁最後的自我練習（不計點數）',
  '準備好了就按右上角「📝 前往測驗」',
  '片語動詞要多用才記得住：每天挑三個造句']), 'o'))),
]

UNIT = {'no': 7, 'zh': '重要的片語動詞', 'en': 'Phrasal Verbs', 'c1': '動詞+副詞', 'c2': '動詞+介系詞', 'slides': S}
