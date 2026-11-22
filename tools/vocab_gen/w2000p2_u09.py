# 主題 2000 字 PART 2 Unit 9：Money 金錢（字表依課本 PART 2 印刷頁 149–150，6 字；中文、例句、題目自編）
from p2kit import W, F, auto_quiz

UNIT = {
  'book': 'w2000p2', 'no': 9, 'en': 'Money', 'zh': '金錢',
  'intro': '付錢、賺錢會用到的字，共 6 個：帳單、現金、硬幣、信用卡、記帳（刷卡）、賺錢。',
  'words': [
    W('bill', 'n.', '帳單；紙鈔', 'pay the bill 付帳；a 100-dollar bill 一百元鈔票', 'Dad paid the bill after dinner.', '晚餐後爸爸付了帳。', '🧾'),
    W('cash', 'n.', '現金', '不可數；pay in cash 付現', 'Do you want to pay in cash or by card?', '你要付現還是刷卡？', '💵'),
    W('coin', 'n.', '硬幣', 'a ten-dollar coin 十元硬幣', 'I put three coins into the machine.', '我投了三個硬幣到機器裡。', '🪙'),
    W('credit card', 'n.', '信用卡', 'pay by credit card 用信用卡付', 'Mom paid for the plane tickets by credit card.', '媽媽用信用卡付了機票錢。', '💳'),
    W('charge', 'v. / n.', '收費；記帳；費用', 'free of charge 免費', 'The hotel charges 3,000 dollars a night.', '這家旅館一晚收三千元。', '🏨'),
    W('earn', 'v.', '賺（錢）；贏得', 'earn money 賺錢', 'My brother earns money by walking dogs.', '我哥哥靠幫人遛狗賺錢。', '💰'),
  ],
  'focus': [
    {'title': '怎麼付錢', 'head': ('說法', '意思', ''),
     'rows': [('pay in cash', '付現金', ''), ('pay by credit card', '刷信用卡', ''), ('pay the bill', '付帳', ''), ('free of charge', '免費', '')],
     'note': 'cash 不可數：不說 a cash、two cashes；coin 和 bill 可數。'},
  ],
}

QUIZ = auto_quiz(UNIT['words'], seed=9, n_ce=5, n_ec=4, n_sp=4, fill=[
  F('I don\'t have any ______. Can I pay by credit card?', ['cash', 'coin', 'bill', 'charge'], 0, '沒有 cash 現金。'),
  F('Waiter, can we have the ______, please?', ['bill', 'coin', 'cash', 'earn'], 0, '跟服務生要 bill 帳單。'),
  F('She ______ 200 dollars an hour by teaching piano.', ['earns', 'charges', 'pays', 'spends'], 0, '教鋼琴賺錢 → earns。'),
  F('The museum is free of ______ on Sundays.', ['charge', 'cash', 'bill', 'coin'], 0, 'free of charge 免費。'),
  F('He found a small ______ under the sofa. It was five dollars.', ['coin', 'credit card', 'bill', 'charge'], 0, '五元 → coin 硬幣。'),
])
