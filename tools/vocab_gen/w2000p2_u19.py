# 主題 2000 字 PART 2 Unit 19：Sizes & measurements 尺寸與測量（字表依課本 PART 2 印刷頁 160–161，17 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 19, 'en': 'Sizes & measurements', 'zh': '尺寸與測量',
  'card': 'kilometer、liter、rectangle、triangle、plus、minus、tiny、weight… 共 17 字；加減與單位',
  'intro': '長度、容量單位、形狀、加減、大小、距離和重量，共 17 個。loaf 的複數是 loaves。',
  'words': [
    W('kilometer', 'n.', '公里', 'km；1 kilometer = 1,000 meters', 'My school is two kilometers from my home.', '我的學校離家兩公里。', '📏'),
    W('liter', 'n.', '公升', 'L；英式拼 litre', 'Drink about two liters of water a day.', '每天喝大約兩公升的水。', '🧃'),
    W('meter', 'n.', '公尺', 'm；1 meter = 100 centimeters', 'He is almost two meters tall.', '他快兩公尺高了。', '📐'),
    W('rectangle', 'n.', '長方形', 'rectangular 長方形的', 'A door is shaped like a rectangle.', '門的形狀是長方形。', '🟦'),
    W('triangle', 'n.', '三角形', 'tri- 三', 'A triangle has three sides.', '三角形有三個邊。', '🔺'),
    W('distant', 'adj.', '遙遠的', 'distance 距離 → distant', 'We could hear distant thunder.', '我們聽見遠處的雷聲。', '🔭'),
    W('extra', 'adj.', '額外的；多餘的', 'extra money 額外的錢', 'Bring an extra pair of socks.', '多帶一雙襪子。', '➕'),
    W('maximum', 'adj. / n.', '最大的；最大量', '↔ minimum 最小量', 'The maximum speed here is 50 kilometers per hour.', '這裡最高速限每小時 50 公里。', '🔝'),
    W('minus', 'prep.', '減', '↔ plus', 'Ten minus four is six.', '十減四等於六。', '➖'),
    W('narrow', 'adj.', '狹窄的', '↔ wide 寬的', 'The street is too narrow for buses.', '這條街太窄，公車開不進來。', '↔️'),
    W('plus', 'prep.', '加', '↔ minus', 'Two plus three is five.', '二加三等於五。', '➕'),
    W('tiny', 'adj.', '極小的', 'tinier → tiniest', 'The ant is tiny, but it\'s very strong.', '螞蟻很小，但很強壯。', '🐜'),
    W('loaf', 'n.', '（一條）麵包', '複數 loaves；a loaf of bread', 'Mom bought two loaves of bread.', '媽媽買了兩條麵包。', '🍞'),
    W('distance', 'n.', '距離', 'in the distance 在遠處', 'What\'s the distance from Taipei to Taichung?', '台北到台中的距離有多遠？', '🗺️'),
    W('weight', 'n.', '重量；體重', 'weigh 秤重 → weight', 'Check the weight of your suitcase before the flight.', '搭機前先量一下行李的重量。', '⚖️'),
    W('amount', 'n.', '數量；總額', 'a large amount of + 不可數名詞', 'He drinks a large amount of water every day.', '他每天喝大量的水。', '🔢'),
    W('measure', 'v. / n.', '測量；措施', 'measurement 測量', 'Measure the table before you buy a tablecloth.', '買桌巾前先量一下桌子。', '📏'),
  ],
  'focus': [
    {'title': '單位', 'head': ('單位', '縮寫', '換算'),
     'rows': [('meter', 'm', '100 centimeters'), ('kilometer', 'km', '1,000 meters'), ('liter', 'L', '1,000 milliliters')],
     'note': ''},
    {'title': '加減怎麼說', 'head': ('算式', '英文', ''),
     'rows': [('2 + 3 = 5', 'Two plus three is five.', ''), ('10 − 4 = 6', 'Ten minus four is six.', '')],
     'note': 'loaf → loaves（f 變 v 加 -es），和 leaf → leaves、knife → knives 一樣。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=19, n_ce=6, n_ec=5, n_sp=5, fill=[
  F('Twenty ______ eight is twelve.', ['minus', 'plus', 'extra', 'tiny'], 0, '20 − 8 = 12 → minus。'),
  F('Seven ______ eight is fifteen.', ['plus', 'minus', 'narrow', 'distant'], 0, '7 + 8 = 15 → plus。'),
  F('Can I have two ______ of bread?', ['loaves', 'loafs', 'loaf', 'liters'], 0, 'loaf 的複數 loaves。'),
  F('This road is very ______. Two cars can\'t pass at the same time.', ['narrow', 'tiny', 'extra', 'maximum'], 0, '兩台車無法同時通過 → narrow 窄。'),
  F('A ______ has three sides and three corners.', ['triangle', 'rectangle', 'meter', 'loaf'], 0, '三個邊 → triangle。'),
  F('I need ______ time to finish the test.', ['extra', 'narrow', 'distant', 'tiny'], 0, 'extra time 額外的時間。'),
  F('Let me ______ your height. Stand against the wall.', ['measure', 'weight', 'amount', 'distance'], 0, '量身高 → measure。'),
])
