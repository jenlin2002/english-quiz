# 主題 2000 字 PART 2 Unit 22：Holidays & festivals 節日與慶典（字表依課本 PART 2 印刷頁 161–162，16 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 22, 'en': 'Holidays & festivals', 'zh': '節日與慶典',
  'card': 'Chinese New Year、Lantern Festival、Moon Festival、Thanksgiving、custom、lantern… 共 16 字；節日前用 on',
  'intro': '台灣和西方的節日，還有文化、習俗、燈籠和回憶，共 16 個。節日名稱每個字的第一個字母大寫；「在某個節日」用 on（on Mother\'s Day）。',
  'words': [
    W('Chinese New Year', N, '農曆新年；春節', 'at／during Chinese New Year', 'Kids get red envelopes at Chinese New Year.', '過年時小孩會拿到紅包。', '🧧'),
    W('New Year\'s Eve', N, '除夕；跨年夜', 'Eve 前夕', 'We watch fireworks on New Year\'s Eve.', '我們在跨年夜看煙火。', '🎆'),
    W('Double Tenth Day', N, '雙十節；國慶日', '十月十日', 'Double Tenth Day is Taiwan\'s National Day.', '雙十節是台灣的國慶日。', '🇹🇼'),
    W('Dragon Boat Festival', N, '端午節', '農曆五月五日', 'We watch dragon boat races at the Dragon Boat Festival.', '端午節我們看龍舟比賽。', '🐉'),
    W('Lantern Festival', N, '元宵節', '農曆一月十五日', 'People eat sweet dumplings at the Lantern Festival.', '元宵節大家吃湯圓。', '🏮'),
    W('Moon Festival', N, '中秋節', '= Mid-Autumn Festival', 'Families eat moon cakes and pomelos at the Moon Festival.', '中秋節家人一起吃月餅和柚子。', '🥮'),
    W('Teacher\'s Day', N, '教師節', '九月二十八日（孔子誕辰）', 'We made cards for our teachers on Teacher\'s Day.', '教師節我們做卡片送老師。', '🍎'),
    W('New Year\'s Day', N, '元旦', '一月一日', 'New Year\'s Day is January 1st.', '元旦是一月一日。', '🎉'),
    W('Mother\'s Day', N, '母親節', '五月第二個星期日', 'I made breakfast for Mom on Mother\'s Day.', '母親節我幫媽媽做早餐。', '💐'),
    W('Father\'s Day', N, '父親節', '台灣是八月八日', 'We took Dad out to dinner on Father\'s Day.', '父親節我們帶爸爸出去吃晚餐。', '👔'),
    W('Thanksgiving', N, '感恩節', '美國：十一月第四個星期四', 'Americans eat turkey on Thanksgiving.', '美國人感恩節吃火雞。', '🦃'),
    W('Valentine\'s Day', N, '情人節', '二月十四日', 'He gave her chocolate on Valentine\'s Day.', '情人節他送她巧克力。', '💝'),
    W('culture', N, '文化', 'cultural 文化的', 'I want to learn more about Japanese culture.', '我想多了解日本文化。', '🎎'),
    W('custom', N, '習俗；風俗', 'customs 海關（複數）', 'Giving red envelopes is a Chinese New Year custom.', '發紅包是過年的習俗。', '🏯'),
    W('lantern', N, '燈籠', 'Lantern Festival 元宵節', 'The kids carried paper lanterns at night.', '孩子們晚上提著紙燈籠。', '🏮'),
    W('memory', N, '記憶；回憶', '複數 memories；memorize 背誦', 'I have many happy memories of my childhood.', '我有很多快樂的童年回憶。', '📸'),
  ],
  'focus': [
    {'title': '節日在哪一天', 'head': ('節日', '時間', ''),
     'rows': [('Chinese New Year', '農曆一月一日', ''), ('Lantern Festival', '農曆一月十五日', ''), ('Dragon Boat Festival', '農曆五月五日', ''), ('Moon Festival', '農曆八月十五日', ''), ('Double Tenth Day', '十月十日', '')],
     'note': '「在某節日當天」用 on：on Mother\'s Day、on Valentine\'s Day。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=22, n_ce=6, n_ec=5, n_sp=4, fill=[
  F('We eat rice dumplings and watch boat races at the ______.', ['Dragon Boat Festival', 'Moon Festival', 'Lantern Festival', 'Thanksgiving'], 0, '粽子、龍舟 → Dragon Boat Festival。'),
  F('People eat turkey with their family on ______.', ['Thanksgiving', 'Teacher\'s Day', 'Double Tenth Day', 'New Year\'s Day'], 0, '吃火雞 → Thanksgiving。'),
  F('On ______, we look at the full moon and eat moon cakes.', ['the Moon Festival', 'Valentine\'s Day', 'Mother\'s Day', 'New Year\'s Eve'], 0, '賞月吃月餅 → Moon Festival。'),
  F('Giving red envelopes is an old Chinese ______.', ['custom', 'lantern', 'memory', 'nation'], 0, '發紅包是 custom 習俗。'),
  F('I have a bad ______. I always forget people\'s names.', ['memory', 'culture', 'custom', 'lantern'], 0, '記不住名字 → memory 記憶力。'),
  F('Taiwan\'s National Day is ______.', ['Double Tenth Day', 'New Year\'s Day', 'Father\'s Day', 'Teacher\'s Day'], 0, '國慶日 → Double Tenth Day 雙十節。'),
  F('My family stays up late to welcome the new year on New Year\'s ______.', ['Eve', 'Day', 'Festival', 'Custom'], 0, '跨年夜 → New Year\'s Eve。'),
])
