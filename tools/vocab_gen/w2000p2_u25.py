# 主題 2000 字 PART 2 Unit 25：Geographical terms 地理名詞（字表依課本 PART 2 印刷頁 164–165，9 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

N = 'n.'
UNIT = {
  'book': 'w2000p2', 'no': 25, 'en': 'Geographical terms', 'zh': '地理名詞',
  'intro': '海岸、沙漠、森林、海洋、平原、溪流、山谷、樹林和環境，共 9 個。注意 desert（沙漠）和 dessert（甜點）。',
  'words': [
    W('coast', N, '海岸；海濱', 'on the coast 在海岸邊', 'We drove along the east coast of Taiwan.', '我們沿著台灣東海岸開車。', '🏖️'),
    W('desert', N, '沙漠', '一個 s；dessert（甜點）兩個 s', 'Camels can walk in the desert for days.', '駱駝可以在沙漠走好幾天。', '🏜️'),
    W('environment', N, '環境', 'environmental 環境的', 'We should protect the environment.', '我們應該保護環境。', '♻️'),
    W('forest', N, '森林', '比 woods 大', 'Many animals live in the forest.', '很多動物住在森林裡。', '🌲'),
    W('ocean', N, '海洋', 'the Pacific Ocean 太平洋', 'Whales live in the ocean.', '鯨魚住在海洋裡。', '🌊'),
    W('plain', 'n. / adj.', '平原；樸素的；簡單的', 'plain clothes 樸素的衣服', 'Rice grows well on the wide plain.', '稻米在廣大的平原上長得很好。', '🌾'),
    W('stream', N, '小溪；溪流', '比 river 小', 'We caught small fish in the stream.', '我們在小溪裡抓小魚。', '🏞️'),
    W('valley', N, '山谷', '複數 valleys', 'A small village sits in the valley.', '一個小村莊座落在山谷中。', '⛰️'),
    W('woods', N, '樹林', '常用複數；比 forest 小', 'We took a walk in the woods.', '我們在樹林裡散步。', '🌳'),
  ],
  'focus': [
    {'title': '大小比一比', 'head': ('大', '小', ''),
     'rows': [('ocean 海洋', 'sea 海', ''), ('river 河', 'stream 小溪', ''), ('forest 森林', 'woods 樹林', '')],
     'note': 'desert 沙漠（一個 s）↔ dessert 甜點（兩個 s，甜點吃兩份）。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=25, n_ce=5, n_ec=5, n_sp=5, fill=[
  F('There is almost no water in the ______.', ['desert', 'dessert', 'stream', 'ocean'], 0, '沒有水 → desert 沙漠（一個 s）。'),
  F('Don\'t throw trash on the ground. Protect the ______.', ['environment', 'coast', 'valley', 'plain'], 0, '保護 environment 環境。'),
  F('The Pacific ______ is the biggest in the world.', ['Ocean', 'Stream', 'Forest', 'Desert'], 0, 'the Pacific Ocean 太平洋。'),
  F('Hualien is on the east ______ of Taiwan.', ['coast', 'desert', 'valley', 'woods'], 0, '在東海岸 → east coast。'),
  F('The river runs through a deep ______ between two mountains.', ['valley', 'plain', 'coast', 'desert'], 0, '兩座山之間 → valley 山谷。'),
  F('She likes ______ clothes. She doesn\'t like bright colors.', ['plain', 'natural', 'humid', 'stormy'], 0, '樸素的衣服 → plain。'),
])
