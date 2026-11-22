# 主題 2000 字 PART 2 Unit 18：Transportation 交通運輸（字表依課本 PART 2 印刷頁 159–160，20 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 18, 'en': 'Transportation', 'zh': '交通運輸',
  'card': 'ambulance、helicopter、airline、MRT、overpass、passenger、platform、wheel… 共 20 字',
  'intro': '交通工具、車站、道路和乘車用語，共 20 個。注意 overpass（天橋）↔ underpass（地下道）。',
  'words': [
    W('ambulance', N, '救護車', 'call an ambulance 叫救護車', 'Call an ambulance! Someone is hurt.', '叫救護車！有人受傷了。', '🚑'),
    W('helicopter', N, '直升機', '', 'The helicopter landed on the roof of the hospital.', '直升機降落在醫院屋頂上。', '🚁'),
    W('jeep', N, '吉普車', '', 'We rode a jeep up the mountain.', '我們坐吉普車上山。', '🚙'),
    W('tank', N, '坦克；水箱；油箱', 'gas tank 油箱；fish tank 魚缸', 'We have three goldfish in our fish tank.', '我們的魚缸裡有三條金魚。', '🐠'),
    W('airline', N, '航空公司', 'air + line', 'Which airline are you flying with?', '你搭哪一家航空公司？', '✈️'),
    W('bus stop', N, '公車站', '', 'I\'ll wait for you at the bus stop.', '我在公車站等你。', '🚏'),
    W('parking lot', N, '停車場', 'park 停車', 'The parking lot is full today.', '今天停車場滿了。', '🅿️'),
    W('train station', N, '火車站', '', 'Let\'s meet at the train station at nine.', '我們九點在火車站見。', '🚉'),
    W('flat tire', N, '爆胎；輪胎沒氣', 'flat 扁平的', 'We got a flat tire on the way home.', '我們回家路上爆胎了。', '🛞'),
    W('highway', N, '公路；高速公路', 'high + way', 'Cars drive fast on the highway.', '車子在高速公路上開得很快。', '🛣️'),
    W('MRT', N, '捷運（大眾捷運系統）', 'Mass Rapid Transit', 'I take the MRT to school every day.', '我每天搭捷運上學。', '🚇', say='M R T', exsay='I take the M R T to school every day.'),
    W('overpass', N, '天橋；陸橋', 'over 上方 + pass 通過', 'Use the overpass to cross the busy road.', '走天橋過這條車很多的馬路。', '🌉'),
    W('passenger', N, '乘客', '', 'All passengers must wear seat belts.', '所有乘客都必須繫安全帶。', '🧑‍🤝‍🧑'),
    W('path', N, '小路；小徑', '', 'Follow the path to the lake.', '沿著小路走到湖邊。', '🥾'),
    W('platform', N, '月台；講台', 'Platform 2 第二月台', 'The train to Kaohsiung leaves from Platform 2.', '往高雄的火車從第二月台出發。', '🚆'),
    W('railroad', N, '鐵路', '= railway', 'The railroad runs along the coast.', '這條鐵路沿著海岸走。', '🛤️'),
    W('railway', N, '鐵路；鐵道', '= railroad（英式）', 'Taiwan High Speed Railway is very fast.', '台灣高鐵非常快。', '🚄'),
    W('subway', N, '地鐵', '= MRT／metro／underground', 'You can take the subway to the museum.', '你可以搭地鐵去博物館。', '🚊'),
    W('underpass', N, '地下道', 'under 下方 + pass；↔ overpass', 'There are many small shops in the underpass.', '地下道裡有很多小商店。', '🚶'),
    W('wheel', N, '輪子；方向盤', 'steering wheel 方向盤', 'A bicycle has two wheels.', '腳踏車有兩個輪子。', '☸️'),
  ],
  'focus': [
    {'title': '過馬路：上面還是下面', 'head': ('字', '意思', ''),
     'rows': [('overpass', '天橋（從上面過）', ''), ('underpass', '地下道（從下面過）', ''), ('crosswalk', '斑馬線', '')],
     'note': 'over 在上、under 在下；pass 通過。'},
    {'title': '各地的「地鐵」', 'head': ('地方', '說法', ''),
     'rows': [('台灣', 'MRT', ''), ('美國', 'subway', ''), ('英國倫敦', 'the Underground', '')],
     'note': ''},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=18, n_ce=6, n_ec=5, n_sp=5, fill=[
  F('A man fell down and couldn\'t get up. We called an ______.', ['ambulance', 'airline', 'overpass', 'jeep'], 0, '有人受傷 → ambulance 救護車。'),
  F('The road is too busy to cross. Let\'s take the ______.', ['overpass', 'highway', 'wheel', 'tank'], 0, '過馬路走 overpass 天橋。'),
  F('There were only five ______ on the bus.', ['passengers', 'platforms', 'wheels', 'airlines'], 0, '車上的人 → passengers 乘客。'),
  F('Our car stopped because of a ______. Dad had to change it.', ['flat tire', 'bus stop', 'parking lot', 'path'], 0, '換輪胎 → flat tire 爆胎。'),
  F('The train is coming. Please wait behind the yellow line on the ______.', ['platform', 'highway', 'overpass', 'wheel'], 0, '月台上等車 → platform。'),
  F('There is no space in the ______. Where can we park the car?', ['parking lot', 'bus stop', 'subway', 'underpass'], 0, '停車 → parking lot 停車場。'),
  F('A car has four ______.', ['wheels', 'tanks', 'paths', 'jeeps'], 0, '汽車四個 wheels 輪子。'),
])
