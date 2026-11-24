# WORD UP 複習區 Unit 38（WORD UP「Q+R-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 38, 'en': 'Q+R-I', 'zh': 'Q、R 開頭（一）',
  'intro': 'WORD UP「Q+R-I」的 32 個字（quality 到 recently）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('quality', 'n.', '品質', '', 'This bag is of high quality.', '這個包包品質很好。', '⭐'),
    W('quarter', 'n.', '四分之一；一刻鐘', 'a quarter past six 六點十五分', 'It\'s a quarter past six.', '現在六點十五分。', '🕡'),
    W('queen', 'n.', '女王；皇后', '', 'The queen wore a crown.', '女王戴著皇冠。', '👑'),
    W('question', 'n.', '問題', 'ask a question 問問題', 'May I ask a question?', '我可以問一個問題嗎？', '❓'),
    W('quick', 'adj.', '快的', 'quickly 快速地', 'Let\'s have a quick lunch.', '我們快速吃個午餐吧。', '⚡'),
    W('quiet', 'adj.', '安靜的', 'quite 相當（拼法不同）', 'Please be quiet in the library.', '在圖書館請保持安靜。', '🤫'),
    W('quit', 'v.', '放棄；戒掉；辭職', '三態都是 quit；quit + V-ing', 'Dad quit smoking last year.', '爸爸去年戒菸了。', '🛑'),
    W('quite', 'adv.', '相當；十分', '', 'The test was quite easy.', '這次考試相當簡單。', '👌'),
    W('quiz', 'n.', '小考', '複數 quizzes', 'We have an English quiz today.', '我們今天有英文小考。', '📝'),
    W('rabbit', 'n.', '兔子', '', 'The rabbit is eating a carrot.', '兔子在吃紅蘿蔔。', '🐰'),
    W('race', 'n./v.', '賽跑；比賽；種族', '', 'Who won the race?', '誰贏了賽跑？', '🏁'),
    W('radio', 'n.', '收音機；廣播', 'on the radio 在廣播中', 'I heard the song on the radio.', '我在廣播裡聽到這首歌。', '📻'),
    W('railroad', 'n.', '鐵路', '= railway', 'The railroad goes around the island.', '鐵路環繞全島。', '🛤️'),
    W('rain', 'n./v.', '雨；下雨', '', 'It is raining heavily.', '正在下大雨。', '🌧️'),
    W('rainbow', 'n.', '彩虹', '', 'Look! There is a rainbow.', '看！有彩虹。', '🌈'),
    W('rainy', 'adj.', '下雨的', 'rainy season 雨季', 'It\'s a rainy day.', '今天是下雨天。', '☔'),
    W('raise', 'v.', '舉起；養育；募集', 'raise your hand 舉手', 'Raise your hand if you know the answer.', '知道答案的人請舉手。', '🙋'),
    W('range', 'n.', '範圍；山脈', '', 'The price range is 100 to 300 dollars.', '價格範圍在 100 到 300 元。', '📏'),
    W('rapid', 'adj.', '快速的', '= fast', 'The city grew at a rapid speed.', '這個城市快速發展。', '🚀'),
    W('rare', 'adj.', '稀有的；罕見的', 'rarely 很少', 'This bird is very rare.', '這種鳥非常稀有。', '💎'),
    W('rat', 'n.', '老鼠（較大的）', 'mouse 小老鼠', 'A rat ran into the hole.', '一隻老鼠跑進洞裡。', '🐀'),
    W('rather', 'adv.', '相當；寧願', 'would rather + 原形 寧願', 'I would rather stay home.', '我寧願待在家。', '🤷'),
    W('reach', 'v.', '到達；伸手拿', '', 'We reached the top of the mountain.', '我們到達了山頂。', '🏔️'),
    W('read', 'v.', '讀', '三態 read-read-read（過去式唸 /rɛd/）', 'I read a book last night.', '我昨晚讀了一本書。', '📖'),
    W('ready', 'adj.', '準備好的', 'be ready for／to V', 'Are you ready for the test?', '你準備好考試了嗎？', '✅'),
    W('real', 'adj.', '真的；真實的', '', 'Is this a real diamond?', '這是真的鑽石嗎？', '💯'),
    W('realize', 'v.', '了解；意識到；實現', '', 'I didn\'t realize it was so late.', '我沒意識到已經這麼晚了。', '💡'),
    W('really', 'adv.', '真正地；非常', '', 'I really like this song.', '我真的很喜歡這首歌。', '❗'),
    W('reason', 'n.', '理由；原因', 'the reason for', 'What is the reason for being late?', '遲到的原因是什麼？', '🤔'),
    W('receive', 'v.', '收到', '', 'I received a letter from my friend.', '我收到朋友寄來的信。', '📩'),
    W('recent', 'adj.', '最近的', '', 'This is a recent photo of me.', '這是我最近的照片。', '🆕'),
    W('recently', 'adv.', '最近', '', 'Have you seen any good movies recently?', '你最近有看什麼好電影嗎？', '🗓️'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('quiet / quite', '安靜的 ／ 相當', 'Be quiet. ／ quite good'),
      ('quit + V-ing', '戒掉、停止做…', 'quit eating junk food'),
      ('would rather + 原形', '寧願…', 'I\'d rather walk.'),
      ('a quarter past / to', '幾點十五分 ／ 差十五分幾點', 'a quarter to eight 七點四十五'),
      ('raise your hand', '舉手', 'Raise your hand to ask.'),
      ('be ready for / to V', '準備好…', 'ready for school'),
      ('recent / recently', '最近的 ／ 最近', 'recent news ／ I\'ve been busy recently.'),
    ], 'note': 'read 的過去式拼法不變，但唸 /rɛd/；quiz 的複數 quizzes。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '品質', 'opts': ['quantity', 'quality', 'quarter', 'question'], 'answer': 1, 'exp': 'quality 品質。'},
    {'type': 'mc', 'q': '稀有的', 'opts': ['rare', 'rapid', 'rather', 'real'], 'answer': 0, 'exp': 'rare 稀有的。'},
    {'type': 'mc', 'q': '收到', 'opts': ['reach', 'realize', 'receive', 'raise'], 'answer': 2, 'exp': 'receive 收到。'},
    {'type': 'mc', 'q': '鐵路', 'opts': ['radio', 'rainbow', 'range', 'railroad'], 'answer': 3, 'exp': 'railroad 鐵路。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '彩虹（r＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['rainbow']], 'exp': 'rainbow。'},
    {'q': '理由（r＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['reason']], 'exp': 'reason。'},
    {'q': '安靜的（q＿＿＿＿，5 個字母）：{0}', 'blanks': [['quiet']], 'exp': 'quiet。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please {0} your hand before you speak. （舉起）', 'blanks': [['raise']], 'exp': 'raise your hand 舉手。'},
    {'q': 'I would {0} stay home than go out in the rain. （寧願）', 'blanks': [['rather']], 'exp': 'would rather 寧願。'},
    {'q': 'Are you {0} for the trip? （準備好的）', 'blanks': [['ready']], 'exp': 'be ready for 準備好…。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'My uncle quit ______ two years ago.', 'opts': ['smoke', 'smoking', 'to smoke', 'smoked'], 'answer': 1, 'exp': 'quit + V-ing。'},
    {'type': 'mc', 'q': 'The movie was ______ good. I enjoyed it.', 'opts': ['quiet', 'quick', 'quite', 'quit'], 'answer': 2, 'exp': 'quite good 相當好。'},
    {'type': 'mc', 'q': 'It\'s 7:45. It\'s a quarter ______ eight.', 'opts': ['to', 'past', 'after', 'of'], 'answer': 0, 'exp': 'a quarter to eight 差十五分八點。'},
    {'type': 'mc', 'q': 'Have you heard from Amy ______ ?', 'opts': ['recent', 'rapid', 'rare', 'recently'], 'answer': 3, 'exp': '副詞 recently 最近。'},
  ]},
]
