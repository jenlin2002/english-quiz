# WORD UP 複習區 Unit 2（WORD UP「A-II」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 2, 'en': 'A-II', 'zh': 'A 開頭（二）',
  'intro': 'WORD UP「A-II」的 38 個字（air 到 apologize）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('air', 'n.', '空氣', '不可數', 'The air in the mountains is fresh.', '山上的空氣很新鮮。', '🌬️'),
    W('aircraft', 'n.', '飛機；航空器', '單複數同形', 'The aircraft landed safely.', '那架飛機安全降落了。', '✈️'),
    W('airline', 'n.', '航空公司', '', 'Which airline are you flying with?', '你搭哪一家航空公司？', '🛫'),
    W('airplane', 'n.', '飛機', '= plane', 'We took an airplane to Japan.', '我們搭飛機去日本。', '✈️'),
    W('airport', 'n.', '機場', '', 'Dad picked us up at the airport.', '爸爸到機場接我們。', '🛬'),
    W('alarm', 'n.', '鬧鐘；警報', 'alarm clock 鬧鐘', 'My alarm rings at six every morning.', '我的鬧鐘每天早上六點響。', '⏰'),
    W('album', 'n.', '相簿；專輯', 'photo album 相簿', 'Grandma showed us her old photo album.', '奶奶給我們看她的舊相簿。', '📔'),
    W('alike', 'adj.', '相像的', '放在 be 動詞後面', 'The twins look alike.', '那對雙胞胎長得很像。', '👯'),
    W('alive', 'adj.', '活著的', '放在 be 動詞後面', 'The fish is still alive.', '那條魚還活著。', '🐟'),
    W('all', 'adj./pron.', '全部的；全部', 'all of us 我們全部', 'All the students are here.', '所有學生都到了。', '💯'),
    W('allow', 'v.', '允許', 'allow + 人 + to V', 'My parents allow me to play games on weekends.', '爸媽允許我週末玩遊戲。', '✅'),
    W('almost', 'adv.', '幾乎；差不多', '', 'It is almost ten o\'clock.', '快十點了。', '⏳'),
    W('alone', 'adj./adv.', '單獨的；獨自', '', 'Don\'t walk home alone at night.', '晚上不要一個人走路回家。', '🚶'),
    W('along', 'prep.', '沿著', 'walk along the river', 'We walked along the beach.', '我們沿著海灘散步。', '🏖️'),
    W('aloud', 'adv.', '大聲地；出聲地', 'read aloud 唸出來', 'Please read the story aloud.', '請把故事唸出來。', '📢'),
    W('alphabet', 'n.', '字母表', '', 'There are 26 letters in the English alphabet.', '英文字母有 26 個。', '🔤'),
    W('already', 'adv.', '已經', '', 'I have already finished my homework.', '我已經寫完功課了。', '✔️'),
    W('also', 'adv.', '也', '放在一般動詞前、be 動詞後', 'I like dogs. I also like cats.', '我喜歡狗，也喜歡貓。', '➕'),
    W('altogether', 'adv.', '總共；完全', '', 'There are thirty students altogether.', '總共有三十個學生。', '🧮'),
    W('always', 'adv.', '總是', '頻率最高', 'She always gets up early.', '她總是很早起床。', '🔁'),
    W('am', 'v.', '是（I 的 be 動詞）', 'I am', 'I am a junior high school student.', '我是國中生。', '🙋'),
    W('ambulance', 'n.', '救護車', '', 'Call an ambulance! Someone is hurt.', '快叫救護車！有人受傷了。', '🚑'),
    W('America', 'n.', '美國；美洲', '', 'My uncle lives in America.', '我叔叔住在美國。', '🇺🇸'),
    W('American', 'adj./n.', '美國的；美國人', '', 'Our new teacher is American.', '我們的新老師是美國人。', '🗽'),
    W('amount', 'n.', '數量；金額', 'a large amount of + 不可數名詞', 'Drink a large amount of water every day.', '每天要喝大量的水。', '💧'),
    W('ancient', 'adj.', '古代的；古老的', '', 'We visited an ancient temple.', '我們參觀了一座古老的廟。', '🏛️'),
    W('angel', 'n.', '天使', '', 'The little girl sings like an angel.', '那個小女孩唱歌像天使一樣。', '👼'),
    W('anger', 'n.', '憤怒', 'angry 的名詞', 'He could not hide his anger.', '他藏不住怒氣。', '💢'),
    W('angry', 'adj.', '生氣的', 'be angry with + 人', 'Mom is angry with me.', '媽媽在生我的氣。', '😠'),
    W('animal', 'n.', '動物', '', 'The panda is my favorite animal.', '貓熊是我最喜歡的動物。', '🐼'),
    W('ankle', 'n.', '腳踝', '', 'I hurt my ankle in PE class.', '我在體育課扭傷腳踝。', '🦶'),
    W('another', 'adj./pron.', '另一個；再一個', '後面接單數名詞', 'Can I have another cookie?', '我可以再吃一塊餅乾嗎？', '🍪'),
    W('answer', 'n./v.', '答案；回答', '', 'Do you know the answer?', '你知道答案嗎？', '✅'),
    W('ant', 'n.', '螞蟻', '', 'An ant is very small but strong.', '螞蟻很小但很有力氣。', '🐜'),
    W('any', 'adj./pron.', '任何；一些', '用在否定句和問句', 'Do you have any questions?', '你有任何問題嗎？', '❓'),
    W('anyway', 'adv.', '無論如何；反正', '', 'It was raining, but we went out anyway.', '雖然在下雨，我們還是出門了。', '🤷'),
    W('apartment', 'n.', '公寓', '', 'We live in an apartment on the fifth floor.', '我們住在五樓的公寓。', '🏢'),
    W('apologize', 'v.', '道歉', 'apologize to + 人 + for + 事', 'He apologized to me for being late.', '他因為遲到向我道歉。', '🙇'),
  ],
  'focus': [
    {'title': '容易搞混的字', 'head': ('字', '用法', '例子'), 'rows': [
      ('alone / lonely', '獨自（事實）／寂寞（感覺）', 'live alone ／ feel lonely'),
      ('alike / like', '相像的（放句尾）／像（後面接名詞）', 'They look alike. ／ He looks like his dad.'),
      ('aloud / loud', '出聲地 ／ 大聲的', 'read aloud ／ loud music'),
      ('anger / angry', '名詞 ／ 形容詞', 'show his anger ／ be angry'),
      ('already / all ready', '已經 ／ 全都準備好', 'I have already eaten. ／ We are all ready.'),
    ], 'note': ''},
    {'title': '頻率副詞與片語', 'head': ('說法', '中文', ''), 'rows': [
      ('always', '總是（100%）', ''),
      ('almost', '幾乎', ''),
      ('allow + 人 + to V', '允許某人做…', ''),
      ('apologize to + 人 + for + 事', '為某事向某人道歉', ''),
      ('be angry with + 人', '生某人的氣', ''),
    ], 'note': 'always 這類頻率副詞放在一般動詞前、be 動詞後。'},
  ],
}

# 課本題目（其他字由測驗程式自動補「看中文選英文」，每個字都會考到）
QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '救護車', 'opts': ['airplane', 'ambulance', 'apartment', 'airport'], 'answer': 1, 'exp': 'ambulance 救護車。'},
    {'type': 'mc', 'q': '道歉', 'opts': ['allow', 'answer', 'apologize', 'agree'], 'answer': 2, 'exp': 'apologize 道歉。'},
    {'type': 'mc', 'q': '古代的', 'opts': ['ancient', 'angel', 'another', 'American'], 'answer': 0, 'exp': 'ancient 古代的。'},
    {'type': 'mc', 'q': '字母表', 'opts': ['album', 'alarm', 'amount', 'alphabet'], 'answer': 3, 'exp': 'alphabet 字母表。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '機場（a＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['airport']], 'exp': 'airport。'},
    {'q': '腳踝（a＿＿＿＿，5 個字母）：{0}', 'blanks': [['ankle']], 'exp': 'ankle。'},
    {'q': '已經（a＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['already']], 'exp': 'already。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The twins look {0}. （相像的）', 'blanks': [['alike']], 'exp': 'look alike 看起來很像。'},
    {'q': 'Please read the poem {0}. （出聲地）', 'blanks': [['aloud']], 'exp': 'read aloud 唸出來。'},
    {'q': 'The old cat is still {0}. （活著的）', 'blanks': [['alive']], 'exp': 'alive 活著的。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'My parents don\'t allow me ______ out late.', 'opts': ['stay', 'to stay', 'staying', 'stayed'], 'answer': 1, 'exp': 'allow + 人 + to V。'},
    {'type': 'mc', 'q': 'He apologized ______ me for breaking my pen.', 'opts': ['to', 'with', 'at', 'of'], 'answer': 0, 'exp': 'apologize to + 人。'},
    {'type': 'mc', 'q': 'Can I have ______ glass of water?', 'opts': ['other', 'others', 'another', 'any'], 'answer': 2, 'exp': 'another + 單數名詞：再一杯。'},
    {'type': 'mc', 'q': 'Do you have ______ brothers or sisters?', 'opts': ['some', 'any', 'all', 'another'], 'answer': 1, 'exp': '問句用 any。'},
  ]},
]
