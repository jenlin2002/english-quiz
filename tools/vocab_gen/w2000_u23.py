# 主題 2000 字 Unit 23：Occupations 職業（字表依課本單元；詞性、中文、例句、題目為本站自編）
# cook 在 Unit 10、14 出現過（煮），這裡用「廚師」的意思。
def W(w, zh, note, ex, exzh, pic, pos='n.'):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 23, 'en': 'Occupations', 'zh': '職業',
  'intro': '30 個和工作、職業有關的字。很多職業是「動作＋-er／-or」（drive → driver、act → actor），也有 -man 結尾、複數變 -men 的字。',
  'words': [
    W('actor', '演員；男演員', 'act（演）＋-or', 'The actor practiced his lines every night.', '那位演員每天晚上練台詞。', '🎬'),
    W('actress', '女演員', '複數 actresses', 'She became a famous actress at the age of twenty.', '她二十歲就成了有名的女演員。', '🎭'),
    W('boss', '老闆；主人', '複數 bosses', 'My boss lets us go home early on Fridays.', '我老闆星期五讓我們早點回家。', '👔'),
    W('businessman', '生意人；企業家', '複數 businessmen', 'The businessman flies to Japan twice a month.', '那位生意人一個月飛日本兩次。', '💼'),
    W('clerk', '職員；店員', '', 'The clerk at the counter helped me find my size.', '櫃台店員幫我找到我的尺寸。', '🧾'),
    W('cook', '廚師', '也當動詞「煮」；cooker 是「炊具」，不是廚師', 'The cook in this restaurant makes great fried rice.', '這家餐廳的廚師炒飯做得很棒。', '👨‍🍳'),
    W('dentist', '牙醫', '', 'Visit the dentist twice a year to check your teeth.', '一年要看兩次牙醫檢查牙齒。', '🦷'),
    W('doctor', '醫生；博士', '縮寫 Dr.', 'The doctor told me to drink more water.', '醫生叫我多喝水。', '🩺'),
    W('driver', '司機；駕駛', 'drive（開車）＋-r', 'The bus driver said hello to every student.', '公車司機和每個學生打招呼。', '🚌'),
    W('engineer', '工程師；技師', '', 'The engineer is fixing the computer system.', '工程師正在修電腦系統。', '👷'),
    W('farmer', '農夫；農民', 'farm（農場）＋-er', 'The farmer grows rice and corn.', '那位農夫種稻米和玉米。', '🧑‍🌾'),
    W('fisherman', '漁夫；漁民', '複數 fishermen', 'The fisherman goes out to sea before sunrise.', '漁夫在日出前出海。', '🎣'),
    W('housewife', '家庭主婦', '複數 housewives', 'My aunt is a housewife and takes care of three kids.', '我阿姨是家庭主婦，照顧三個孩子。', '🏠'),
    W('lawyer', '律師', 'law（法律）＋-yer', 'You should talk to a lawyer before you sign it.', '你簽名之前應該先問律師。', '⚖️'),
    W('mailman', '郵差', '複數 mailmen；現在常說 mail carrier', 'The mailman brings letters every morning.', '郵差每天早上送信來。', '📬'),
    W('nurse', '護士', '', 'The nurse took my temperature.', '護士幫我量了體溫。', '🧑‍⚕️'),
    W('police officer', '警官；警員', 'police 是警方（複數）；一位警察是 a police officer', 'A police officer showed us the way to the station.', '一位警察告訴我們去車站的路。', '👮'),
    W('reporter', '記者', 'report（報導）＋-er', 'The reporter asked the singer some questions.', '記者問了歌手幾個問題。', '🎤'),
    W('salesman', '推銷員；業務員', '複數 salesmen', 'The salesman showed us three kinds of phones.', '業務員給我們看了三種手機。', '🤝'),
    W('secretary', '秘書', '複數 secretaries', 'The secretary answers the phone for the boss.', '秘書幫老闆接電話。', '📞'),
    W('shopkeeper', '店主；老闆', 'shop（店）＋keeper（看管的人）', 'The shopkeeper knows every kid on this street.', '那位店老闆認識這條街上每個小孩。', '🏪'),
    W('singer', '歌手', 'sing（唱）＋-er', 'She wants to be a singer when she grows up.', '她長大想當歌手。', '🎙️'),
    W('soldier', '士兵；軍人', '', 'The soldiers helped people after the typhoon.', '颱風過後軍人幫忙災民。', '🪖'),
    W('waiter', '（男）服務生', '', 'The waiter brought us the menu.', '服務生拿菜單給我們。', '🍽️'),
    W('waitress', '（女）服務生', '複數 waitresses', 'The waitress asked what we wanted to drink.', '女服務生問我們要喝什麼。', '☕'),
    W('worker', '工人', 'work（工作）＋-er', 'The workers are building a new bridge.', '工人們正在蓋一座新橋。', '👷‍♂️'),
    W('writer', '作家', 'write（寫）＋-r', 'J.K. Rowling is a famous writer.', 'J.K. 羅琳是一位有名的作家。', '✍️'),
    W('business', '生意；企業；公司', '做生意的事不可數；公司可數', 'My uncle runs a small business in Tainan.', '我叔叔在臺南經營一家小公司。', '🏢'),
    W('job', '工作', '可數：a job、two jobs', 'My sister found a part-time job at a bookstore.', '我姊姊在書店找到一份兼職工作。', '💼'),
    W('work', '工作；作品', '工作不可數（a lot of work）；作品可數', 'I have a lot of work to do today.', '我今天有很多工作要做。', '🛠️', pos='n./v.'),
  ],
  'focus': [
    {'title': '職業字怎麼來的', 'head': ('規則', '例子', ''), 'rows': [
      ('動詞＋-er', 'drive → driver、sing → singer、report → reporter、write → writer、work → worker', ''),
      ('名詞＋-er', 'farm → farmer、law → lawyer', ''),
      ('動詞＋-or', 'act → actor', ''),
      ('…＋-man（複數 -men）', 'businessman、fisherman、mailman、salesman', ''),
      ('女性：-ess', 'actor → actress、waiter → waitress', ''),
    ], 'note': '注意：cook 本身就是「廚師」，cooker 是「炊具、電鍋」。'},
    {'title': '特別的複數', 'head': ('單數', '複數', ''), 'rows': [
      ('businessman', 'businessmen', ''),
      ('fisherman', 'fishermen', ''),
      ('housewife', 'housewives', ''),
      ('secretary', 'secretaries', ''),
      ('actress / waitress / boss', 'actresses / waitresses / bosses', ''),
    ], 'note': '-man → -men；-fe → -ves；子音＋y → -ies；-ss → -sses。'},
    {'title': '問職業、job 和 work', 'head': ('說法', '中文', ''), 'rows': [
      ('What does your father do? — He is an engineer.', '你爸爸做什麼工作？——他是工程師。', ''),
      ('What do you want to be? — I want to be a doctor.', '你想當什麼？——我想當醫生。', ''),
      ('She has a job. / She has two jobs.', '她有一份工作。／她有兩份工作。（job 可數）', ''),
      ('I have a lot of work.', '我有很多工作。（work 不可數）', ''),
    ], 'note': '說職業要加 a／an：He is a nurse. / She is an actress.'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '律師', 'opts': ['lawyer', 'farmer', 'writer', 'reporter'], 'answer': 0, 'exp': 'lawyer 律師（law 法律）。'},
    {'type': 'mc', 'q': '牙醫', 'opts': ['doctor', 'nurse', 'dentist', 'engineer'], 'answer': 2, 'exp': 'dentist 牙醫。'},
    {'type': 'mc', 'q': '秘書', 'opts': ['secretary', 'singer', 'soldier', 'salesman'], 'answer': 0, 'exp': 'secretary 秘書。'},
    {'type': 'mc', 'q': '家庭主婦', 'opts': ['house', 'housework', 'housewife', 'household'], 'answer': 2, 'exp': 'housewife 家庭主婦。'},
    {'type': 'mc', 'q': '漁夫', 'opts': ['farmer', 'fisherman', 'mailman', 'businessman'], 'answer': 1, 'exp': 'fisherman 漁夫。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'clerk', 'opts': ['時鐘', '職員；店員', '廚師', '老闆'], 'answer': 1, 'exp': 'clerk 職員、店員；clock 才是時鐘。'},
    {'type': 'mc', 'q': 'soldier', 'opts': ['士兵；軍人', '推銷員', '店主', '警察'], 'answer': 0, 'exp': 'soldier 士兵、軍人。'},
    {'type': 'mc', 'q': 'engineer', 'opts': ['引擎', '工人', '司機', '工程師'], 'answer': 3, 'exp': 'engineer 工程師；engine 才是引擎。'},
    {'type': 'mc', 'q': 'shopkeeper', 'opts': ['顧客', '店主；老闆', '收銀機', '警衛'], 'answer': 1, 'exp': 'shopkeeper 店主。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '記者（r＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['reporter']], 'exp': 'report＋-er＝reporter。'},
    {'q': '護士（n＿＿＿＿，5 個字母）：{0}', 'blanks': [['nurse']], 'exp': 'nurse。'},
    {'q': '女演員（a＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['actress']], 'exp': 'actor → actress。'},
    {'q': '作家（w＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['writer']], 'exp': 'write＋-r＝writer，只有一個 t。'},
    {'q': '工作（j＿＿，3 個字母，可數）：{0}', 'blanks': [['job']], 'exp': 'job。'},
  ]},
  {'title': '④ 單字變化', 'note': '照括號的提示寫出正確的字。', 'items': [
    {'q': 'drive → (開車的人) {0}', 'blanks': [['driver']], 'exp': 'drive＋-r → driver。'},
    {'q': 'farm → (在農場工作的人) {0}', 'blanks': [['farmer']], 'exp': 'farm＋-er → farmer。'},
    {'q': 'waiter → (女性) {0}', 'blanks': [['waitress']], 'exp': 'waiter → waitress。'},
    {'q': 'businessman → (複數) {0}', 'blanks': [['businessmen']], 'exp': '-man → -men。'},
    {'q': 'housewife → (複數) {0}', 'blanks': [['housewives']], 'exp': '-fe → -ves。'},
  ]},
  {'title': '⑤ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The {0} brought our food to the table. （男服務生）', 'blanks': [['waiter']], 'exp': '送餐的男服務生 → waiter。'},
    {'q': 'I have a toothache. I need to see a {0}. （牙醫）', 'blanks': [['dentist']], 'exp': '牙痛看牙醫 → dentist。'},
    {'q': 'The {0} caught the thief last night. （警察，兩個字）', 'blanks': [['police officer']], 'exp': 'a police officer 一位警察。'},
    {'q': 'Lady Gaga is a famous {0}. （歌手）', 'blanks': [['singer']], 'exp': '歌手 → singer。'},
    {'q': 'The {0} delivers letters to our house every day. （郵差）', 'blanks': [['mailman', 'mail carrier']], 'exp': '郵差 → mailman（mail carrier 也對）。'},
    {'q': 'The {0} are building a road near my school. （工人，複數）', 'blanks': [['workers']], 'exp': '工人們 → workers。'},
  ]},
  {'title': '⑥ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'A: What does your mother ______?  B: She is a nurse.', 'opts': ['do', 'does', 'job', 'work'], 'answer': 0, 'exp': '問職業：What does she do?'},
    {'type': 'mc', 'q': 'My father is ______ engineer.', 'opts': ['a', 'an', 'the', '（不填）'], 'answer': 1, 'exp': 'engineer 母音開頭 → an engineer。'},
    {'type': 'mc', 'q': 'I have too much ______ to do today.', 'opts': ['job', 'jobs', 'work', 'works'], 'answer': 2, 'exp': '「工作量」用不可數的 work：too much work。'},
    {'type': 'mc', 'q': 'My mom is a great ______. Her beef noodles are the best.', 'opts': ['cooker', 'cook', 'cooking', 'cooks'], 'answer': 1, 'exp': '廚師是 cook；cooker 是炊具。'},
    {'type': 'mc', 'q': 'The ______ asked the boss many questions for the news.', 'opts': ['soldier', 'farmer', 'reporter', 'dentist'], 'answer': 2, 'exp': '為新聞問問題 → reporter 記者。'},
    {'type': 'mc', 'q': 'My aunt doesn\'t work outside. She is a ______ and takes care of the family.', 'opts': ['housewife', 'secretary', 'shopkeeper', 'lawyer'], 'answer': 0, 'exp': '在家照顧家人 → housewife。'},
  ]},
]
