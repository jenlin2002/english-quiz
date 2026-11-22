# 主題 2000 字 PART 2 Unit 4：Health 健康（字表依課本 PART 2 印刷頁 147–148，14 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 4, 'en': 'Health', 'zh': '健康',
  'intro': '生病、受傷、看醫生會用到的字，共 14 個。注意 -ache 的病痛：stomachache、toothache。',
  'words': [
    W('dizzy', 'adj.', '頭暈的', 'feel dizzy 覺得頭暈', 'I felt dizzy after the roller coaster ride.', '坐完雲霄飛車我覺得頭暈。', '😵‍💫'),
    W('ill', 'adj.', '生病的', '= sick；ill 多放在 be 動詞後面', 'Mike is ill, so he stayed home today.', 'Mike 生病了，所以今天待在家。', '🤒'),
    W('painful', 'adj.', '疼痛的；痛苦的', 'pain + -ful', 'My sore throat is very painful.', '我的喉嚨痛得很厲害。', '😣'),
    W('pale', 'adj.', '蒼白的', 'turn pale 臉色發白', 'You look pale. Are you OK?', '你臉色好蒼白，還好嗎？', '😶'),
    W('wound', 'n. / v.', '傷口；使受傷', '讀 [wund]', 'The nurse cleaned the wound on my knee.', '護士清理了我膝蓋上的傷口。', '🩹'),
    W('cancer', 'n.', '癌症；（大寫）巨蟹座', 'lung cancer 肺癌', 'Smoking can cause cancer.', '抽菸可能導致癌症。', '🎗️'),
    W('flu', 'n.', '流行性感冒', 'get the flu 得流感；cold 是一般感冒', 'Many students got the flu this winter.', '今年冬天很多學生得了流感。', '🤧'),
    W('stomachache', 'n.', '胃痛；肚子痛', 'stomach + ache；have a stomachache', 'I ate too much ice cream and got a stomachache.', '我吃太多冰淇淋，肚子痛了。', '🤢'),
    W('toothache', 'n.', '牙痛', 'tooth + ache', 'I have a toothache. I need to see a dentist.', '我牙痛，需要去看牙醫。', '🦷'),
    W('cough', 'v. / n.', '咳嗽', 'gh 讀 [f]', 'The boy kept coughing all night.', '那個男孩整晚一直咳嗽。', '😷'),
    W('pain', 'n.', '疼痛', 'have a pain in… …痛', 'I have a pain in my back.', '我背痛。', '🤕'),
    W('throat', 'n.', '喉嚨', 'have a sore throat 喉嚨痛', 'Drink warm water for your sore throat.', '喉嚨痛就喝溫開水。', '🗣️'),
    W('cure', 'v. / n.', '治療；治好', 'cure + 病／人', 'Doctors hope to cure the disease one day.', '醫生希望有一天能治好這種病。', '💊'),
    W('recover', 'v.', '恢復；康復', 'recover from 從…康復', 'Grandpa is recovering from a cold.', '爺爺感冒正在康復中。', '💪'),
  ],
  'focus': [
    {'title': '-ache 疼痛', 'head': ('部位', '疼痛', ''),
     'rows': [('stomach 胃', 'stomachache 胃痛', ''), ('tooth 牙齒', 'toothache 牙痛', ''), ('head 頭', 'headache 頭痛', '')],
     'note': '說「我…痛」用 I have a ___ache.；喉嚨痛說 I have a sore throat.'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=4, fill=[
  F('I ate some old fish and got a ______.', ['stomachache', 'toothache', 'cancer', 'beard'], 0, '吃壞東西 → stomachache 肚子痛。'),
  F('You look ______. Did you sleep last night?', ['pale', 'painful', 'ill', 'cure'], 0, '看起來臉色 pale 蒼白。'),
  F('I have a sore ______, so I can\'t sing today.', ['throat', 'wound', 'pain', 'flu'], 0, 'sore throat 喉嚨痛。'),
  F('She is ______ from the flu. She will come back to school next week.', ['recovering', 'coughing', 'curing', 'feeling'], 0, 'recover from 從…康復。'),
  F('Cover your mouth when you ______.', ['cough', 'cure', 'recover', 'wound'], 0, '咳嗽時遮住嘴巴 → cough。'),
  F('After spinning around ten times, I felt ______.', ['dizzy', 'pale', 'painful', 'ill'], 0, '轉了十圈 → dizzy 頭暈。'),
  F('Eat less candy, or you\'ll get a ______.', ['toothache', 'stomachache', 'cancer', 'wound'], 0, '少吃糖，不然會 toothache 牙痛。'),
])
