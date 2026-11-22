# 主題 2000 字 PART 2 Unit 13：Colors 顏色（字表依課本 PART 2 印刷頁 153：golden；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 13, 'en': 'Colors', 'zh': '顏色',
  'intro': 'PART 2 的顏色只有一個字：golden 金色的。gold 是「金子」，golden 是「金色的」。',
  'words': [
    W('golden', 'adj.', '金色的；金黃色的；珍貴的', 'gold 金 → golden 金色的；golden chance 大好機會', 'The rice fields turn golden in autumn.', '稻田在秋天變成金黃色。', '🌾'),
  ],
  'focus': [
    {'title': 'gold 和 golden', 'head': ('字', '用法', ''),
     'rows': [('gold', '金子（材料）：a gold ring 金戒指', ''), ('golden', '金色的、像金子的：golden hair 金髮', '')],
     'note': 'golden 也可以是「珍貴的」：a golden chance 千載難逢的機會。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=13, n_ce=0, n_ec=0, n_sp=1, fill=[
  F('The little girl has long ______ hair, like a princess.', ['golden', 'gold', 'silver', 'iron'], 0, '金色頭髮 → golden hair。'),
  F('This is a ______ chance. Don\'t miss it!', ['golden', 'gold', 'cotton', 'iron'], 0, 'golden chance 大好機會。'),
  F('He gave her a ring made of real ______.', ['gold', 'golden', 'goldy', 'goal'], 0, '金子這種材料 → gold。'),
])
