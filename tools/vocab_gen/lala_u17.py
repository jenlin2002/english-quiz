# LaLa Word Unit 17（字表與每個字有哪些意思照課本；例句、中文、題目都自編，不搬課本）
# 課本印刷頁第 189–195 頁（PDF 頁序＝印刷頁碼－1）

def S(pos, zh, ex, exzh, ph=''):
    return {'pos': pos, 'zh': zh, 'ex': ex, 'exzh': exzh, 'ph': ph}


def W(w, pic, senses, forms='', key=False):
    return {'w': w, 'pic': pic, 'senses': senses, 'forms': forms, 'key': key}


UNIT = {
  'book': 'lala', 'no': 17, 'en': 'Why Taylor Swift\'s Music Stays in Our Hearts', 'zh': '一字多義（十七）',
  'intro': 'present 是禮物，也是「現在」和「發表」；spot 是地點，也是「斑點」和「看見」。這個單元有 4 個主題單字、6 個更多單字，'
           '最後整理都是「禮物」的 gift／present。',
  'words': [
    W('follow', '👣', [
        S('v.', '關注；追蹤', 'I follow my favorite singer on Instagram.', '我在 IG 上追蹤我最喜歡的歌手。'),
        S('v.', '跟著', 'Follow me. I\'ll show you the way.', '跟我來，我帶你去。'),
        S('v.', '遵守', 'Please follow the rules.', '請遵守規則。'),
        S('v.', '理解；聽懂', 'Sorry, I can\'t follow you. Can you say it again?', '抱歉，我聽不懂，可以再說一次嗎？'),
        S('v.', '接著發生', 'Dinner was followed by a movie.', '晚餐後接著看電影。'),
    ], 'follow - followed - followed - following', key=True),
    W('case', '💼', [
        S('n.', '情況', 'In that case, let\'s stay home.', '那樣的話，我們就待在家吧。', 'in that case 那樣的話；in case 以防萬一'),
        S('n.', '案件；病例', 'There are more flu cases this winter.', '今年冬天流感病例變多了。'),
        S('n.', '盒；箱；套', 'Put your glasses in the case.', '把眼鏡放進盒子裡。', 'pencil case 鉛筆盒；bookcase 書架'),
    ], '複數 cases', key=True),
    W('present', '🎁', [
        S('n.', '現在', 'Forget the past and enjoy the present.', '忘了過去，享受現在。', 'at present 目前（唸 [ˋprɛznt]）'),
        S('n.', '禮物', 'Thank you for the birthday present.', '謝謝你的生日禮物。'),
        S('adj.', '在場的；出席的', 'All the students are present today.', '今天全班都到齊了。'),
        S('adj.', '目前的', 'What is your present address?', '你目前的地址是什麼？'),
        S('v.', '發表；提出', 'Each group will present its report.', '每一組都要上台報告。', '動詞唸 [prɪˋzɛnt]'),
        S('v.', '頒發；給予', 'The principal presented the prizes to the winners.', '校長把獎頒給優勝者。'),
    ], 'present - presented - presented - presenting', key=True),
    W('spot', '🐆', [
        S('n.', '地點', 'This is a great spot for a picnic.', '這是野餐的好地點。', 'on the spot 當場；立刻'),
        S('n.', '斑點；汙漬', 'A leopard has black spots.', '豹身上有黑色斑點。'),
        S('n.', '痘痘', 'I have a spot on my nose.', '我鼻子上長了一顆痘痘。'),
        S('v.', '看見；發現', 'Can you spot the difference?', '你看得出差別嗎？'),
    ], 'spot - spotted - spotted - spotting', key=True),
    W('deal', '🤝', [
        S('v.', '處理；應付', 'I can deal with this problem.', '這個問題我可以處理。', 'deal with 處理'),
        S('v.', '販賣；做生意', 'The shop deals in old books.', '這家店專賣舊書。'),
        S('v.', '發（牌）', 'It\'s your turn to deal the cards.', '輪到你發牌了。'),
        S('n.', '交易；划算的買賣', 'This bike is a good deal.', '這台腳踏車買得很划算。', 'It\'s no big deal. 沒什麼大不了'),
        S('n.', '大量', 'He spends a great deal of time on games.', '他花很多時間打電動。', 'a great deal of 很多'),
    ], 'deal - dealt - dealt - dealing'),
    W('degree', '🌡️', [
        S('n.', '度（溫度、角度）', 'It\'s 30 degrees today.', '今天三十度。'),
        S('n.', '學位', 'My aunt has a degree in music.', '我阿姨有音樂學位。'),
        S('n.', '程度', 'I agree with you to some degree.', '我某種程度上同意你。'),
    ], '複數 degrees'),
    W('form', '📋', [
        S('v.', '形成；組成', 'The students formed a circle.', '學生們圍成一個圈。'),
        S('n.', '表格', 'Please fill out this form.', '請填寫這份表格。', 'fill out a form 填表格'),
        S('n.', '形式；樣子', 'The past form of "eat" is "ate."', 'eat 的過去式是 ate。'),
        S('n.', '類型', 'Walking is a good form of exercise.', '走路是一種很好的運動。'),
    ], 'form - formed - formed - forming'),
    W('stamp', '📮', [
        S('n.', '郵票', 'I need a stamp for this letter.', '這封信需要一張郵票。'),
        S('n.', '印章；戳記', 'The teacher put a star stamp on my homework.', '老師在我的作業上蓋了星星章。'),
        S('v.', '蓋章', 'Stamp the card when you get here.', '到了這裡就在卡上蓋章。'),
        S('v.', '跺腳', 'The angry boy stamped his feet.', '生氣的男孩跺腳。'),
    ], 'stamp - stamped - stamped - stamping'),
    W('step', '👟', [
        S('n.', '步驟；階段', 'Follow the steps to make the cake.', '照著步驟做蛋糕。', 'step by step 一步一步'),
        S('n.', '措施', 'We must take steps to save water.', '我們必須採取措施節約用水。', 'take steps 採取措施'),
        S('n.', '腳步', 'Take one step forward.', '向前走一步。', 'in step 步伐一致'),
        S('n.', '臺階', 'Watch your step!', '小心腳下的臺階！'),
    ], 'step - stepped - stepped - stepping'),
    W('while', '⏳', [
        S('conj.', '當…的時候', 'The phone rang while I was taking a shower.', '我在洗澡的時候電話響了。'),
        S('conj.', '然而', 'I like dogs, while my sister likes cats.', '我喜歡狗，而我妹妹喜歡貓。'),
        S('conj.', '雖然', 'While the test was hard, I passed it.', '雖然考試很難，我還是通過了。'),
        S('n.', '一段時間', 'Please wait for a while.', '請稍等一會兒。', 'for a while 一會兒'),
    ]),
  ],
  'focus': [
    {'title': '易混淆字：gift 和 present', 'head': ('單字', '用法', '例句'), 'rows': [
      ('gift', '禮物（比較正式，也用在商業：gift card、gift shop）；天分', 'She has a gift for music.'),
      ('present', '禮物（日常說法）；也當「現在的、在場的」「發表、贈送」', 'I got a birthday present.'),
    ], 'note': 'present 名詞、形容詞唸 [ˋprɛznt]，動詞唸 [prɪˋzɛnt]。'},
    {'title': '一字多義：最常見 vs. 容易忽略的意思', 'head': ('單字', '最常見的意思', '容易忽略的意思'), 'rows': [
      ('follow', '跟著', '關注；聽懂'),
      ('case', '情況', '盒子；病例'),
      ('present', '禮物', '現在；在場的；發表'),
      ('spot', '地點', '斑點；痘痘；看見'),
      ('deal', '交易', '處理；發牌'),
      ('degree', '度', '學位；程度'),
      ('form', '表格', '形成；形式'),
      ('stamp', '郵票', '蓋章；跺腳'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '意思', '例句'), 'rows': [
      ('in that case', '那樣的話', 'In that case, I\'ll take a taxi.'),
      ('on the spot', '當場；立刻', 'He answered on the spot.'),
      ('deal with', '處理', 'How do you deal with stress?'),
      ('It\'s no big deal.', '沒什麼大不了', 'Don\'t worry. It\'s no big deal.'),
      ('fill out a form', '填表格', 'Fill out this form, please.'),
      ('step by step', '一步一步', 'Learn it step by step.'),
      ('for a while', '一會兒', 'Let\'s rest for a while.'),
    ], 'note': ''},
  ],
}

QUIZ = [
  {'title': '① 這個字在句子裡是什麼意思？', 'items': [
    {'type': 'mc', 'q': 'Sorry, I can\'t <b>follow</b> you. You\'re talking too fast.', 'opts': ['跟著', '遵守', '聽懂', '追蹤'], 'answer': 2, 'exp': '說太快聽不懂。'},
    {'type': 'mc', 'q': 'There are fewer flu <b>cases</b> this year.', 'opts': ['情況', '病例', '盒子', '箱子'], 'answer': 1, 'exp': 'flu cases 流感病例。'},
    {'type': 'mc', 'q': 'Twenty students were <b>present</b> at the meeting.', 'opts': ['禮物', '現在', '出席的', '發表'], 'answer': 2, 'exp': 'be present at 出席。'},
    {'type': 'mc', 'q': 'I <b>spotted</b> my friend in the crowd.', 'opts': ['地點', '斑點', '看見', '弄髒'], 'answer': 2, 'exp': 'spot 動詞：看見。'},
    {'type': 'mc', 'q': 'Mom knows how to <b>deal</b> with angry customers.', 'opts': ['處理', '發牌', '交易', '販賣'], 'answer': 0, 'exp': 'deal with 處理。'},
    {'type': 'mc', 'q': 'My sister got a <b>degree</b> in science.', 'opts': ['度', '學位', '程度', '證書'], 'answer': 1, 'exp': 'a degree in 某科學位。'},
    {'type': 'mc', 'q': 'Swimming is a good <b>form</b> of exercise.', 'opts': ['表格', '形成', '類型', '形狀'], 'answer': 2, 'exp': 'a form of 一種…。'},
    {'type': 'mc', 'q': 'The angry child <b>stamped</b> his feet.', 'opts': ['蓋章', '郵票', '跺腳', '踩到'], 'answer': 2, 'exp': 'stamp one\'s feet 跺腳。'},
    {'type': 'mc', 'q': 'I like tea, <b>while</b> my brother likes coffee.', 'opts': ['當…時', '然而', '一會兒', '因為'], 'answer': 1, 'exp': '對比 → 然而。'},
  ]},
  {'title': '② 選出可以同時填入兩句的字', 'items': [
    {'type': 'mc', 'q': 'Put your pens in your pencil ______.  ／  In that ______, we\'ll leave early.', 'opts': ['box', 'case', 'bag', 'time'], 'answer': 1, 'exp': 'case 盒子／情況。'},
    {'type': 'mc', 'q': 'This is a nice ______ for a photo.  ／  The dog has black and white ______s.', 'opts': ['place', 'spot', 'point', 'dot'], 'answer': 1, 'exp': 'spot 地點／斑點。'},
    {'type': 'mc', 'q': 'I need a ______ for this postcard.  ／  The teacher put a smiley ______ on my book.', 'opts': ['stamp', 'sticker', 'mark', 'seal'], 'answer': 0, 'exp': 'stamp 郵票／印章。'},
    {'type': 'mc', 'q': 'Mind the ______ when you get off.  ／  We should take ______s to stop the problem.', 'opts': ['gap', 'step', 'stair', 'action'], 'answer': 1, 'exp': 'step 臺階／措施。'},
    {'type': 'mc', 'q': 'It\'s 25 ______s outside.  ／  I agree with you to some ______.', 'opts': ['degree', 'level', 'point', 'grade'], 'answer': 0, 'exp': 'degree 度／程度。'},
  ]},
  {'title': '③ 易混淆字：gift／present', 'items': [
    {'type': 'mc', 'q': 'My grandpa has a ______ for telling stories.', 'opts': ['gift', 'present', 'presents', 'gifted'], 'answer': 0, 'exp': '天分 → gift。'},
    {'type': 'mc', 'q': 'Everyone in our class is ______ today.', 'opts': ['gift', 'present', 'gifts', 'presented'], 'answer': 1, 'exp': '在場的 → present。'},
    {'type': 'mc', 'q': 'I bought a ______ card for my teacher.', 'opts': ['gift', 'present', 'presenting', 'gifts'], 'answer': 0, 'exp': 'gift card 禮物卡。'},
    {'type': 'mc', 'q': 'Each student will ______ a short speech.', 'opts': ['gift', 'present', 'give a gift', 'presents'], 'answer': 1, 'exp': '發表 → present（動詞）。'},
  ]},
  {'title': '④ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please {0} the traffic rules. （遵守）', 'blanks': [['follow']], 'exp': 'follow the rules 遵守規則。'},
    {'q': 'Don\'t worry. It\'s no big {0}. （沒什麼大不了）', 'blanks': [['deal']], 'exp': 'It\'s no big deal.'},
    {'q': 'Please fill out this {0} before you see the doctor. （表格）', 'blanks': [['form']], 'exp': 'fill out a form 填表格。'},
    {'q': 'Learn to cook step by {0}. （一步一步）', 'blanks': [['step']], 'exp': 'step by step。'},
    {'q': 'Can you wait for a {0}? （一會兒）', 'blanks': [['while']], 'exp': 'for a while 一會兒。'},
    {'q': 'He answered the question on the {0}. （當場）', 'blanks': [['spot']], 'exp': 'on the spot 當場；立刻。'},
  ]},
]
