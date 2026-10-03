from sl import *

W = 19
T = '句型整合與英檢題型診斷'

S = [
title(W, T, 'Putting It All Together for the GEPT', '看題型', '找線索'),

section('本週目標與暖身', cards(2,
  card('本週目標', ul([
    '認識英檢中級四項能力的題型：聽力、閱讀、寫作、口說',
    '學會「文法題四步驟」：看空格、數動詞、找時間、看連接',
    '把第 1–18 週的重點分成四大類，診斷自己最弱的一類',
    '練習閱讀與聽力的解題策略，以及口說的回答架構'])),
  card('暖身 3 題（各來自不同週）', qas([
    ('If I ____ you, I would study harder. (am / were)', 'were（第 8 週）'),
    ('The man ____ is talking is my uncle. (who / which)', 'who（第 11 週）'),
    ('Each of the students ____ a book. (has / have)', 'has（第 18 週）')]), 'o'))),

section('回收：第 18 週的主詞動詞一致', lead('英檢文法題最常考的陷阱，就是「主詞和動詞」離很遠。') + cards(2,
  card('第 18 週回顧',
    ex('<b>The number of</b> students <b>is</b> growing.', '→ the number of + 單數動詞') +
    ex('The teacher, <i>as well as</i> the students, <i>is</i> here.', '→ 插入語不影響動詞', 'o')),
  card('這週的延伸',
    ex('The books <b>that</b> my teacher gave me <b>are</b> interesting.', '→ 跳過關係子句，主詞是 books') +
    ex('<i>Walking</i> to school every day <i>is</i> good for you.', '→ 動名詞當主詞，用單數', 'o'), 'o'))),

section('英檢中級四項能力題型總覽', table(['能力', '題型', '這學期學過的重點'], [
  ['聽力', '看圖辨義、問答、簡短對話', '聽關鍵字：however、not until、neither'],
  ['閱讀', '詞彙題、段落填空、閱讀理解', '關代、分詞構句、轉折語、倒裝'],
  ['寫作', '中譯英、英文作文', '時態一致、被動、比較、平行結構'],
  ['口說', '朗讀短文、回答問題、看圖敘述', '完整句子、連接詞、加上理由和例子'],
]) + note('初試是聽力和閱讀，通過後才考複試的寫作和口說。這學期每週的測驗題型（看圖辨義、問答、閱讀理解、文意選填、克漏字、口說）都是照英檢的方向設計的。')),

section('文法題四步驟診斷法', cards(2,
  card('四步驟', row('1. 看空格：', '空格前後是什麼詞性？缺主詞、動詞還是修飾語？') + row('2. 數動詞：', '一個句子只有一個主要動詞；多一個動詞就要連接詞或關代') + row('3. 找時間：', 'yesterday、since、by the time、next week → 決定時態') + row('4. 看連接：', '有沒有 although、if、who、that、however？'), sub='Four-Step Check'),
  card('示範', ex('By the time we arrived, the movie <b>had started</b>.', '→ 步驟 3：by the time + 過去 → 過去完成式') +
    ex('The girl <b>sitting</b> next to me is my cousin.', '→ 步驟 2：已經有動詞 is，sitting 是分詞修飾') +
    ex('<i>Although</i> he was tired, he kept working.', '→ 步驟 4：前後是兩個子句，要連接詞', 'o'), 'o', sub='Example'))),

section('診斷 1：動詞形式（第 2–4、9 週）', table(['考點', '線索', '例句'], [
  ['完成進行式', 'for、since、all day', ('I <b>have been waiting</b> for an hour.', '我已經等了一個小時')],
  ['過去完成式', 'by the time、before + 過去', ('The train <b>had left</b> before we got there.', '我們到之前火車就開走了')],
  ['被動語態', '主詞是「被」做的', ('The bridge <b>was built</b> in 1990.', '這座橋建於 1990 年')],
  ['使役動詞', 'have / make / let + O + V', ('My mom <b>made</b> me <b>clean</b> my room.', '我媽叫我打掃房間')],
  ['V-ing / to V', '動詞後面接哪一種', ('I <b>enjoy reading</b>, and I <b>hope to travel</b>.', '我喜歡閱讀，也希望去旅行')],
], audio_col=2)),

section('診斷 2：假設與情態（第 6–8 週）', table(['考點', '公式', '例句'], [
  ['推測過去', 'must / can\'t have + p.p.', ('He <b>must have forgotten</b> the meeting.', '他一定是忘了開會')],
  ['後悔', 'should have + p.p.', ('I <b>should have studied</b> harder.', '我當初應該更用功')],
  ['與現在相反', 'If + 過去式, would + V', ('If I <b>had</b> more time, I <b>would learn</b> Japanese.', '如果我有更多時間，我會學日文')],
  ['與過去相反', 'If + had p.p., would have p.p.', ('If you <b>had asked</b>, I <b>would have helped</b>.', '如果你當時有問，我就會幫忙')],
  ['wish / as if', 'wish + 過去式 / had p.p.', ('I <b>wish</b> I <b>were</b> taller.', '真希望我高一點')],
], audio_col=2)),

section('診斷 3：子句與連接（第 11–14 週）', table(['考點', '判斷方法', '例句'], [
  ['關係代名詞', '先行詞是人 / 物；有沒有逗號', ('My aunt, <b>who</b> lives in Tainan, is a nurse.', '我住在台南的阿姨是護理師')],
  ['what / that', '前面有沒有先行詞', ('<b>What</b> he said is true.', '他說的是真的')],
  ['間接問句', '疑問詞 + 主詞 + 動詞', ('Do you know <b>where he lives</b>?', '你知道他住哪裡嗎？')],
  ['分詞構句', '主動 V-ing / 被動 p.p.', ('<b>Seen</b> from the hill, the city looks beautiful.', '從山上看，這座城市很美')],
  ['連接詞 / 轉折語', '子句、名詞，還是分號後', ('It rained; <b>however</b>, we still went out.', '下雨了，但我們還是出門了')],
], audio_col=2)),

section('診斷 4：形容詞、比較、倒裝、一致（第 1、16–18 週）', table(['考點', '判斷方法', '例句'], [
  ['-ed / -ing 形容詞', '人感到 -ed；事物令人 -ing', ('The movie was <b>boring</b>, so I felt <b>bored</b>.', '電影很無聊，所以我覺得很無聊')],
  ['as…as / 比較級', '中間原級；比較級用 much 加強', ('This road is <b>much wider than</b> that one.', '這條路比那條寬得多')],
  ['the 比較級', '兩邊都要 the', ('<b>The earlier</b> you leave, <b>the sooner</b> you arrive.', '你越早出發就越早到')],
  ['否定倒裝', '否定副詞在句首', ('<b>Rarely does</b> she complain.', '她很少抱怨')],
  ['強調句', 'It is / was…that', ('<b>It was</b> in the library <b>that</b> I met her.', '我是在圖書館遇見她的')],
  ['主詞動詞一致', '找真正的主詞', ('<b>Each</b> of the rooms <b>has</b> a window.', '每個房間都有一扇窗')],
], audio_col=2)),

section('閱讀題型策略', cards(2,
  card('四種常見題目', row('主旨題：', 'What is the passage mainly about? → 看第一段和最後一段') + row('細節題：', 'According to the passage… → 回原文找關鍵字') + row('推論題：', 'What can we infer…? → 找證據，不要憑感覺') + row('字義題：', 'The word "…" means… → 看前後文'), sub='Reading Strategies'),
  card('實際示範', ex('Although the plan sounded perfect, <b>few people</b> signed up.', '→ 推論：這個計畫其實不成功') +
    ex('The museum, <i>which</i> opened in 2010, attracts many tourists.', '→ 細節：博物館 2010 年開幕', 'o') +
    note('看到 however、but、although 後面，常常就是答案所在。'), 'o', sub='找線索'))),

section('聽力題型策略', cards(2,
  card('看圖辨義與問答', row('看圖辨義：', '先看圖：人在哪裡、做什麼、有幾個') + row('問答：', '聽清楚第一個字：Who、When、Why、How long') +
    ex('How long have you lived here? — <b>For five years.</b>', '→ How long → 一段時間') +
    ex('Why are you late? — <b>Because</b> I missed the bus.', '→ Why → 原因'), sub='Part 1 &amp; 2'),
  card('簡短對話', row('先看選項：', '猜會問人、地點、時間還是原因') + row('注意轉折：', 'but、actually、however 後面常是答案') +
    ex('I wanted to take the bus, <i>but actually</i> I walked.', '→ 答案是 walked', 'o') +
    ex('<i>Not until</i> Friday will the package arrive.', '→ 答案是 Friday', 'o'), 'o', sub='Part 3'))),

section('學生最常錯的 5 句（全期總整理）', top5([
  ('I have lived here since five years.', 'I have lived here for five years.', '一段時間用 for，時間點用 since。（第 2 週）'),
  ('If I was you, I will study harder.', 'If I were you, I would study harder.', '與現在事實相反：If + were, would + V。（第 7、8 週）'),
  ('Do you know where does he live?', 'Do you know where he lives?', '間接問句用直述語序。（第 13 週）'),
  ('Although it rained, but we went out.', 'Although it rained, we went out.', 'although 和 but 不能同時用。（第 14 週）'),
  ('The number of cars are increasing.', 'The number of cars is increasing.', 'the number of + 單數動詞。（第 18 週）'),
])),

section('快問快答 8 題（混合題）', qas([
  ('She ____ English for three years. (has studied / studies)', 'has studied'),
  ('The letter ____ yesterday. (was sent / sent)', 'was sent'),
  ('I wish I ____ fly. (could / can)', 'could'),
  ('This is the house ____ I was born. (where / which)', 'where'),
  ('____ tired, he went to bed early. (Feeling / Felt)', 'Feeling'),
  ('He is ____ taller than me. (much / very)', 'much'),
  ('Never ____ so happy. (have I been / I have been)', 'have I been'),
  ('Everyone in my class ____ a phone. (has / have)', 'has'),
])),

section('挑錯練習與中譯英', two(div(lead('挑錯：每句有一個錯'), qas([
  ('The man who live next door is a doctor.', 'live → lives'),
  ('I look forward to see you.', 'see → seeing'),
  ('She made me to wait for an hour.', '刪掉 to'),
])), div(lead('中譯英（英檢寫作第一部分）'), qas([
  ('我住在台北已經十年了。', 'I have lived in Taipei for ten years.'),
  ('如果明天下雨，我們就待在家。', 'If it rains tomorrow, we will stay home.'),
  ('他不但聰明，而且很用功。', 'He is not only smart but also hardworking.'),
])))),

section('口說：回答問題與看圖敘述的架構', cards(2,
  card('回答問題：三句法', row('1. 直接回答：', 'Yes, I do. / My favorite… is…') + row('2. 給理由：', 'because…、The reason is that…') + row('3. 舉例或感受：', 'For example…、That\'s why…') +
    ex('My favorite place is the library <b>because</b> it is quiet. <b>For example</b>, I often read there on weekends.', '→ 回答 + 理由 + 例子'), sub='Answer + Reason + Example'),
  card('看圖敘述：由大到小', row('1. 地點：', 'This picture shows…、In this picture, …') + row('2. 人物動作：', 'There are…、A girl is…') + row('3. 推測：', 'They might be…、It seems that…') +
    ex('<i>In this picture</i>, some students are eating lunch. They <i>seem to be</i> enjoying their food.', '→ 地點 + 動作 + 推測', 'o'), 'o', sub='Where → Who → What → Guess'))),

section('口說句型跟讀', lead('先按 🔊 聽，再跟著大聲念，最後換成自己的句子。') + two(div(
  ex('I <b>have been learning</b> English <b>for</b> six years.', '→ 完成進行式'),
  ex('<b>If I had</b> more free time, I <b>would</b> learn to play the piano.', '→ 與現在相反的假設'),
  ex('The person <b>who</b> helps me the most is my mother.', '→ 關係代名詞')), div(
  ex('<i>The more</i> I practice, <i>the more confident</i> I feel.', '→ the 比較級', 'o'),
  ex('<i>This picture shows</i> a girl standing next to a school bus.', '→ 看圖敘述開頭', 'o')))),

section('重點整理與測驗說明', two(div(
  table(['診斷類別', '週次', '自我檢查'], [
    ['動詞形式', '2–4、9', '時態線索、被動、V-ing / to V'],
    ['假設與情態', '6–8', 'must have、should have、If…were'],
    ['子句與連接', '11–14', '關代、what、間接問句、分詞構句'],
    ['比較倒裝一致', '1、16–18', 'as…as、Never have I、the number of']]),
  note('考試時遇到不會的題目，先用四步驟：看空格、數動詞、找時間、看連接。把錯的題目記下來，看是哪一類最常錯。')), div(
  card('本週測驗：64 題', row('題型：', '文法 20．閱讀 10．克漏字 4．單字 10．聽力 15．口說 5') + ul(['文法 20 題全部是混合題，分別來自四大診斷類別，每題說明會標出是第幾週的重點', '閱讀和聽力照英檢中級的出題方式設計']), 'o'),
  card('回家作業', ol(['做完測驗後，把錯的題目分到四大類，找出最弱的一類。', '把那一類對應週次的投影片再看一次。', '用「回答＋理由＋例子」回答：What do you like to do on weekends?']))))),
]
