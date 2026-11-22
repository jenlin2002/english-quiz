# 主題 2000 字 PART 2 Unit 8：Time 時間（字表依課本 PART 2 印刷頁 148–149，8 字；書上寫 stop watch，這裡用 stopwatch；中文、例句、題目自編）
# 課本 PART 2 沒有 Unit 7。
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 8, 'en': 'Time', 'zh': '時間',
  'intro': '和時間有關的進階字，共 8 個：黎明、午夜、平日、鬧鐘、日曆、碼錶、目前的、每天的。',
  'words': [
    W('dawn', 'n.', '黎明；破曉', 'at dawn 在黎明時', 'The farmers get up at dawn.', '農夫們天一亮就起床。', '🌅'),
    W('midnight', 'n.', '午夜；半夜十二點', 'at midnight 在午夜', 'Cinderella had to go home before midnight.', '灰姑娘必須在午夜前回家。', '🌙'),
    W('weekday', 'n.', '平日；工作日（週一到週五）', '↔ weekend 週末；on weekdays', 'I get up at six thirty on weekdays.', '我平日六點半起床。', '📅'),
    W('alarm clock', 'n.', '鬧鐘', 'set the alarm clock 設定鬧鐘', 'I set my alarm clock for six o\'clock.', '我把鬧鐘設在六點。', '⏰'),
    W('calendar', 'n.', '日曆；月曆', 'mark on the calendar 在日曆上做記號', 'I marked Mom\'s birthday on the calendar.', '我在日曆上把媽媽的生日做了記號。', '🗓️'),
    W('stopwatch', 'n.', '碼錶', 'stop + watch', 'The coach used a stopwatch to time our run.', '教練用碼錶幫我們跑步計時。', '⏱️'),
    W('current', 'adj.', '目前的；流行的', 'current events 時事', 'What is your current address?', '你目前的地址是什麼？', '📰'),
    W('daily', 'adj. / adv.', '每天的；每天', '= everyday；day → daily', 'Reading the news is part of my daily life.', '看新聞是我日常生活的一部分。', '☕'),
  ],
  'focus': [
    {'title': '一天的時間', 'head': ('時候', '英文', ''),
     'rows': [('天剛亮', 'at dawn', ''), ('半夜十二點', 'at midnight', ''), ('週一到週五', 'on weekdays', ''), ('週末', 'on weekends', '')],
     'note': 'day → daily、week → weekly、month → monthly、year → yearly：加 -ly 變成「每…的」。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=8, fill=[
  F('I didn\'t hear my ______, so I was late for school.', ['alarm clock', 'calendar', 'stopwatch', 'dawn'], 0, '沒聽到 alarm clock 鬧鐘。'),
  F('The store is open from 9 to 5 on ______.', ['weekdays', 'midnight', 'dawn', 'calendars'], 0, 'on weekdays 平日。'),
  F('Let me check my ______ to see if I\'m free on Friday.', ['calendar', 'stopwatch', 'alarm clock', 'midnight'], 0, '查 calendar 日曆。'),
  F('The party ended at ______, twelve o\'clock at night.', ['midnight', 'dawn', 'weekday', 'noon'], 0, '晚上十二點 → midnight。'),
  F('Exercise is part of my ______ life.', ['daily', 'current', 'pale', 'elder'], 0, 'daily life 日常生活。'),
  F('The birds start to sing at ______.', ['dawn', 'midnight', 'weekday', 'calendar'], 0, '天一亮 → at dawn。'),
])
