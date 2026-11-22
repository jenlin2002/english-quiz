# 主題 2000 字 PART 2 Unit 20：Countries and areas 國家與區域（字表依課本 PART 2 印刷頁 161，4 字；中文、例句、題目自編）
# 課本 PART 2 沒有 Unit 21（語言）。
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 20, 'en': 'Countries and areas', 'zh': '國家與區域',
  'intro': '亞洲、國家，以及台灣的兩個鄰居：日本和韓國，共 4 個。國名、洲名第一個字母要大寫。',
  'words': [
    W('Asia', 'n.', '亞洲', 'Asian 亞洲的；亞洲人', 'Taiwan is in East Asia.', '台灣在東亞。', '🌏'),
    W('nation', 'n.', '國家；民族', 'national 國家的；the United Nations 聯合國', 'People from every nation came to the Olympics.', '每個國家的人都來參加奧運。', '🏳️'),
    W('Japan', 'n.', '日本', 'Japanese 日本的；日語；日本人', 'We visited Tokyo, Japan, last summer.', '我們去年夏天去了日本東京。', '🇯🇵'),
    W('Korea', 'n.', '韓國', 'Korean 韓國的；韓語；韓國人', 'Many tourists from Korea visit Taiwan.', '很多韓國觀光客來台灣。', '🇰🇷'),
  ],
  'focus': [
    {'title': '國家、形容詞、人和語言', 'head': ('國家／地區', '形容詞／人／語言', ''),
     'rows': [('Asia 亞洲', 'Asian', ''), ('Japan 日本', 'Japanese', ''), ('Korea 韓國', 'Korean', ''), ('Taiwan 台灣', 'Taiwanese', '')],
     'note': '國名和它們的形容詞、語言，第一個字母都要大寫。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=20, n_ce=4, n_ec=4, n_sp=4, fill=[
  F('Sushi is a famous food from ______.', ['Japan', 'Korea', 'Asia', 'nation'], 0, '壽司來自 Japan 日本。'),
  F('Kimchi is a popular ______ food.', ['Korean', 'Korea', 'Japan', 'Asia'], 0, '形容詞 Korean 韓國的。'),
  F('China, Japan, and Taiwan are all in ______.', ['Asia', 'Korea', 'nation', 'Japan'], 0, '都在 Asia 亞洲。'),
  F('The whole ______ was happy when our team won the gold medal.', ['nation', 'Asia', 'Korea', 'Japan'], 0, '全國 → the whole nation。'),
])
