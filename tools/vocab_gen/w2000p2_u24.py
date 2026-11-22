# 主題 2000 字 PART 2 Unit 24：Weather & nature 天氣與大自然（字表依課本 PART 2 印刷頁 164，14 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 24, 'en': 'Weather & nature', 'zh': '天氣與大自然',
  'card': 'foggy、freezing、humid、storm、thunder、lightning、climate、temperature… 共 14 字；名詞加 -y 變形容詞',
  'intro': '天氣、自然現象、氣候和溫度，共 14 個。很多天氣名詞加 -y 就變形容詞：fog → foggy、storm → stormy。',
  'words': [
    W('foggy', 'adj.', '有霧的', 'fog + g + y', 'It was so foggy that we couldn\'t see the road.', '霧大到我們看不見路。', '🌫️'),
    W('freezing', 'adj.', '極冷的；冰凍的', 'freeze 結冰 → freezing', 'It\'s freezing outside. Wear your coat.', '外面冷死了，穿上外套。', '🥶'),
    W('humid', 'adj.', '潮濕的', 'humidity 濕度', 'Taiwan is hot and humid in summer.', '台灣夏天又熱又潮濕。', '💦'),
    W('stormy', 'adj.', '暴風雨的', 'storm + y', 'The boats stayed in the harbor on the stormy night.', '暴風雨的晚上船都留在港口。', '⛈️'),
    W('fog', 'n.', '霧', '不可數', 'The fog will clear up in the afternoon.', '霧會在下午散去。', '🌁'),
    W('lightning', 'n.', '閃電', '不可數；先看到閃電才聽到雷', 'Lightning hit the tall tree.', '閃電打中那棵高大的樹。', '⚡'),
    W('snowman', 'n.', '雪人', '複數 snowmen', 'The kids built a snowman in the yard.', '孩子們在院子裡堆了雪人。', '⛄'),
    W('storm', 'n.', '暴風雨', 'thunderstorm 雷雨', 'The storm knocked down many trees.', '暴風雨吹倒了很多樹。', '🌪️'),
    W('thunder', 'n.', '雷；雷聲', '不可數', 'My dog hides under the bed when it hears thunder.', '我的狗聽到雷聲就躲到床底下。', '🌩️'),
    W('natural', 'adj.', '自然的；天然的', 'nature → natural', 'This juice is made from natural fruit.', '這果汁是用天然水果做的。', '🍃'),
    W('air', 'n.', '空氣；天空', '不可數；fresh air 新鮮空氣', 'Let\'s open the window to get some fresh air.', '我們打開窗戶透透氣吧。', '🌬️'),
    W('climate', 'n.', '氣候', '長期的；weather 是每天的', 'Taiwan has a warm climate.', '台灣氣候溫暖。', '🌍'),
    W('degree', 'n.', '度數；學位', '30 degrees 三十度', 'It\'s 35 degrees today. It\'s really hot!', '今天三十五度，真的好熱！', '🌡️'),
    W('temperature', 'n.', '溫度；體溫', 'take one\'s temperature 量體溫', 'The nurse took my temperature.', '護士幫我量體溫。', '🤒'),
  ],
  'focus': [
    {'title': '名詞 → 形容詞', 'head': ('名詞', '形容詞', ''),
     'rows': [('fog 霧', 'foggy 有霧的', ''), ('storm 暴風雨', 'stormy 暴風雨的', ''), ('nature 自然', 'natural 自然的', ''), ('freeze 結冰（動詞）', 'freezing 極冷的', '')],
     'note': 'fog 是短母音加單子音，要重複 g 再加 -y：foggy。'},
    {'title': 'weather 和 climate', 'head': ('字', '意思', ''),
     'rows': [('weather', '某一天的天氣', ''), ('climate', '一個地方長期的氣候', '')],
     'note': ''},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=24, n_ce=6, n_ec=5, n_sp=5, fill=[
  F('It\'s so ______ that I can\'t see the mountains.', ['foggy', 'humid', 'natural', 'freezing'], 0, '看不到山 → foggy 有霧的。'),
  F('First we saw the ______, and then we heard the thunder.', ['lightning', 'fog', 'snowman', 'climate'], 0, '先看到閃電 lightning，再聽到雷。'),
  F('It\'s ______ cold today. The water turned into ice.', ['freezing', 'humid', 'foggy', 'natural'], 0, '水都結冰了 → freezing。'),
  F('The ______ in Taiwan is warm, but it\'s cold in Canada.', ['climate', 'temperature', 'degree', 'air'], 0, '一地的氣候 → climate。'),
  F('You have a fever. Let me take your ______.', ['temperature', 'climate', 'degree', 'weather'], 0, '量體溫 → take your temperature。'),
  F('The air is very wet in summer. It\'s really ______.', ['humid', 'freezing', 'stormy', 'foggy'], 0, '空氣很濕 → humid 潮濕的。'),
  F('It\'s 38 ______ today. Stay inside!', ['degrees', 'temperatures', 'climates', 'storms'], 0, '38 度 → 38 degrees。'),
])
