# 主題 2000 字 Unit 24：Weather & nature 天氣與大自然（字表依課本單元；詞性、中文、例句、題目為本站自編）
# cold（Unit 4 感冒）、cool（Unit 2 酷）、hot（Unit 10 辣）在前面出現過，這裡用天氣的意思。
def W(w, pos, zh, note, ex, exzh, pic):
    return {'w': w, 'pic': pic, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh}

UNIT = {
  'book': 'w2000', 'no': 24, 'en': 'Weather & nature', 'zh': '天氣與大自然',
  'intro': '說天氣的形容詞、天氣現象，還有天空裡的日月星辰，共 29 個字。很多天氣形容詞是「名詞＋y」：rain → rainy、sun → sunny。',
  'words': [
    W('weather', 'n.', '天氣', '不可數', 'What\'s the weather like today?', '今天天氣怎麼樣？', '🌤️'),
    W('clear', 'adj.', '晴朗的；清楚的', '', 'The sky is clear, so we can see the stars.', '天空很晴朗，所以我們看得到星星。', '🔭'),
    W('cloudy', 'adj.', '多雲的；陰天的', 'cloud＋y', 'It\'s cloudy, but it\'s not raining.', '天氣陰陰的，但沒有下雨。', '☁️'),
    W('cold', 'adj.', '冷的', '也當名詞「感冒」', 'It\'s cold outside. Put on your coat.', '外面很冷，穿上外套。', '🥶'),
    W('cool', 'adj.', '涼快的', '也有「很酷」的意思', 'The weather is cool in autumn.', '秋天天氣涼爽。', '🍂'),
    W('dry', 'adj.', '乾的；乾燥的', '相反 wet', 'The air is very dry in winter.', '冬天空氣很乾燥。', '🏜️'),
    W('hot', 'adj.', '熱的', '也有「辣的」的意思', 'It\'s so hot that I want to go swimming.', '天氣熱到我想去游泳。', '🥵'),
    W('rainy', 'adj.', '下雨的；多雨的', 'rain＋y；rainy day 雨天', 'Don\'t forget your umbrella on rainy days.', '雨天別忘了帶傘。', '🌧️'),
    W('snowy', 'adj.', '下雪的；積雪的', 'snow＋y', 'It was snowy in Japan when we visited.', '我們去日本的時候正在下雪。', '🌨️'),
    W('sunny', 'adj.', '晴朗的；陽光充足的', 'sun＋n＋y（要多一個 n）', 'Let\'s go on a picnic on a sunny day.', '找個晴天去野餐吧。', '☀️'),
    W('warm', 'adj.', '溫暖的', '', 'Spring is warm and comfortable.', '春天溫暖又舒服。', '🌷'),
    W('wet', 'adj.', '溼的；多雨的', '相反 dry', 'My shoes got wet in the rain.', '我的鞋子被雨淋溼了。', '💧'),
    W('windy', 'adj.', '有風的；風大的', 'wind＋y', 'It\'s too windy to use an umbrella.', '風太大了，沒辦法撐傘。', '🌬️'),
    W('rainbow', 'n.', '彩虹', 'rain＋bow', 'Look! There\'s a rainbow after the rain.', '你看！雨後有一道彩虹。', '🌈'),
    W('shower', 'n.', '陣雨；淋浴', 'take a shower 洗澡', 'There will be some showers this afternoon.', '今天下午會有陣雨。', '🌦️'),
    W('snow', 'n./v.', '雪；下雪', '雪不可數', 'The kids made a snowman in the snow.', '孩子們在雪地裡堆了一個雪人。', '❄️'),
    W('typhoon', 'n.', '颱風', '', 'School is closed because of the typhoon.', '因為颱風，學校停課。', '🌀'),
    W('wind', 'n.', '風', '', 'The wind blew my hat away.', '風把我的帽子吹走了。', '🍃'),
    W('blow', 'v.', '吹', '三態 blow／blew／blown', 'The wind is blowing hard tonight.', '今晚風吹得很大。', '💨'),
    W('rain', 'n./v.', '雨；下雨', '雨不可數；It is raining. 正在下雨', 'It started to rain when we left school.', '我們離開學校時開始下雨了。', '☔'),
    W('shine', 'v.', '照耀；發光', '照耀：shine／shone／shone', 'The sun is shining after the storm.', '暴風雨過後陽光照耀。', '🌞'),
    W('nature', 'n.', '大自然', '不可數；natural 自然的', 'We should protect nature.', '我們應該保護大自然。', '🌿'),
    W('cloud', 'n.', '雲', '', 'The clouds look like cotton candy.', '那些雲看起來像棉花糖。', '☁️'),
    W('earth', 'n.', '地球；土地', '指地球時常寫 the Earth', 'The Earth goes around the sun.', '地球繞著太陽轉。', '🌍'),
    W('earthquake', 'n.', '地震', 'earth＋quake（搖動）', 'The house shook during the earthquake.', '地震時房子在搖晃。', '🏚️'),
    W('moon', 'n.', '月亮', '常說 the moon', 'The moon is full and bright tonight.', '今晚的月亮又圓又亮。', '🌕'),
    W('sky', 'n.', '天空', '複數 skies；in the sky', 'Birds are flying in the sky.', '鳥在天空飛。', '🌌'),
    W('sun', 'n.', '太陽', '常說 the sun', 'The sun rises in the east.', '太陽從東邊升起。', '☀️'),
    W('star', 'n.', '星星', '也有「明星」的意思', 'We counted the stars in the night sky.', '我們數著夜空裡的星星。', '⭐'),
  ],
  'focus': [
    {'title': '名詞＋y → 天氣形容詞', 'head': ('名詞', '形容詞', '例句'), 'rows': [
      ('rain 雨', 'rainy 下雨的', 'It\'s rainy today.'),
      ('snow 雪', 'snowy 下雪的', 'It\'s snowy in Hokkaido.'),
      ('wind 風', 'windy 風大的', 'It\'s windy at the beach.'),
      ('cloud 雲', 'cloudy 多雲的', 'It\'s cloudy this morning.'),
      ('sun 太陽', 'sunny 晴朗的', 'It\'s sunny. 注意多一個 n'),
    ], 'note': '說天氣用 It：It is sunny. / It is raining.（正在下雨）'},
    {'title': '問天氣、說天氣', 'head': ('英文', '中文', ''), 'rows': [
      ('How\'s the weather today?', '今天天氣如何？', ''),
      ('What\'s the weather like in Taipei?', '臺北天氣怎麼樣？', ''),
      ('It\'s hot and wet in summer.', '夏天又熱又潮溼。', ''),
      ('It\'s going to rain tomorrow.', '明天會下雨。', ''),
      ('A typhoon is coming.', '颱風要來了。', ''),
    ], 'note': 'weather 不可數：nice weather（不是 a nice weather）。'},
    {'title': '相反詞與動詞三態', 'head': ('字', '相反／三態', ''), 'rows': [
      ('hot ↔ cold', 'warm ↔ cool', ''),
      ('dry ↔ wet', 'sunny ↔ cloudy', ''),
      ('blow', 'blow → blew → blown', ''),
      ('shine（照耀）', 'shine → shone → shone', ''),
      ('rain／snow', 'rained／snowed（規則變化）', ''),
    ], 'note': 'the sun、the moon、the Earth、the sky 前面通常加 the（只有一個）。'},
  ],
}

QUIZ = [
  {'title': '① 看中文選英文', 'items': [
    {'type': 'mc', 'q': '颱風', 'opts': ['typhoon', 'earthquake', 'rainbow', 'shower'], 'answer': 0, 'exp': 'typhoon 颱風。'},
    {'type': 'mc', 'q': '地震', 'opts': ['earth', 'earthquake', 'nature', 'thunder'], 'answer': 1, 'exp': 'earthquake 地震（earth＋quake）。'},
    {'type': 'mc', 'q': '彩虹', 'opts': ['rainy', 'raincoat', 'rainbow', 'rain'], 'answer': 2, 'exp': 'rainbow 彩虹。'},
    {'type': 'mc', 'q': '大自然', 'opts': ['natural', 'nation', 'weather', 'nature'], 'answer': 3, 'exp': 'nature 大自然。'},
    {'type': 'mc', 'q': '溫暖的', 'opts': ['warm', 'wet', 'windy', 'cool'], 'answer': 0, 'exp': 'warm 溫暖的。'},
  ]},
  {'title': '② 看英文選中文', 'items': [
    {'type': 'mc', 'q': 'shower', 'opts': ['陣雨', '彩虹', '雪', '雲'], 'answer': 0, 'exp': 'shower 陣雨（也是淋浴）。'},
    {'type': 'mc', 'q': 'dry', 'opts': ['溼的', '乾燥的', '涼快的', '熱的'], 'answer': 1, 'exp': 'dry 乾燥的；wet 溼的。'},
    {'type': 'mc', 'q': 'shine', 'opts': ['鞋子', '害羞', '照耀；發光', '吹'], 'answer': 2, 'exp': 'shine 照耀。'},
    {'type': 'mc', 'q': 'sky', 'opts': ['滑雪', '星星', '太陽', '天空'], 'answer': 3, 'exp': 'sky 天空。'},
  ]},
  {'title': '③ 拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': [
    {'q': '天氣（w＿＿＿＿＿＿，7 個字母）：{0}', 'blanks': [['weather']], 'exp': 'weather，中間是 ea。'},
    {'q': '晴朗的（s＿＿＿＿，5 個字母）：{0}', 'blanks': [['sunny']], 'exp': 'sun＋n＋y＝sunny。'},
    {'q': '雲（c＿＿＿＿，5 個字母）：{0}', 'blanks': [['cloud']], 'exp': 'cloud。'},
    {'q': '月亮（m＿＿＿，4 個字母）：{0}', 'blanks': [['moon']], 'exp': 'moon。'},
    {'q': '地球（e＿＿＿＿，5 個字母）：{0}', 'blanks': [['earth', 'Earth']], 'exp': 'earth（地球常寫 the Earth）。'},
  ]},
  {'title': '④ 單字變化', 'note': '照括號的提示寫出正確的字。', 'items': [
    {'q': 'rain → (形容詞，下雨的) {0}', 'blanks': [['rainy']], 'exp': 'rain＋y → rainy。'},
    {'q': 'wind → (形容詞，風大的) {0}', 'blanks': [['windy']], 'exp': 'wind＋y → windy。'},
    {'q': 'blow → (過去式) {0}', 'blanks': [['blew']], 'exp': 'blow → blew → blown。'},
    {'q': 'sky → (複數) {0}', 'blanks': [['skies']], 'exp': '子音＋y → skies。'},
  ]},
  {'title': '⑤ 例句填空：寫出正確的單字', 'note': '每題括號裡有中文提示。', 'items': [
    {'q': 'It\'s {0} today. Take an umbrella with you. （下雨的）', 'blanks': [['rainy']], 'exp': '帶傘 → rainy。'},
    {'q': 'There are many {0} in the night sky. （星星，複數）', 'blanks': [['stars']], 'exp': '很多星星 → stars。'},
    {'q': 'The {0} rises in the east and sets in the west. （太陽）', 'blanks': [['sun']], 'exp': '太陽 → the sun。'},
    {'q': 'My clothes are still {0}. They aren\'t dry yet. （溼的）', 'blanks': [['wet']], 'exp': '還沒乾 → wet。'},
    {'q': 'It is too {0} to wear a T-shirt. Put on a sweater. （冷的）', 'blanks': [['cold']], 'exp': '要穿毛衣 → cold。'},
  ]},
  {'title': '⑥ 用法：選出最合適的答案', 'items': [
    {'type': 'mc', 'q': '______ is the weather today? — It\'s windy.', 'opts': ['What', 'How', 'Who', 'Which'], 'answer': 1, 'exp': 'How is the weather? 天氣如何？'},
    {'type': 'mc', 'q': 'Look outside! It ______ now.', 'opts': ['rain', 'rains', 'is raining', 'rainy'], 'answer': 2, 'exp': '正在下雨 → It is raining.'},
    {'type': 'mc', 'q': 'We had ______ weather on our trip.', 'opts': ['a nice', 'nice', 'nices', 'an nice'], 'answer': 1, 'exp': 'weather 不可數，不加 a：nice weather。'},
    {'type': 'mc', 'q': 'The ______ goes around the sun once a year.', 'opts': ['moon', 'star', 'Earth', 'sky'], 'answer': 2, 'exp': '一年繞太陽一圈 → the Earth。'},
    {'type': 'mc', 'q': 'Everyone ran out of the building during the ______.', 'opts': ['earthquake', 'rainbow', 'nature', 'star'], 'answer': 0, 'exp': '地震時跑出大樓 → earthquake。'},
  ]},
]
