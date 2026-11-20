# LaLa Word Unit 8（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 82–95 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 8, 'en': 'One Young Mind, Big Impact', 'zh': '一字多義（八）',
  'intro': 'catch 是接住，也是「趕上公車」「染上感冒」；break 是弄壞，也是「休息一下」。這個單元有 6 個主題單字、18 個更多單字，'
           '再整理 before／ago、after／later、work／job／career、problem／question，和字尾 -ist（artist、dentist、scientist）。',
  'words': [
    W('country', '🌾', [
        S('n.', '國家', 'Japan is a beautiful country.', '日本是一個美麗的國家。'),
        S('n.', '鄉下', 'My grandparents live in the country.', '我的祖父母住在鄉下。', 'in the country 在鄉下'),
    ], '複數 countries', key=True),
    W('deliver', '📦', [
        S('v.', '發表（演說）；傳達', 'The principal delivered a speech at the meeting.', '校長在大會上發表演說。', 'deliver a speech 發表演說'),
        S('v.', '遞送', 'Do you deliver food to this area?', '你們有外送到這一區嗎？'),
        S('v.', '履行（承諾）', 'He promised to help, and he delivered.', '他答應要幫忙，也真的做到了。'),
        S('v.', '接生', 'The doctor delivered the baby at 3 a.m.', '醫生在凌晨三點接生了寶寶。'),
    ], 'deliver - delivered - delivered - delivering', key=True),
    W('dream', '💭', [
        S('n.', '夢；夢想', 'I had a strange dream last night.', '我昨晚做了一個奇怪的夢。', 'a dream come true 夢想成真'),
        S('adj.', '夢想中的；理想的', 'This is my dream house.', '這是我夢想中的房子。'),
        S('v.', '做夢；夢想', 'She dreams of becoming a singer.', '她夢想成為歌手。', 'dream of / about 夢想；夢到'),
    ], 'dream - dreamed（dreamt） - dreamed（dreamt） - dreaming', key=True),
    W('fix', '🔧', [
        S('v.', '修理；整理；解決', 'Dad fixed my bike.', '爸爸修好了我的腳踏車。', 'fix up 修理；fix a problem 解決問題'),
        S('v.', '安排；確定', 'Let\'s fix a date for the party.', '我們來訂派對的日期吧。', 'fix a date 訂日期'),
        S('v.', '固定；盯著', 'Fix the poster on the wall with tape.', '用膠帶把海報固定在牆上。', 'fix one\'s eyes on 盯著'),
    ], 'fix - fixed - fixed - fixing', key=True),
    W('catch', '🥎', [
        S('v.', '偵測到；聽清楚', 'Sorry, I didn\'t catch your name.', '抱歉，我沒聽清楚你的名字。'),
        S('v.', '抓住；接住', 'Catch the ball!', '接住球！'),
        S('v.', '趕上（交通工具）', 'I ran to catch the bus.', '我跑去趕公車。'),
        S('v.', '染上（疾病）', 'I caught a cold last week.', '我上星期感冒了。', 'catch a cold 感冒'),
        S('v.', '吸引（目光）', 'The red dress caught my eye.', '那件紅洋裝吸引了我的目光。', 'catch one\'s eye 吸引某人的目光'),
        S('v.', '著（火）', 'The old house caught fire.', '那棟老房子著火了。', 'catch fire 著火'),
    ], 'catch - caught - caught - catching', key=True),
    W('save', '🐷', [
        S('v.', '救', 'The lifeguard saved the boy.', '救生員救了那個男孩。'),
        S('v.', '節省', 'Taking the MRT saves time.', '搭捷運省時間。'),
        S('v.', '存（錢）；保留', 'I\'m saving money for a new bike.', '我在存錢買新腳踏車。', 'save up for 為…存錢；save a seat 保留位子'),
    ], 'save - saved - saved - saving', key=True),
    W('act', '🎬', [
        S('v.', '行動；表現得', 'We must act fast.', '我們必須趕快行動。', 'act as if 表現得好像'),
        S('v.', '扮演', 'She acted as Snow White in the play.', '她在戲裡演白雪公主。'),
        S('n.', '行為', 'Helping others is a kind act.', '幫助別人是善良的行為。'),
    ], 'act - acted - acted - acting'),
    W('break', '☕', [
        S('v.', '打破；弄壞', 'Who broke the window?', '誰打破了窗戶？'),
        S('v.', '打破（紀錄）；分開', 'He broke the school record.', '他打破了學校的紀錄。', 'break the record 破紀錄；break up 分手'),
        S('v.', '違反', 'Don\'t break the rules.', '不要違反規定。', 'break one\'s word 不守承諾'),
        S('n.', '休息', 'Let\'s take a ten-minute break.', '我們休息十分鐘吧。', 'take a break 休息一下'),
        S('n.', '裂痕；骨折', 'The X-ray shows a break in his arm.', 'X 光顯示他的手臂骨折。'),
    ], 'break - broke - broken - breaking'),
    W('channel', '📺', [
        S('n.', '頻道', 'Let\'s change the channel.', '我們轉台吧。'),
        S('n.', '管道；途徑', 'The internet is a good channel for learning.', '網路是學習的好管道。'),
        S('n.', '海峽', 'The ship sailed through the channel.', '船駛過海峽。'),
    ], '複數 channels'),
    W('close', '🚪', [
        S('v.', '關上', 'Please close the window.', '請關窗。'),
        S('v.', '打烊；關門', 'The shop closes at nine.', '這家店九點打烊。'),
        S('adj.', '靠近的；親近的', 'My house is close to the school.', '我家離學校很近。', 'be close to 靠近；親近（形容詞唸 [klos]）'),
    ], 'close - closed - closed - closing；close - closer - closest'),
    W('drive', '🚗', [
        S('v.', '開車；載', 'Mom drives me to school every day.', '媽媽每天開車載我上學。'),
        S('v.', '迫使', 'The noise is driving me crazy.', '那噪音快把我逼瘋了。', 'drive + 人 + crazy 把人逼瘋'),
        S('n.', '車程；兜風', 'It\'s a two-hour drive to Taichung.', '到臺中要開兩小時的車。', 'go for a drive 去兜風'),
        S('n.', '幹勁；決心', 'She has the drive to win.', '她有贏的決心。'),
    ], 'drive - drove - driven - driving'),
    W('dry', '🏜️', [
        S('adj.', '乾的；乾燥的', 'My clothes are dry now.', '我的衣服乾了。', 'the dry season 乾季'),
        S('v.', '弄乾；變乾', 'Dry your hair before you go to bed.', '睡覺前把頭髮吹乾。'),
    ], 'dry - drier - driest；dry - dried - dried - drying'),
    W('floor', '🏢', [
        S('n.', '地板', 'The floor is wet. Be careful.', '地板濕濕的，小心。'),
        S('n.', '樓層', 'Our classroom is on the third floor.', '我們的教室在三樓。', 'on the + 序數 + floor 在第…樓'),
    ], '複數 floors'),
    W('grade', '💯', [
        S('n.', '年級', 'My sister is in fifth grade.', '我妹妹讀五年級。'),
        S('n.', '等級；品質', 'This is high-grade tea.', '這是高級茶葉。'),
        S('n.', '成績；分數', 'I got a good grade on the test.', '我考試得到好成績。', 'get a good / bad grade 得到好／壞成績'),
        S('v.', '評分', 'The teacher is grading our tests.', '老師正在改我們的考卷。'),
    ], 'grade - graded - graded - grading'),
    W('grow', '🌱', [
        S('v.', '生長；成長', 'Kids grow fast.', '小孩長得很快。', 'grow up 長大'),
        S('v.', '留長（頭髮）', 'I want to grow my hair long.', '我想把頭髮留長。'),
        S('v.', '種植', 'Grandpa grows tomatoes in his garden.', '爺爺在花園種番茄。'),
        S('v.', '變得', 'It grew dark outside.', '外面天色變暗了。'),
    ], 'grow - grew - grown - growing'),
    W('half', '🌗', [
        S('adj.', '一半的', 'I waited for half an hour.', '我等了半個小時。', 'half an hour 半小時；half a dozen 半打'),
        S('n.', '半票；一半', 'One adult and two halves, please.', '一張全票、兩張半票，謝謝。'),
    ], '複數 halves'),
    W('keep', '🧾', [
        S('v.', '保持', 'Keep quiet in the library.', '在圖書館要保持安靜。', 'keep + V-ing 持續做；keep in mind 記住；keep one\'s word 守信'),
        S('v.', '保留；留著', 'Keep the change.', '零錢不用找了。', 'keep the receipt 保留收據'),
    ], 'keep - kept - kept - keeping'),
    W('leave', '🚶', [
        S('v.', '離開', 'The train leaves at six.', '火車六點開。', 'leave for 前往'),
        S('v.', '留下；遺忘', 'I left my bag on the bus.', '我把包包忘在公車上。', 'leave a message 留言'),
        S('v.', '讓…保持某狀態', 'Don\'t leave the door open.', '別讓門開著。'),
        S('n.', '假期；休假', 'Ms. Chen is on leave this week.', '陳老師這星期請假。', 'on leave 休假中；sick leave 病假'),
    ], 'leave - left - left - leaving'),
    W('mop', '🧹', [
        S('v.', '拖（地）；擦', 'It\'s my turn to mop the floor.', '輪到我拖地了。'),
        S('n.', '拖把', 'Where is the mop?', '拖把在哪裡？'),
    ], 'mop - mopped - mopped - mopping'),
    W('move', '📦', [
        S('v.', '移動', 'Don\'t move! There\'s a bee on your arm.', '別動！你手上有一隻蜜蜂。'),
        S('v.', '搬家', 'We moved to Taipei last year.', '我們去年搬到臺北。'),
        S('v.', '採取行動；繼續前進', 'It\'s time to move on.', '該向前走了。', 'move on 放下；繼續前進'),
        S('v.', '使感動', 'Everyone was moved by her story.', '每個人都被她的故事感動。'),
        S('n.', '行動；舉動', 'It\'s your move.', '輪到你走了（下棋）。'),
    ], 'move - moved - moved - moving'),
    W('past', '🕰️', [
        S('n.', '過去', 'In the past, people wrote letters.', '以前人們寫信。', 'in the past 在過去'),
        S('adj.', '過去的', 'It has been hot for the past few days.', '過去幾天都很熱。'),
        S('adv.', '經過', 'A bus went past.', '一輛公車開過去了。'),
        S('prep.', '（時間）過了', 'It\'s half past seven.', '現在七點半。'),
    ]),
    W('pet', '🐶', [
        S('n.', '寵物', 'Do you have any pets?', '你有養寵物嗎？', 'keep a pet 養寵物'),
        S('v.', '撫摸', 'You can pet the rabbit gently.', '你可以輕輕摸兔子。'),
    ], 'pet - petted - petted - petting'),
    W('quarter', '🕒', [
        S('n.', '四分之一', 'Cut the cake into quarters.', '把蛋糕切成四份。'),
        S('n.', '十五分鐘', 'It\'s a quarter past three.', '現在三點十五分。', 'a quarter past / to 過／差十五分'),
        S('n.', '季度（三個月）', 'Sales went up in the second quarter.', '第二季的銷售量上升了。'),
    ], '複數 quarters'),
    W('through', '🚇', [
        S('prep.', '穿過', 'The train went through the tunnel.', '火車穿過隧道。', 'get through 熬過；通過'),
        S('prep.', '透過', 'I found this job through a friend.', '我透過朋友找到這份工作。'),
        S('adv.', '徹底地', 'Read the letter through before you sign it.', '簽名前把信從頭到尾看完。'),
    ]),
    W('artist', '🎨', [
        S('n.', '藝術家；畫家', 'Van Gogh was a famous artist.', '梵谷是有名的藝術家。'),
    ], 'art 藝術 + -ist；複數 artists'),
    W('dentist', '🦷', [
        S('n.', '牙醫', 'I have a toothache. I need to see a dentist.', '我牙痛，要去看牙醫。', 'see a dentist 看牙醫'),
    ], 'dent（牙齒）+ -ist；複數 dentists'),
    W('scientist', '🔬', [
        S('n.', '科學家', 'She wants to be a scientist.', '她想當科學家。'),
    ], 'science 科學 + -ist；複數 scientists'),
  ],
  'focus': [
    {'title': '易混淆字：before 和 ago', 'head': ('單字', '用法', '例句'), 'rows': [
      ('before', '在…之前；也可以單獨用「以前」，常和完成式一起用', 'I have seen this movie before.／before lunch'),
      ('ago', '時間 + ago，從現在算回去多久以前，用過去式', 'I met him two years ago.'),
    ], 'note': ''},
    {'title': '易混淆字：after 和 later', 'head': ('單字', '用法', '例句'), 'rows': [
      ('after', '在某件事、某時間之後：after + 名詞／子句', 'Let\'s play after school.'),
      ('later', '「之後；晚一點」，可以單獨用：see you later、three days later', 'See you later!'),
    ], 'note': ''},
    {'title': '易混淆字：work／job／career', 'head': ('單字', '用法', '例句'), 'rows': [
      ('work', '工作（不可數）；也當動詞', 'I have a lot of work to do.'),
      ('job', '一份工作（可數）', 'She got a part-time job.'),
      ('career', '長期的職業生涯、事業', 'He wants a career in music.'),
    ], 'note': ''},
    {'title': '易混淆字：problem 和 question', 'head': ('單字', '用法', '例句'), 'rows': [
      ('problem', '需要「解決」的問題、困難', 'We need to solve this problem.'),
      ('question', '需要「回答」的問題', 'May I ask a question?'),
    ], 'note': ''},
    {'title': '字尾 -ist：從事某領域的人', 'head': ('原來的字', '加 -ist', '意思'), 'rows': [
      ('art 藝術', 'artist', '藝術家'),
      ('dent（拉丁文：牙齒）', 'dentist', '牙醫'),
      ('science 科學', 'scientist', '科學家'),
      ('piano 鋼琴', 'pianist', '鋼琴家'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'My grandparents moved to the <b>country</b> after they retired.', 'opts': ['國家', '鄉下', '城市', '國外'], 'answer': 1, 'exp': 'the country 鄉下。'},
    {'type': 'mc', 'q': 'Hurry up, or you won\'t <b>catch</b> the last train.', 'opts': ['抓住', '趕上', '染上', '吸引'], 'answer': 1, 'exp': 'catch the train 趕上火車。'},
    {'type': 'mc', 'q': 'You look tired. Let\'s take a <b>break</b>.', 'opts': ['弄壞', '裂痕', '休息', '分手'], 'answer': 2, 'exp': 'take a break 休息一下。'},
    {'type': 'mc', 'q': 'I live very <b>close</b> to the MRT station.', 'opts': ['關上', '打烊', '靠近的', '親密的'], 'answer': 2, 'exp': 'close to 靠近。'},
    {'type': 'mc', 'q': 'The crying baby is <b>driving</b> me crazy.', 'opts': ['開車', '迫使', '車程', '決心'], 'answer': 1, 'exp': 'drive + 人 + crazy 把人逼瘋。'},
    {'type': 'mc', 'q': 'Mr. Lin <b>grades</b> our homework every night.', 'opts': ['年級', '等級', '分數', '評分'], 'answer': 3, 'exp': 'grade 動詞：評分。'},
    {'type': 'mc', 'q': 'We were <b>moved</b> by the old man\'s story.', 'opts': ['搬家', '移動', '感動', '行動'], 'answer': 2, 'exp': 'be moved by 被…感動。'},
    {'type': 'mc', 'q': 'The company did well in the first <b>quarter</b> of the year.', 'opts': ['四分之一', '十五分鐘', '季度', '角落'], 'answer': 2, 'exp': '公司的 first quarter 第一季。'},
    {'type': 'mc', 'q': 'The pizza shop <b>delivers</b> until midnight.', 'opts': ['發表', '外送', '履行', '接生'], 'answer': 1, 'exp': '披薩店 deliver → 外送。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Can you help me ______ my computer?  ／  Let\'s ______ a time for the meeting.', 'opts': ['repair', 'fix', 'set', 'make'], 'answer': 1, 'exp': 'fix 修理／訂（時間）。'},
    {'type': 'mc', 'q': 'Doctors ______ lives every day.  ／  I ______ 100 dollars every week.', 'opts': ['help', 'save', 'keep', 'catch'], 'answer': 1, 'exp': 'save 救／存錢。'},
    {'type': 'mc', 'q': 'The ______ is wet.  ／  My office is on the 12th ______.', 'opts': ['ground', 'floor', 'level', 'room'], 'answer': 1, 'exp': 'floor 地板／樓層。'},
    {'type': 'mc', 'q': 'Let\'s watch the cartoon ______.  ／  The English ______ is between England and France.', 'opts': ['show', 'channel', 'river', 'station'], 'answer': 1, 'exp': 'channel 頻道／海峽。'},
    {'type': 'mc', 'q': 'Don\'t ______ your umbrella on the bus.  ／  Mr. Wu is on sick ______ today.', 'opts': ['forget', 'leave', 'lose', 'rest'], 'answer': 1, 'exp': 'leave 遺留／休假。'},
  ]},
  {'title': '③ 易混淆字：選出正確的字', 'items': [
    {'type': 'mc', 'q': 'I visited Kenting three years ______.', 'opts': ['before', 'ago', 'after', 'later'], 'answer': 1, 'exp': '時間 + ago。'},
    {'type': 'mc', 'q': 'Wash your hands ______ you eat.', 'opts': ['ago', 'before', 'later', 'past'], 'answer': 1, 'exp': 'before + 子句。'},
    {'type': 'mc', 'q': 'I\'m busy now. Can I call you ______?', 'opts': ['after', 'later', 'ago', 'before'], 'answer': 1, 'exp': '單獨用「晚一點」→ later。'},
    {'type': 'mc', 'q': 'My brother found a part-time ______ at a café.', 'opts': ['work', 'job', 'career', 'works'], 'answer': 1, 'exp': 'a job 一份工作（可數）。'},
    {'type': 'mc', 'q': 'There is a ______ with my phone. It won\'t turn on.', 'opts': ['question', 'problem', 'answer', 'job'], 'answer': 1, 'exp': '需要解決的 → problem。'},
    {'type': 'mc', 'q': 'I have a toothache, so I\'m going to see a ______.', 'opts': ['scientist', 'artist', 'dentist', 'pianist'], 'answer': 2, 'exp': '牙痛看牙醫 dentist。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Winning the gold medal was a {0} come true. （夢想）', 'blanks': [['dream']], 'exp': 'a dream come true 夢想成真。'},
    {'q': 'I caught a {0} because I didn\'t wear a coat. （感冒）', 'blanks': [['cold']], 'exp': 'catch a cold 感冒。'},
    {'q': 'What do you want to be when you grow {0}? （長大）', 'blanks': [['up']], 'exp': 'grow up 長大。'},
    {'q': 'Please keep {0} mind that the test is on Friday. （記住）', 'blanks': [['in']], 'exp': 'keep in mind 記住。'},
    {'q': 'It\'s a quarter {0} four. （過了，四點十五分）', 'blanks': [['past']], 'exp': 'a quarter past four 四點十五分。'},
    {'q': 'My friends helped me get {0} the hard times. （熬過）', 'blanks': [['through']], 'exp': 'get through 熬過。'},
  ]},
]
