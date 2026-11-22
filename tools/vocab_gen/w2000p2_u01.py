# 主題 2000 字 PART 2（1201–2000 字彙）Unit 1：People 人物
# 字表依翰林《單字2000活用練習》PART 2 Unit 1（學用 PDF 印刷頁第 144 頁，16 字）；詞性、中文、例句、題目為本站自編。
def N(w, zh, note, ex, exzh, pic, pos='n.'):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000p2', 'no': 1, 'en': 'People', 'zh': '人物',
  'intro': '進階的「人物」名詞，共 16 個：大人、客人、主人、英雄、王子公主……注意男女成對的字（hero／heroine、host／hostess、prince／princess）和不規則複數。',
  'words': [
    N('adult', '成年人；大人', '= grown-up；↔ child', 'Kids under twelve must come with an adult.', '十二歲以下的小孩要有大人陪同。', '🧑'),
    N('angel', '天使；天使般的人', 'You are an angel! 你真是好人！', 'Thank you for helping me. You are an angel!', '謝謝你幫我，你真是個天使！', '👼'),
    N('couple', '一對夫妻；情侶', 'a couple of = 兩個；幾個', 'The old couple walk in the park every morning.', '那對老夫妻每天早上在公園散步。', '💑'),
    N('customer', '顧客', 'The customer is always right. 顧客永遠是對的', 'The shop gives every customer a free cookie.', '這家店送每位顧客一塊免費餅乾。', '🛒'),
    N('genius', '天才', '複數 geniuses', 'Mozart was a music genius. He wrote songs at age five.', '莫札特是音樂天才，五歲就會寫曲子。', '🧠'),
    N('gentleman', '紳士；先生', '複數 gentlemen；Ladies and gentlemen 各位先生女士', 'A gentleman opened the door for the old lady.', '一位紳士幫那位老太太開門。', '🎩'),
    N('guest', '客人；來賓', 'host 主人 ↔ guest 客人', 'We have ten guests coming to dinner tonight.', '今晚有十位客人來吃晚餐。', '🍽️'),
    N('hero', '英雄；男主角', '複數 heroes；女英雄 heroine', 'The firefighter became a hero after he saved the baby.', '那位消防員救了嬰兒之後成了英雄。', '🦸'),
    N('host', '主人；主持人', '女主人 hostess', 'The host of the party welcomed us at the door.', '派對的主人在門口歡迎我們。', '🎤'),
    N('lady', '女士；小姐', '複數 ladies；比 woman 有禮貌', 'The lady in the red dress is my aunt.', '穿紅洋裝的那位女士是我阿姨。', '👩‍🦰'),
    N('male', '男性的；雄性的', '↔ female 女性的', 'Most of the male students in my class play basketball.', '我們班大部分男生都打籃球。', '♂️', pos='adj.'),
    N('master', '主人；大師', 'master of the dog 狗的主人', 'The dog waited at the door for its master.', '那隻狗在門口等牠的主人。', '🐕'),
    N('partner', '夥伴；搭檔', 'work with a partner 和夥伴合作', 'Find a partner and practice the dialogue together.', '找一個夥伴一起練習對話。', '🤝'),
    N('prince', '王子', '公主 princess', 'In the story, the prince saved the princess from the dragon.', '故事裡，王子從龍手中救出公主。', '🤴'),
    N('princess', '公主', '複數 princesses', 'My little sister wants to be a princess for Halloween.', '我妹妹萬聖節想扮成公主。', '👸'),
    N('youth', '青春時期；年輕人', 'in my youth 我年輕的時候', 'My grandpa played baseball in his youth.', '我爺爺年輕時打棒球。', '🌱'),
  ],
  'focus': [
    {'title': '男女成對的字', 'head': ('男', '女', ''),
     'rows': [('hero', 'heroine', ''), ('host', 'hostess', ''), ('prince', 'princess', ''), ('gentleman', 'lady', ''), ('male', 'female', '')],
     'note': '-ess 常表示女性：host → hostess、prince → princess、actor → actress。'},
    ('要注意的複數', [('gentleman', 'gentlemen'), ('hero', 'heroes'), ('lady', 'ladies'), ('genius', 'geniuses'), ('princess', 'princesses')]),
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '顧客', 'opts': ['guest', 'customer', 'host', 'partner'], 'answer': 1, 'exp': 'customer 顧客（在店裡買東西的人）；guest 是被邀請來的客人。'},
    {'type': 'mc', 'q': '成年人；大人', 'opts': ['youth', 'adult', 'angel', 'master'], 'answer': 1, 'exp': 'adult 成年人 = grown-up。'},
    {'type': 'mc', 'q': '天才', 'opts': ['genius', 'gentleman', 'guest', 'hero'], 'answer': 0, 'exp': 'genius 天才（複數 geniuses）。'},
    {'type': 'mc', 'q': '夥伴；搭檔', 'opts': ['couple', 'prince', 'partner', 'lady'], 'answer': 2, 'exp': 'partner 夥伴。'},
    {'type': 'mc', 'q': '一對夫妻；情侶', 'opts': ['couple', 'customer', 'master', 'angel'], 'answer': 0, 'exp': 'couple 一對夫妻、情侶。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'youth', 'opts': ['主人', '青春時期；年輕人', '天使', '紳士'], 'answer': 1, 'exp': 'youth 青春時期；in my youth 我年輕的時候。'},
    {'type': 'mc', 'q': 'master', 'opts': ['主人；大師', '英雄', '王子', '客人'], 'answer': 0, 'exp': 'master 主人（狗的主人）；大師。'},
    {'type': 'mc', 'q': 'male', 'opts': ['女性的', '成年的', '男性的', '年輕的'], 'answer': 2, 'exp': 'male 男性的 ↔ female 女性的。'},
    {'type': 'mc', 'q': 'angel', 'opts': ['天使', '天才', '女士', '公主'], 'answer': 0, 'exp': 'angel 天使；也可說人很好心。'},
  ]},
  {'title': '③ 寫出女性的說法或複數', 'note': '注意 -ess 和不規則複數。', 'items': [
    {'q': 'prince → (女) {0}', 'blanks': [['princess']], 'exp': 'prince 王子 → princess 公主。'},
    {'q': 'host → (女) {0}', 'blanks': [['hostess']], 'exp': 'host 主人 → hostess 女主人。'},
    {'q': 'hero → (女) {0}', 'blanks': [['heroine']], 'exp': 'hero 英雄 → heroine 女英雄。'},
    {'q': 'one gentleman → two {0}', 'blanks': [['gentlemen']], 'exp': 'man → men，所以 gentleman → gentlemen。'},
    {'q': 'one lady → three {0}', 'blanks': [['ladies']], 'exp': '子音 + y → 去 y 加 -ies → ladies。'},
    {'q': 'one hero → many {0}', 'blanks': [['heroes']], 'exp': 'hero → heroes（加 -es）。'},
  ]},
  {'title': '④ 例句填空：選出最合適的單字', 'items': [
    {'type': 'mc', 'q': 'Ladies and ______, welcome to our show!', 'opts': ['gentlemen', 'guests', 'adults', 'partners'], 'answer': 0, 'exp': 'Ladies and gentlemen 各位先生女士。'},
    {'type': 'mc', 'q': 'The man saved three kids from the fire. He is a real ______.', 'opts': ['customer', 'hero', 'guest', 'couple'], 'answer': 1, 'exp': '從火場救出孩子 → hero 英雄。'},
    {'type': 'mc', 'q': 'This movie is not for kids. It is only for ______.', 'opts': ['adults', 'angels', 'princes', 'youths'], 'answer': 0, 'exp': '不適合小孩，只給大人 → adults。'},
    {'type': 'mc', 'q': 'The ______ of the party cooked a big dinner for all of us.', 'opts': ['host', 'guest', 'customer', 'genius'], 'answer': 0, 'exp': '辦派對、煮晚餐請大家的人 → host 主人。'},
    {'type': 'mc', 'q': 'Mom invited five ______ to our home for dinner.', 'opts': ['customers', 'guests', 'masters', 'heroes'], 'answer': 1, 'exp': '被邀請到家裡的人 → guests 客人。'},
    {'type': 'mc', 'q': 'The store is full of ______ on the first day of the sale.', 'opts': ['customers', 'angels', 'princesses', 'gentlemen'], 'answer': 0, 'exp': '店裡特賣第一天擠滿 → customers 顧客。'},
    {'type': 'mc', 'q': 'Mr. and Mrs. Lin are a happy ______.', 'opts': ['partner', 'couple', 'youth', 'master'], 'answer': 1, 'exp': '林先生和林太太是一對 → couple。'},
    {'type': 'mc', 'q': 'Grandma was a good swimmer in her ______.', 'opts': ['youth', 'adult', 'genius', 'lady'], 'answer': 0, 'exp': 'in her youth 她年輕的時候。'},
  ]},
]
