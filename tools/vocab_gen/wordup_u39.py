# WORD UP 複習區 Unit 39（WORD UP「R-I」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 39, 'en': 'R-I', 'zh': 'R 開頭（一）',
  'intro': 'WORD UP「R-I」的 32 個字（record 到 revise）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('record', 'n./v.', '紀錄；唱片；錄音', 'break the record 破紀錄', 'She broke the world record.', '她打破了世界紀錄。', '🏅'),
    W('recover', 'v.', '康復；恢復', 'recover from 從…康復', 'I hope you recover soon.', '希望你早日康復。', '💪'),
    W('rectangle', 'n.', '長方形', '', 'A door is a rectangle.', '門是長方形的。', '▭'),
    W('recycle', 'v.', '回收', '', 'We should recycle bottles and cans.', '我們應該回收瓶罐。', '♻️'),
    W('red', 'adj./n.', '紅色的', '', 'Stop at the red light.', '紅燈要停。', '🔴'),
    W('refrigerator', 'n.', '冰箱', '= fridge', 'Put the milk in the refrigerator.', '把牛奶放進冰箱。', '🧊'),
    W('refuse', 'v.', '拒絕', 'refuse to V', 'He refused to help me.', '他拒絕幫我。', '🙅'),
    W('regard', 'v.', '把…看作', 'regard A as B', 'I regard him as my brother.', '我把他當作我的兄弟。', '👀'),
    W('region', 'n.', '地區', '', 'This region is famous for tea.', '這個地區以茶聞名。', '🗺️'),
    W('regret', 'v./n.', '後悔', '過去式 regretted', 'I regret saying that.', '我後悔說了那些話。', '😔'),
    W('regular', 'adj.', '規律的；一般的', 'regularly 規律地', 'Regular exercise is good for you.', '規律運動對你有益。', '🔁'),
    W('reject', 'v.', '拒絕；駁回', '', 'They rejected my idea.', '他們否決了我的點子。', '❌'),
    W('relative', 'n.', '親戚', '', 'We visit our relatives during Chinese New Year.', '過年時我們去拜訪親戚。', '👨‍👩‍👧'),
    W('remember', 'v.', '記得', 'remember to V 記得要做', 'Remember to lock the door.', '記得要鎖門。', '🧠'),
    W('remind', 'v.', '提醒', 'remind + 人 + to V／of', 'Remind me to call Mom.', '提醒我打電話給媽媽。', '⏰'),
    W('rent', 'v./n.', '租；租金', '', 'We rented a car in Hualien.', '我們在花蓮租了一輛車。', '🔑'),
    W('repair', 'v.', '修理', '= fix', 'The man is repairing the roof.', '那個人正在修屋頂。', '🛠️'),
    W('repeat', 'v.', '重複', '', 'Please repeat after me.', '請跟我唸。', '🔂'),
    W('reply', 'v./n.', '回覆', 'reply to + 人／信', 'Please reply to my email.', '請回覆我的電子郵件。', '↩️'),
    W('report', 'n./v.', '報告；報導', '', 'I have to write a book report.', '我得寫一篇讀書報告。', '📑'),
    W('reporter', 'n.', '記者', '', 'The reporter interviewed the mayor.', '記者訪問了市長。', '🎙️'),
    W('Republic of China', 'n.', '中華民國', 'R.O.C.', 'Taiwan is called the Republic of China.', '台灣的國號是中華民國。', '🇹🇼'),
    W('require', 'v.', '需要；要求', '', 'This job requires good English.', '這份工作需要好的英文能力。', '📋'),
    W('respect', 'v./n.', '尊敬', '', 'We should respect our teachers.', '我們應該尊敬老師。', '🙇'),
    W('responsible', 'adj.', '負責的', 'be responsible for', 'Who is responsible for this?', '誰要為這件事負責？', '🧑‍✈️'),
    W('rest', 'n./v.', '休息；其餘', 'take a rest 休息', 'Let\'s take a rest.', '我們休息一下吧。', '😌'),
    W('restaurant', 'n.', '餐廳', '', 'We ate at a Japanese restaurant.', '我們在日本料理餐廳吃飯。', '🍽️'),
    W('restroom', 'n.', '洗手間', '', 'Where is the restroom?', '洗手間在哪裡？', '🚻'),
    W('result', 'n.', '結果', 'as a result 結果', 'What was the result of the game?', '比賽結果如何？', '📊'),
    W('return', 'v./n.', '回來；歸還', 'return + 東西 + to', 'Please return the book to the library.', '請把書還給圖書館。', '🔙'),
    W('review', 'v./n.', '複習；評論', '', 'I review my notes before a test.', '我考試前會複習筆記。', '📖'),
    W('revise', 'v.', '修改；修訂', '', 'Please revise your essay.', '請修改你的作文。', '✏️'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('remember / remind', '記得 ／ 提醒', 'remember to go ／ remind me to go'),
      ('remember to V / V-ing', '記得要做 ／ 記得做過', 'remember to call ／ remember calling'),
      ('refuse to V', '拒絕做…', 'refuse to eat'),
      ('regard A as B', '把 A 視為 B', 'regard her as a friend'),
      ('be responsible for', '對…負責', 'responsible for the class'),
      ('recover from', '從…中康復', 'recover from a cold'),
      ('return A to B', '把 A 還給 B', 'return the pen to Amy'),
    ], 'note': 'return 本身就有「回來」的意思，不說 return back。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '親戚', 'opts': ['region', 'relative', 'reporter', 'record'], 'answer': 1, 'exp': 'relative 親戚。'},
    {'type': 'mc', 'q': '後悔', 'opts': ['regret', 'reject', 'regard', 'require'], 'answer': 0, 'exp': 'regret 後悔。'},
    {'type': 'mc', 'q': '長方形', 'opts': ['refrigerator', 'restroom', 'rectangle', 'restaurant'], 'answer': 2, 'exp': 'rectangle 長方形。'},
    {'type': 'mc', 'q': '修改', 'opts': ['review', 'repeat', 'reply', 'revise'], 'answer': 3, 'exp': 'revise 修改。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '餐廳（r＿＿＿＿＿＿＿＿＿，10 個字母）：{0}', 'blanks': [['restaurant']], 'exp': 'restaurant。'},
    {'q': '回收（r＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['recycle']], 'exp': 'recycle。'},
    {'q': '尊敬（r＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['respect']], 'exp': 'respect。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please {0} me to bring my umbrella. （提醒）', 'blanks': [['remind']], 'exp': 'remind + 人 + to V。'},
    {'q': 'Class leaders are {0} for closing the windows. （負責的）', 'blanks': [['responsible']], 'exp': 'be responsible for。'},
    {'q': 'He {0} to answer my question. （拒絕，過去式）', 'blanks': [['refused']], 'exp': 'refuse 的過去式 refused。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': 'Remember ______ the lights before you leave.', 'opts': ['turn off', 'to turn off', 'turned off', 'turns off'], 'answer': 1, 'exp': 'remember to V 記得要做。'},
    {'type': 'mc', 'q': 'I need to ______ these books to the library.', 'opts': ['rest', 'rent', 'return', 'report'], 'answer': 2, 'exp': 'return A to B 歸還。'},
    {'type': 'mc', 'q': 'Grandpa is recovering ______ his operation.', 'opts': ['from', 'of', 'with', 'at'], 'answer': 0, 'exp': 'recover from 從…康復。'},
    {'type': 'mc', 'q': 'Everyone regards Tom ______ a good leader.', 'opts': ['to', 'for', 'like', 'as'], 'answer': 3, 'exp': 'regard A as B。'},
  ]},
]
