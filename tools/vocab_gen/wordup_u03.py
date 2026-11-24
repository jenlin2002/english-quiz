# WORD UP 複習區 Unit 3（WORD UP「A-III」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 3, 'en': 'A-III', 'zh': 'A 開頭（三）',
  'intro': 'WORD UP「A-III」的 38 個字（appear 到 away）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('appear', 'v.', '出現；看起來', 'disappear 消失', 'A rainbow appeared after the rain.', '雨後出現了一道彩虹。', '🌈'),
    W('appearance', 'n.', '外表；出現', 'appear 的名詞', 'Don\'t judge people by their appearance.', '不要以貌取人。', '🪞'),
    W('apple', 'n.', '蘋果', 'an apple', 'I eat an apple every morning.', '我每天早上吃一顆蘋果。', '🍎'),
    W('apply', 'v.', '申請；應用', 'apply for + 職位／學校', 'My sister applied for a job at the bank.', '我姊姊應徵了銀行的工作。', '📝'),
    W('appreciate', 'v.', '感激；欣賞', 'I appreciate it. 我很感激', 'I really appreciate your help.', '我真的很感謝你的幫忙。', '🙏'),
    W('April', 'n.', '四月', '月份第一個字母大寫', 'My birthday is in April.', '我的生日在四月。', '🌸'),
    W('are', 'v.', '是（you／we／they 的 be 動詞）', 'you are / we are / they are', 'They are my classmates.', '他們是我的同學。', '👥'),
    W('area', 'n.', '地區；面積', '', 'There are many parks in this area.', '這個地區有很多公園。', '🗺️'),
    W('argue', 'v.', '爭吵；爭論', 'argue with + 人', 'The brothers often argue about small things.', '那對兄弟常為小事吵架。', '🗣️'),
    W('arm', 'n.', '手臂', 'arms 也有「武器」的意思', 'He broke his arm playing basketball.', '他打籃球摔斷了手臂。', '💪'),
    W('armchair', 'n.', '扶手椅', '', 'Grandpa is reading in the armchair.', '爺爺坐在扶手椅上看書。', '🛋️'),
    W('army', 'n.', '軍隊；陸軍', '', 'My uncle served in the army.', '我叔叔當過兵。', '🪖'),
    W('around', 'prep./adv.', '在…周圍；大約', 'around + 時間／數字＝大約', 'We sat around the table.', '我們圍著桌子坐。', '🔄'),
    W('arrange', 'v.', '安排；整理', '', 'Mom arranged the flowers in a vase.', '媽媽把花插進花瓶裡。', '💐'),
    W('arrest', 'v./n.', '逮捕', '', 'The police arrested the thief.', '警察逮捕了那個小偷。', '🚓'),
    W('arrive', 'v.', '到達', 'arrive at + 小地點／arrive in + 大地點', 'We arrived in Tainan at noon.', '我們中午到達台南。', '🏁'),
    W('art', 'n.', '藝術；美術', 'art class 美術課', 'Art is my favorite subject.', '美術是我最喜歡的科目。', '🎨'),
    W('article', 'n.', '文章；冠詞', 'a／an／the 是冠詞', 'I read an article about whales.', '我讀了一篇關於鯨魚的文章。', '📰'),
    W('artist', 'n.', '藝術家；畫家', '', 'The artist painted a picture of the sea.', '那位畫家畫了一幅海的畫。', '👩‍🎨'),
    W('Asia', 'n.', '亞洲', '', 'Taiwan is in Asia.', '台灣在亞洲。', '🌏'),
    W('Asian', 'adj./n.', '亞洲的；亞洲人', '', 'Rice is an important Asian food.', '米飯是很重要的亞洲食物。', '🍚'),
    W('ask', 'v.', '問；要求', 'ask + 人 + to V 要求某人做…', 'May I ask you a question?', '我可以問你一個問題嗎？', '🙋'),
    W('asleep', 'adj.', '睡著的', 'fall asleep 睡著；放在 be 動詞後面', 'The baby is asleep.', '寶寶睡著了。', '😴'),
    W('assistant', 'n.', '助理', '', 'The doctor\'s assistant called my name.', '醫生的助理叫了我的名字。', '🧑‍💼'),
    W('assume', 'v.', '以為；假定', '', 'I assumed you were at home.', '我以為你在家。', '🤔'),
    W('attack', 'v./n.', '攻擊', '', 'The dog attacked the cat.', '那隻狗攻擊了貓。', '⚔️'),
    W('attend', 'v.', '參加；出席', 'attend + 活動（不加 to）', 'All students must attend the meeting.', '所有學生都必須參加這個會議。', '🏫'),
    W('attention', 'n.', '注意', 'pay attention to + 名詞', 'Please pay attention to the teacher.', '請注意聽老師說。', '👀'),
    W('audience', 'n.', '觀眾；聽眾', '指一整群人', 'The audience clapped loudly.', '觀眾大聲鼓掌。', '👏'),
    W('August', 'n.', '八月', '', 'Summer vacation ends in August.', '暑假在八月結束。', '☀️'),
    W('aunt', 'n.', '阿姨；姑姑；嬸嬸', 'uncle 叔叔、舅舅', 'My aunt lives in Kaohsiung.', '我阿姨住在高雄。', '👩'),
    W('Australia', 'n.', '澳洲', '', 'Kangaroos live in Australia.', '袋鼠住在澳洲。', '🇦🇺'),
    W('Australian', 'adj./n.', '澳洲的；澳洲人', '', 'Our English teacher is Australian.', '我們的英文老師是澳洲人。', '🦘'),
    W('autumn', 'n.', '秋天', '= fall（美式）', 'Leaves turn red in autumn.', '秋天葉子會變紅。', '🍂'),
    W('available', 'adj.', '可用的；有空的', '', 'Is this seat available?', '這個位子有人坐嗎？', '🪑'),
    W('avoid', 'v.', '避免', 'avoid + V-ing', 'Try to avoid eating too much sugar.', '盡量避免吃太多糖。', '🚫'),
    W('aware', 'adj.', '知道的；察覺的', 'be aware of + 名詞', 'Are you aware of the danger?', '你知道這有危險嗎？', '💡'),
    W('away', 'adv.', '離開；遠離', 'go away 走開／far away 很遠', 'The bird flew away.', '那隻鳥飛走了。', '🕊️'),
  ],
  'focus': [
    {'title': '常考片語', 'head': ('說法', '中文', '例子'), 'rows': [
      ('arrive in / arrive at', '到達（大地點／小地點）', 'arrive in Taipei ／ arrive at the station'),
      ('pay attention to', '注意', 'pay attention to the teacher'),
      ('apply for', '申請、應徵', 'apply for a job'),
      ('be aware of', '知道、察覺', 'be aware of the problem'),
      ('avoid + V-ing', '避免做…', 'avoid eating junk food'),
      ('argue with + 人', '和某人吵架', 'argue with my brother'),
    ], 'note': 'attend 後面直接接活動：attend the meeting（不說 attend to the meeting）。'},
    {'title': '一家人的字', 'head': ('字', '用法', '例子'), 'rows': [
      ('appear / appearance', '動詞 ／ 名詞', 'appear on TV ／ his appearance'),
      ('art / artist', '藝術 ／ 藝術家', 'art class ／ a famous artist'),
      ('Asia / Asian', '亞洲 ／ 亞洲的、亞洲人', 'in Asia ／ Asian food'),
      ('Australia / Australian', '澳洲 ／ 澳洲的、澳洲人', 'in Australia ／ an Australian'),
      ('asleep / sleep', '睡著的（形容詞）／ 睡覺（動詞）', 'He is asleep. ／ He sleeps late.'),
    ], 'note': ''},
  ],
}

# 課本題目（其他字由測驗程式自動補「看中文選英文」，每個字都會考到）
QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '觀眾', 'opts': ['attention', 'audience', 'assistant', 'artist'], 'answer': 1, 'exp': 'audience 觀眾。'},
    {'type': 'mc', 'q': '感激；欣賞', 'opts': ['appreciate', 'appear', 'apply', 'arrange'], 'answer': 0, 'exp': 'appreciate 感激。'},
    {'type': 'mc', 'q': '秋天', 'opts': ['August', 'April', 'autumn', 'Asia'], 'answer': 2, 'exp': 'autumn 秋天。'},
    {'type': 'mc', 'q': '逮捕', 'opts': ['attack', 'argue', 'assume', 'arrest'], 'answer': 3, 'exp': 'arrest 逮捕。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '到達（a＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['arrive']], 'exp': 'arrive。'},
    {'q': '避免（a＿＿＿＿，5 個字母）：{0}', 'blanks': [['avoid']], 'exp': 'avoid。'},
    {'q': '文章（a＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['article']], 'exp': 'article。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'The baby fell {0} in my arms. （睡著的）', 'blanks': [['asleep']], 'exp': 'fall asleep 睡著。'},
    {'q': 'Please pay {0} to the traffic lights. （注意）', 'blanks': [['attention']], 'exp': 'pay attention to 注意。'},
    {'q': 'Is the manager {0} this afternoon? （有空的）', 'blanks': [['available']], 'exp': 'available 有空的。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'We arrived ______ Japan last night.', 'opts': ['at', 'in', 'to', 'on'], 'answer': 1, 'exp': '大地點（國家、城市）用 arrive in。'},
    {'type': 'mc', 'q': 'You should avoid ______ in the sun too long.', 'opts': ['stay', 'to stay', 'staying', 'stayed'], 'answer': 2, 'exp': 'avoid + V-ing。'},
    {'type': 'mc', 'q': 'Tom will ______ the English contest next week.', 'opts': ['attend', 'attend to', 'arrive', 'apply'], 'answer': 0, 'exp': 'attend + 活動：參加比賽。'},
    {'type': 'mc', 'q': 'My brother applied ______ a summer job.', 'opts': ['to', 'with', 'for', 'of'], 'answer': 2, 'exp': 'apply for 應徵、申請。'},
  ]},
]
