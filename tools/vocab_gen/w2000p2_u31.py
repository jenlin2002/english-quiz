# 主題 2000 字 PART 2 Unit 31：Prepositions 介系詞（字表依課本 PART 2 印刷頁 167–168，11 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

P = 'prep.'
UNIT = {
  'book': 'w2000p2', 'no': 31, 'en': 'Prepositions', 'zh': '介系詞',
  'card': 'against、among、beyond、in front of、next to、till、toward、upon、upper… 共 11 個',
  'intro': '表示位置、方向和時間的介系詞，共 11 個。among 用在三者以上（between 是兩者之間）；in back of = behind。',
  'words': [
    W('against', P, '靠著；反對；對抗', 'be against… 反對…', 'He leaned his bike against the wall.', '他把腳踏車靠在牆上。', '🧱'),
    W('among', P, '在…之中（三者以上）', '兩者之間用 between', 'The little house is hidden among the trees.', '那間小屋藏在樹林之中。', '🌲'),
    W('beyond', P, '在…的那一邊；超出', 'beyond the mountains 在山的另一邊', 'There is a small village beyond the river.', '河的那一邊有一個小村莊。', '🏞️'),
    W('in back of', P, '在…後面', '= behind', 'There is a garden in back of the house.', '房子後面有一個花園。', '🏡'),
    W('in front of', P, '在…前面', '↔ in back of／behind', 'Please don\'t stand in front of the TV.', '請不要站在電視前面。', '📺'),
    W('out of', P, '從…出來；離開', 'get out of bed 起床', 'The cat jumped out of the box.', '貓從箱子裡跳出來。', '📦'),
    W('next to', P, '在…旁邊；隔壁', '= beside', 'Come and sit next to me.', '過來坐我旁邊。', '🪑'),
    W('till', P, '直到', '= until', 'The store is open till ten p.m.', '這家店開到晚上十點。', '🕙'),
    W('toward', P, '朝向；向…方向', '= towards', 'The dog ran toward me.', '那隻狗朝我跑過來。', '➡️'),
    W('upon', P, '在…上面', '= on（比較正式）；Once upon a time 從前從前', 'Once upon a time, there lived a king.', '從前從前，有一位國王。', '📖'),
    W('upper', 'adj.', '上面的；上部的', '↔ lower 下面的', 'My room is on the upper floor.', '我的房間在樓上。', '🔝'),
  ],
  'focus': [
    {'title': '位置', 'head': ('介系詞', '意思', ''),
     'rows': [('in front of', '在前面', ''), ('in back of／behind', '在後面', ''), ('next to', '在旁邊', ''), ('among', '在（三者以上）之中', ''), ('between', '在（兩者）之間', '')],
     'note': 'in front of（在外面的前方）和 in the front of（在裡面的前段）不一樣。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=31, n_ce=6, n_ec=5, n_sp=4, fill=[
  F('Tom is sitting ______ Amy and Ken.', ['between', 'among', 'beyond', 'toward'], 0, '兩個人之間 → between。'),
  F('She is the tallest ______ all the girls in the class.', ['among', 'between', 'next to', 'upon'], 0, '三個以上之中 → among。'),
  F('Let\'s wait here ______ the rain stops.', ['till', 'toward', 'against', 'upon'], 0, '直到雨停 → till。'),
  F('Put the ladder ______ the wall.', ['against', 'among', 'beyond', 'out of'], 0, '靠著牆 → against。'),
  F('______ a time, there was a little girl named Snow White.', ['Once upon', 'Next to', 'Out of', 'In front of'], 0, 'Once upon a time 從前從前。'),
  F('The children ran ______ the ice cream truck.', ['toward', 'against', 'upon', 'among'], 0, '朝著冰淇淋車跑 → toward。'),
  F('Get ______ the car. We\'re here!', ['out of', 'next to', 'in front of', 'upon'], 0, '下車 → get out of the car。'),
])
