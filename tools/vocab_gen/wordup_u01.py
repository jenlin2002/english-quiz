# WORD UP 複習區 Unit 1（WORD UP「A-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 1, 'en': 'A-I', 'zh': 'A 開頭（一）',
  'intro': 'WORD UP「A-I」的 38 個字（A.M. 到 aim）。紅色＝在 WORD UP 還不熟或在這裡答錯的字，先複習紅色的字再做測驗。',
  'words': [
    W('A.M.', 'adv.', '上午', '= a.m.；下午是 P.M.', 'School starts at 8:00 A.M.', '學校早上八點開始上課。', '🌅'),
    W('ability', 'n.', '能力', 'able 的名詞', 'She has the ability to swim very fast.', '她有游得很快的能力。', '💪'),
    W('able', 'adj.', '能夠的', 'be able to + V', 'Are you able to come to my party?', '你能來我的派對嗎？', '🙆'),
    W('abroad', 'adv.', '在國外；到國外', 'go abroad（不加 to）', 'My cousin is studying abroad in Canada.', '我表哥在加拿大留學。', '✈️'),
    W('absent', 'adj.', '缺席的', 'be absent from 缺席…', 'Tom was absent from school because he was sick.', 'Tom 生病沒來上學。', '🪑'),
    W('accept', 'v.', '接受', '', 'Please accept this small gift.', '請收下這份小禮物。', '🎁'),
    W('accident', 'n.', '意外；事故', 'by accident 意外地', 'There was a car accident on the road.', '路上發生了車禍。', '🚑'),
    W('achieve', 'v.', '達成；實現', 'achieve a goal', 'Work hard and you will achieve your dream.', '努力就會實現夢想。', '🏆'),
    W('act', 'v./n.', '表演；行動', 'actor 演員', 'He acts in the school play.', '他在學校的話劇裡演出。', '🎭'),
    W('action', 'n.', '行動；動作', 'take action 採取行動', 'We need to take action now.', '我們現在就要採取行動。', '🏃'),
    W('active', 'adj.', '活躍的；積極的', '', 'My grandma is still very active.', '我奶奶還是很有活力。', '⚡'),
    W('activity', 'n.', '活動', '複數 activities', 'Swimming is my favorite summer activity.', '游泳是我最喜歡的夏日活動。', '🤸'),
    W('actor', 'n.', '男演員', '', 'The actor smiled at his fans.', '那位男演員對粉絲微笑。', '🎬'),
    W('actress', 'n.', '女演員', '', 'She wants to be an actress.', '她想當女演員。', '🎬'),
    W('actually', 'adv.', '實際上；其實', '', 'Actually, I don\'t like coffee.', '其實我不喜歡咖啡。', '💭'),
    W('add', 'v.', '加；增加', 'add A to B', 'Add some sugar to the tea.', '在茶裡加點糖。', '➕'),
    W('addition', 'n.', '加；增加', 'in addition 此外', 'We learned addition in math class.', '我們在數學課學加法。', '➕'),
    W('address', 'n.', '地址', 'email address 電子郵件地址', 'What is your home address?', '你家的地址是什麼？', '🏠'),
    W('admire', 'v.', '欣賞；佩服', '', 'I admire my teacher very much.', '我很佩服我的老師。', '👏'),
    W('admit', 'v.', '承認', 'admit – admitted', 'He admitted that he broke the window.', '他承認是他打破窗戶的。', '🙋'),
    W('adopt', 'v.', '領養；採用', '', 'We adopted a cat from the shelter.', '我們從收容所領養了一隻貓。', '🐈'),
    W('adult', 'n.', '成年人', '', 'This movie is for adults only.', '這部電影只限成人觀看。', '🧑'),
    W('advance', 'n./v.', '前進；進步', 'in advance 事先', 'Please buy the tickets in advance.', '請事先買票。', '⏩'),
    W('advantage', 'n.', '優點；好處', 'take advantage of 利用', 'Living near school is a big advantage.', '住在學校附近是一大好處。', '👍'),
    W('advertisement', 'n.', '廣告', '= ad', 'I saw an advertisement for a new phone.', '我看到一則新手機的廣告。', '📢'),
    W('advice', 'n.', '建議；勸告', '不可數；a piece of advice', 'Can you give me some advice?', '你可以給我一些建議嗎？', '💡'),
    W('advise', 'v.', '建議；勸告', 'advice 是名詞、advise 是動詞', 'The doctor advised me to rest.', '醫生建議我休息。', '🩺'),
    W('affair', 'n.', '事情；事務', '', 'This is my own affair.', '這是我自己的事。', '📂'),
    W('affect', 'v.', '影響', '', 'Too much screen time can affect your eyes.', '看太久螢幕會影響眼睛。', '👀'),
    W('afraid', 'adj.', '害怕的', 'be afraid of 害怕…', 'My sister is afraid of dogs.', '我妹妹怕狗。', '😨'),
    W('afternoon', 'n.', '下午', 'in the afternoon', 'We play basketball in the afternoon.', '我們下午打籃球。', '🌤️'),
    W('again', 'adv.', '再一次', '', 'Please say that again.', '請再說一次。', '🔁'),
    W('age', 'n.', '年齡', 'at the age of… 在…歲時', 'He started to play piano at the age of five.', '他五歲開始彈鋼琴。', '🎂'),
    W('ago', 'adv.', '在…以前', 'two days ago 兩天前', 'I saw him two days ago.', '我兩天前看到他。', '⏳'),
    W('agree', 'v.', '同意', 'agree with + 人', 'I agree with you.', '我同意你的看法。', '🤝'),
    W('aid', 'n./v.', '幫助；援助', 'first aid 急救', 'Every classroom has a first aid kit.', '每間教室都有急救箱。', '🩹'),
    W('AIDS', 'n.', '愛滋病', '一種疾病的縮寫', 'Doctors are still studying AIDS.', '醫生們仍在研究愛滋病。', '🎗️'),
    W('aim', 'n./v.', '目標；瞄準', '', 'My aim is to read ten books this year.', '我今年的目標是讀十本書。', '🎯'),
  ],
  'focus': [
    {'title': '容易搞混的字', 'head': ('字', '詞性', '例子'), 'rows': [
      ('advice / advise', '名詞 / 動詞', 'some advice（不可數）／ advise me to rest'),
      ('actor / actress', '男演員 / 女演員', 'a famous actor ／ a famous actress'),
      ('add / addition', '動詞 / 名詞', 'add sugar ／ in addition'),
      ('able / ability', '形容詞 / 名詞', 'be able to swim ／ the ability to swim'),
    ], 'note': ''},
    {'title': '常用片語', 'head': ('片語', '中文', ''), 'rows': [
      ('be able to + V', '能夠…', ''),
      ('be absent from', '缺席…', ''),
      ('be afraid of', '害怕…', ''),
      ('agree with + 人', '同意某人', ''),
      ('in advance', '事先', ''),
      ('go abroad', '出國（不加 to）', ''),
    ], 'note': ''},
  ],
}

# 課本題目（其他字由測驗程式自動補「看中文選英文」，每個字都會考到）
QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '能力', 'opts': ['able', 'ability', 'activity', 'action'], 'answer': 1, 'exp': 'ability 能力；able 是形容詞。'},
    {'type': 'mc', 'q': '在國外', 'opts': ['abroad', 'about', 'above', 'across'], 'answer': 0, 'exp': 'abroad 在國外。'},
    {'type': 'mc', 'q': '廣告', 'opts': ['advice', 'adult', 'advertisement', 'advantage'], 'answer': 2, 'exp': 'advertisement 廣告。'},
    {'type': 'mc', 'q': '領養', 'opts': ['admit', 'admire', 'accept', 'adopt'], 'answer': 3, 'exp': 'adopt 領養。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '意外；事故（a＿＿＿＿＿＿＿，8 個字母）：{0}', 'blanks': [['accident']], 'exp': 'accident。'},
    {'q': '害怕的（a＿＿＿＿＿，6 個字母）：{0}', 'blanks': [['afraid']], 'exp': 'afraid。'},
    {'q': '同意（a＿＿＿＿，5 個字母）：{0}', 'blanks': [['agree']], 'exp': 'agree。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Tom was {0} from school yesterday. （缺席的）', 'blanks': [['absent']], 'exp': 'be absent from 缺席。'},
    {'q': 'I saw him three days {0}. （以前）', 'blanks': [['ago']], 'exp': 'three days ago 三天前。'},
    {'q': 'My {0} is to get full marks on the test. （目標）', 'blanks': [['aim']], 'exp': 'aim 目標。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Can you give me some ______?', 'opts': ['advise', 'advice', 'advices', 'a advice'], 'answer': 1, 'exp': 'advice 是不可數名詞：some advice。'},
    {'type': 'mc', 'q': 'The doctor ______ me to drink more water.', 'opts': ['advised', 'advice', 'adviced', 'advices'], 'answer': 0, 'exp': 'advise 是動詞，過去式 advised。'},
    {'type': 'mc', 'q': 'My brother is afraid ______ the dark.', 'opts': ['to', 'with', 'of', 'at'], 'answer': 2, 'exp': 'be afraid of 害怕…'},
    {'type': 'mc', 'q': 'Are you able ______ the box?', 'opts': ['carry', 'to carry', 'carrying', 'carried'], 'answer': 1, 'exp': 'be able to + 原形動詞。'},
  ]},
]
