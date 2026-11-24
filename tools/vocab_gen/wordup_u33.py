# WORD UP 複習區 Unit 33（WORD UP「O」的字）：只用 WORD UP 的英文字表；中文、例句、題目為本站自編
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'wordup', 'no': 33, 'en': 'O', 'zh': 'O 開頭',
  'intro': 'WORD UP「O」的 37 個字（o\'clock 到 ox）。紅色＝要複習，藍色標籤＝WORD UP 標熟記、還要在這裡考對。',
  'words': [
    W('o\'clock', 'adv.', '…點鐘', '整點才用', 'It\'s seven o\'clock.', '現在七點整。', '🕖'),
    W('obey', 'v.', '服從；遵守', 'obey the rules', 'We should obey the traffic rules.', '我們應該遵守交通規則。', '🚦'),
    W('object', 'n./v.', '物體；反對', 'object to + V-ing 反對', 'What is that object on the table?', '桌上那個東西是什麼？', '📦'),
    W('occur', 'v.', '發生', '= happen；過去式 occurred', 'The accident occurred last night.', '那場意外發生在昨晚。', '❗'),
    W('ocean', 'n.', '海洋', 'the Pacific Ocean 太平洋', 'Whales live in the ocean.', '鯨魚住在海洋裡。', '🌊'),
    W('October', 'n.', '十月', '', 'Halloween is in October.', '萬聖節在十月。', '🎃'),
    W('off', 'adv./prep.', '離開；關掉', 'turn off 關掉；take off 脫掉、起飛', 'Turn off the TV.', '把電視關掉。', '📴'),
    W('offer', 'v./n.', '提供；提議', 'offer + 人 + 東西', 'He offered me a seat.', '他讓座給我。', '🤲'),
    W('office', 'n.', '辦公室', '', 'Dad works in an office.', '爸爸在辦公室上班。', '🏢'),
    W('officer', 'n.', '官員；警官', 'police officer 警察', 'The police officer helped the old lady.', '警察幫助那位老太太。', '👮'),
    W('official', 'adj./n.', '官方的；官員', '', 'English is an official language in Singapore.', '英文是新加坡的官方語言之一。', '📜'),
    W('often', 'adv.', '常常', 't 常不發音', 'I often go swimming in summer.', '我夏天常去游泳。', '🔁'),
    W('oil', 'n.', '油', '不可數', 'Don\'t use too much oil.', '不要用太多油。', '🛢️'),
    W('old', 'adj.', '老的；舊的；…歲', 'How old are you?', 'How old is your brother?', '你哥哥幾歲？', '👴'),
    W('omit', 'v.', '省略；遺漏', '過去式 omitted', 'Don\'t omit any words.', '不要漏掉任何字。', '✂️'),
    W('once', 'adv.', '一次；曾經', 'once a week 一週一次', 'I go to the library once a week.', '我一週去圖書館一次。', '1️⃣'),
    W('one', 'n./pron.', '一；一個', '', 'I have one sister.', '我有一個姊姊。', '☝️'),
    W('onion', 'n.', '洋蔥', '', 'Cutting onions makes me cry.', '切洋蔥讓我流淚。', '🧅'),
    W('only', 'adj./adv.', '唯一的；只', '', 'He is the only child in his family.', '他是家裡的獨生子。', '🎯'),
    W('open', 'v./adj.', '打開；開著的', '', 'The store is open until ten.', '那家店營業到十點。', '🔓'),
    W('operate', 'v.', '操作；動手術', '', 'Can you operate this machine?', '你會操作這台機器嗎？', '⚙️'),
    W('operation', 'n.', '手術；操作', '', 'Grandpa had an operation on his heart.', '爺爺動了心臟手術。', '🏥'),
    W('opinion', 'n.', '意見；看法', 'in my opinion 依我看', 'In my opinion, the movie is boring.', '依我看，這部電影很無聊。', '💭'),
    W('opportunity', 'n.', '機會', '= chance', 'This is a great opportunity.', '這是個大好機會。', '🚪'),
    W('orange', 'n./adj.', '柳橙；橘色的', 'an orange', 'I\'d like a glass of orange juice.', '我要一杯柳橙汁。', '🍊'),
    W('order', 'n./v.', '順序；命令；點餐', 'in order 依序；May I take your order?', 'May I take your order?', '請問要點什麼？', '🧾'),
    W('ordinary', 'adj.', '普通的', '', 'It was just an ordinary day.', '那只是普通的一天。', '😐'),
    W('organization', 'n.', '組織；機構', '', 'She works for an international organization.', '她在一個國際組織工作。', '🏛️'),
    W('organize', 'v.', '組織；整理', '', 'Let\'s organize a party for Mom.', '我們幫媽媽辦個派對吧。', '🗂️'),
    W('out', 'adv.', '出去；在外', 'go out 出去', 'Let\'s go out for dinner.', '我們出去吃晚餐吧。', '🚶'),
    W('outside', 'adv./prep.', '在外面', 'inside 在裡面', 'The kids are playing outside.', '孩子們在外面玩。', '🌳'),
    W('oven', 'n.', '烤箱', '', 'Put the cake in the oven.', '把蛋糕放進烤箱。', '♨️'),
    W('overpass', 'n.', '天橋；高架橋', 'underpass 地下道', 'Use the overpass to cross the road.', '走天橋過馬路。', '🌉'),
    W('overseas', 'adj./adv.', '海外的；在國外', '= abroad', 'My cousin is studying overseas.', '我表哥在國外留學。', '✈️'),
    W('own', 'adj./v.', '自己的；擁有', 'on one\'s own 獨自', 'I have my own room.', '我有自己的房間。', '🏡'),
    W('owner', 'n.', '主人；擁有者', '', 'Who is the owner of this bike?', '這台腳踏車是誰的？', '🔑'),
    W('ox', 'n.', '公牛；牛', '複數 oxen', 'The ox is pulling a cart.', '那頭牛在拉車。', '🐂'),
  ],
  'focus': [
    {'title': '重點整理', 'head': ('說法', '中文', '例子'), 'rows': [
      ('turn on / turn off', '打開 ／ 關掉（電器）', 'turn off the light'),
      ('in my opinion', '依我看', 'In my opinion, it\'s too expensive.'),
      ('once / twice / three times', '一次 ／ 兩次 ／ 三次', 'once a day'),
      ('offer + 人 + 東西', '提供某人…', 'offer him a job'),
      ('operate / operation', '操作、動手術 ／ 手術', 'have an operation'),
      ('organize / organization', '組織（動詞）／ 組織（名詞）', 'organize a trip'),
      ('my own / on my own', '我自己的 ／ 我獨自', 'my own room ／ do it on my own'),
    ], 'note': 'ox 的複數是 oxen；o\'clock 只用在整點：seven o\'clock。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '機會', 'opts': ['opinion', 'opportunity', 'operation', 'organization'], 'answer': 1, 'exp': 'opportunity 機會。'},
    {'type': 'mc', 'q': '遵守', 'opts': ['obey', 'omit', 'occur', 'offer'], 'answer': 0, 'exp': 'obey 遵守。'},
    {'type': 'mc', 'q': '烤箱', 'opts': ['onion', 'office', 'oven', 'owner'], 'answer': 2, 'exp': 'oven 烤箱。'},
    {'type': 'mc', 'q': '普通的', 'opts': ['official', 'outside', 'overseas', 'ordinary'], 'answer': 3, 'exp': 'ordinary 普通的。'},
  ]},
  {'title': '② 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '海洋（o＿＿＿＿，5 個字母）：{0}', 'blanks': [['ocean']], 'exp': 'ocean。'},
    {'q': '意見（o＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['opinion']], 'exp': 'opinion。'},
    {'q': '洋蔥（o＿＿＿＿，5 個字母）：{0}', 'blanks': [['onion']], 'exp': 'onion。'},
  ]},
  {'title': '③ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'Please turn {0} the light when you leave. （關掉）', 'blanks': [['off']], 'exp': 'turn off 關掉。'},
    {'q': 'I visit my grandparents {0} a month. （一次）', 'blanks': [['once']], 'exp': 'once a month 一個月一次。'},
    {'q': 'The boy {0} his seat to an old man. （提供，過去式）', 'blanks': [['offered']], 'exp': 'offer 的過去式 offered。'},
  ]},
  {'title': '④ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': '______ my opinion, we should go by train.', 'opts': ['On', 'In', 'At', 'For'], 'answer': 1, 'exp': 'in my opinion 依我看。'},
    {'type': 'mc', 'q': 'He wants to have his ______ room.', 'opts': ['owner', 'only', 'own', 'one'], 'answer': 2, 'exp': 'his own room 他自己的房間。'},
    {'type': 'mc', 'q': 'Students must ______ the school rules.', 'opts': ['obey', 'omit', 'occur', 'order'], 'answer': 0, 'exp': 'obey the rules 遵守規則。'},
    {'type': 'mc', 'q': 'The farmer has two ______ .', 'opts': ['ox', 'oxes', 'oxs', 'oxen'], 'answer': 3, 'exp': 'ox 的複數 oxen。'},
  ]},
]
