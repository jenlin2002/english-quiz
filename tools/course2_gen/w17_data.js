const GRAMMAR_QUESTIONS = [
  { text:"Never <span class='blank'>______</span> such a big dog.", options:["have I seen","I have seen","I saw","seen I have"], answer:0, note:"否定副詞 Never 放句首要倒裝：助動詞 have 放到主詞 I 前面。" },
  { text:"Seldom <span class='blank'>______</span> breakfast.", options:["does he eat","he eats","he does eat","eats he"], answer:0, note:"Seldom 放句首要倒裝；沒有助動詞時借 does，動詞改回原形 eat。" },
  { text:"Little <span class='blank'>______</span> that he was the new teacher.", options:["did I know","I knew","I did know","knew I"], answer:0, note:"Little 放句首表示「一點也不」，要倒裝：did I know。" },
  { text:"A: I like pizza. B: So <span class='blank'>______</span> I.", options:["do","am","like","have"], answer:0, note:"前一句用一般動詞 like，「我也是」用 So do I。" },
  { text:"A: She is very tired. B: So <span class='blank'>______</span> I.", options:["am","do","is","was"], answer:0, note:"前一句用 be 動詞 is，主詞是 I，所以用 So am I。" },
  { text:"A: I can't swim. B: <span class='blank'>______</span> can I.", options:["Neither","So","Either","Too"], answer:0, note:"前一句是否定句，「我也不」用 Neither can I。" },
  { text:"A: Tom didn't go to the party. B: Nor <span class='blank'>______</span> Amy.", options:["did","was","does","had"], answer:0, note:"前一句用 didn't（過去式），所以用 Nor did Amy。" },
  { text:"Not until midnight <span class='blank'>______</span> to bed.", options:["did he go","he went","he did go","went he"], answer:0, note:"Not until 放句首，主要子句要倒裝：did he go。" },
  { text:"Only then <span class='blank'>______</span> the problem.", options:["did I understand","I understood","I did understand","understood I"], answer:0, note:"Only + 副詞放句首要倒裝：did I understand。" },
  { text:"No sooner had I arrived <span class='blank'>______</span> it began to rain.", options:["than","when","then","that"], answer:0, note:"No sooner…than：一…就…，搭配的是 than。" },
  { text:"Hardly had she sat down <span class='blank'>______</span> the phone rang.", options:["when","than","then","that"], answer:0, note:"Hardly / Scarcely…when：一…就…，搭配的是 when。" },
  { text:"Not only <span class='blank'>______</span> smart, but she is also kind.", options:["is she","she is","does she","she does"], answer:0, note:"Not only 放句首，前半句要倒裝：is she。" },
  { text:"Here <span class='blank'>______</span>!", options:["comes the bus","the bus comes","does the bus come","the bus is come"], answer:0, note:"地方副詞 Here 放句首，主詞是名詞時要倒裝：Here comes the bus。" },
  { text:"<span class='blank'>______</span> I known the truth, I would have told you.", options:["Had","If","Have","Did"], answer:0, note:"條件句省略 if 的倒裝：If I had known → Had I known。" },
  { text:"It was Tom <span class='blank'>______</span> broke the window.", options:["that","what","which","whom"], answer:0, note:"強調句 It is / was…that…，強調人也可以用 who，但不能用 what。" },
  { text:"<span class='blank'>______</span> I need is a good rest.", options:["What","That","Which","It"], answer:0, note:"What I need is…：我需要的是…，what = the thing that。" },
  { text:"She is not as <span class='blank'>______</span> as her sister.（回收）", options:["tall","taller","tallest","more tall"], answer:0, note:"not as…as 中間用原級：tall。" },
  { text:"The harder you work, <span class='blank'>______</span> you will be.（回收）", options:["the more successful","more successful","the most successful","most successful"], answer:0, note:"the + 比較級, the + 比較級：the more successful。" },
  { text:"Either you or Tom <span class='blank'>______</span> to clean the room.（回收）", options:["has","have","are","were"], answer:0, note:"either…or 用就近原則，動詞看 Tom（單數）：has。" },
  { text:"He likes singing, dancing, and <span class='blank'>______</span>.（回收）", options:["painting","to paint","paint","painted"], answer:0, note:"平行結構：singing、dancing 都是 V-ing，所以用 painting。" }
];

const READING_PASSAGE = {
  title:"The Snowy Day",
  html:`Never had the small mountain village seen so much snow. It started on Monday night, and not until Wednesday afternoon did it finally stop. All the roads were closed, and so was the only school.<br><br>
It was an old farmer named Mr. Lin who cleared the main road first. Hardly had he finished when the children ran out to throw snowballs. "What this village needs is more people like him," said the mayor. Not only did Mr. Lin help his neighbors, but he also brought hot tea to everyone. Rarely do people forget such kindness.`
};

const READING_QUESTIONS = [
  { type:"閱讀理解", text:"What is the passage mainly about?", options:["A farmer who helped his village after a big snow","A school that opened a new class","A mayor who lost an election","Children who learned to cook"], answer:0, note:"全文講大雪之後，林先生幫助村民的故事。" },
  { type:"閱讀理解", text:"When did the snow stop?", options:["On Wednesday afternoon","On Monday night","On Tuesday morning","On Thursday"], answer:0, note:"文章提到 not until Wednesday afternoon did it finally stop。" },
  { type:"閱讀理解", text:"Who cleared the main road first?", options:["Mr. Lin, an old farmer","The mayor","The children","The teachers"], answer:0, note:"文章用強調句 It was an old farmer named Mr. Lin who cleared the main road first。" },
  { type:"閱讀理解", text:"What did the children do right after Mr. Lin finished?", options:["They threw snowballs.","They went to school.","They cleared the road.","They made hot tea."], answer:0, note:"Hardly had he finished when the children ran out to throw snowballs，表示他一做完小孩就跑出來丟雪球。" },
  { type:"閱讀理解", text:"Besides clearing the road, what else did Mr. Lin do?", options:["He brought hot tea to everyone.","He built a new school.","He opened a shop.","He drove the children home."], answer:0, note:"文章提到 Not only did Mr. Lin help his neighbors, but he also brought hot tea to everyone。" },
  { type:"文意選填", text:"Never ______ the small mountain village seen so much snow.（選出最適合填入文中空格的字）", options:["had","has","did","was"], answer:0, note:"Never 放句首要倒裝，過去完成式 had seen → had the village seen。" },
  { type:"文意選填", text:"All the roads were closed, and so ______ the only school.（選出最適合填入文中空格的字）", options:["was","did","were","had"], answer:0, note:"前面用 were closed，主詞 the only school 是單數，所以用 so was。" },
  { type:"文意選填", text:"It was an old farmer named Mr. Lin ______ cleared the main road first.（選出最適合填入文中空格的字）", options:["who","which","what","whom"], answer:0, note:"強調句 It was…who / that…，強調的是人，用 who。" },
  { type:"文意選填", text:"Hardly had he finished ______ the children ran out.（選出最適合填入文中空格的字）", options:["when","than","then","until"], answer:0, note:"Hardly…when：一…就…。" },
  { type:"文意選填", text:"Rarely ______ people forget such kindness.（選出最適合填入文中空格的字）", options:["do","are","have","does"], answer:0, note:"Rarely 放句首要倒裝，主詞 people 是複數，借助動詞 do。" }
];

const CLOZE_PASSAGE = {
  title:"My First Concert",
  html:`Last Saturday I went to my first concert. Never (1)<span class='blank'>____</span> I heard such loud music! My best friend loved it, and so (2)<span class='blank'>____</span> I.<br><br>
Not until the last song (3)<span class='blank'>____</span> we notice how late it was. (4)<span class='blank'>____</span> I remember most is the moment everyone sang together.`
};

const CLOZE_QUESTIONS = [
  { type:"克漏字 (1)", text:"選出最適合填入空格 (1) 的字：", options:["had","did","was","have"], answer:0, note:"Never 放句首倒裝；在那之前從來沒聽過，用過去完成式：Never had I heard。" },
  { type:"克漏字 (2)", text:"選出最適合填入空格 (2) 的字：", options:["did","was","do","had"], answer:0, note:"前一句用一般動詞過去式 loved，「我也是」用 so did I。" },
  { type:"克漏字 (3)", text:"選出最適合填入空格 (3) 的字：", options:["did","do","had","were"], answer:0, note:"Not until 放句首，主要子句倒裝，過去式借 did：did we notice。" },
  { type:"克漏字 (4)", text:"選出最適合填入空格 (4) 的字：", options:["What","That","Which","It"], answer:0, note:"What I remember most is…：我最記得的是…。" }
];

const LISTENING_QUESTIONS = [
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/bus.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Here comes the school bus, and the girl is ready.", "Here the school bus comes it, and the girl is ready.", "Here does the school bus come, and the girl is ready."], answer: 0,
    note: "地方副詞 Here 放句首，名詞主詞要倒裝：Here comes the school bus，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/library.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Rarely do students talk loudly in a library.", "Rarely students talk loudly in a library.", "Rarely are students talk loudly in a library."], answer: 0,
    note: "Rarely 放句首要倒裝，借助動詞 do，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/soccer.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["It is the boy in yellow who is going to kick the ball.", "It is the boy in yellow what is going to kick the ball.", "It is the boy in yellow which is going to kick the ball."], answer: 0,
    note: "強調句強調的是人，用 who 或 that，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/laptop.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["What the woman needs now is a cup of coffee and her laptop.", "That the woman needs now is a cup of coffee and her laptop.", "Which the woman needs now is a cup of coffee and her laptop."], answer: 0,
    note: "What…is… 表示「…的是」，所以答案是 (A)。"
  },
  {
    type: "看圖辨義", text: "請看照片，點按鈕聽題目與三個選項，選出正確答案。",
    audioQuestion: "Which sentence describes the picture?", image: "../img/lunch.jpg", imageCredit: "Photo from Pexels (pexels.com)",
    options: ["Not only are the children eating, but they are also chatting.", "Not only the children are eating, but they are also chatting.", "Not only do the children are eating, but they are also chatting."], answer: 0,
    note: "Not only 放句首要倒裝：are the children eating，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "I really love bubble tea.", options: ["So do I.", "So am I.", "Neither do I."], answer: 0,
    note: "對方用一般動詞 love 的肯定句，「我也是」用 So do I，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "I'm not ready for the test.", options: ["Neither am I.", "So am I.", "Neither do I."], answer: 0,
    note: "對方用 be 動詞的否定句，「我也不」用 Neither am I，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "When did you find out about the change?", options: ["Not until this morning did I hear about it.", "Not until this morning I heard about it.", "Not until this morning heard I about it."], answer: 0,
    note: "Not until 放句首，主要子句要倒裝並借 did，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽題目與三個選項，選出最適合的回答。",
    audioQuestion: "Who made this delicious cake?", options: ["It was my mother who made it.", "It was my mother what made it.", "It was my mother which made it."], answer: 0,
    note: "強調句強調人，用 who 或 that，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A boy says, No sooner had I got home than it started to rain. A girl says, Lucky you! I got wet on the way. Who got wet?",
    options: ["The girl", "The boy", "Both of them"], answer: 0,
    note: "男孩一到家就下雨，所以沒淋濕；女孩說 I got wet on the way，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A woman says, I can't find my keys anywhere. A man says, Neither can I. Did you check your bag? The woman says, Oh! Here they are. Where were the keys?",
    options: ["In her bag", "On the table", "In the car"], answer: 0,
    note: "男子問 Did you check your bag?，女子接著說 Here they are，表示鑰匙在包包裡，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A girl says, Had I known about the sale, I would have bought the shoes. A boy says, The sale ended yesterday. Did the girl buy the shoes?",
    options: ["No, she didn't know about the sale.", "Yes, she bought them yesterday.", "Yes, she bought two pairs."], answer: 0,
    note: "Had I known… = If I had known…，和過去事實相反，表示她不知道特價、沒有買，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "請點按鈕聽對話，選出最適合的答案。",
    audioQuestion: "A man says, It was in Tainan that I first tried beef soup. A woman says, Really? I thought it was in Taipei. Where did the man first try beef soup?",
    options: ["In Tainan", "In Taipei", "In Kaohsiung"], answer: 0,
    note: "強調句 It was in Tainan that… 強調地點是台南，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽廣播，選出最合理的答案。",
    audioQuestion: "Attention, passengers. Due to heavy rain, the train to Hualien will be late. Not until three o'clock will it arrive at this station. Should you need any help, please go to the service center. We are sorry for the trouble. When will the train arrive?",
    options: ["At three o'clock", "At two o'clock", "It has already arrived."], answer: 0,
    note: "Not until three o'clock will it arrive 表示三點才會到站，所以答案是 (A)。"
  },
  {
    type: "問答理解", text: "（進階）請點按鈕聽演講，選出最合理的答案。",
    audioQuestion: "Thank you all for coming. Never have I been so proud of my students. Not only did they win the contest, but they also helped the younger players. It is their kindness that I will remember most. What will the speaker remember most?",
    options: ["The students' kindness", "The prize money", "The contest rules"], answer: 0,
    note: "強調句 It is their kindness that I will remember most，所以答案是 (A)。"
  }
];

const VOCAB_QUESTIONS = [
  { word:"village", text:"village 這個字的中文意思最接近：", options:["村莊","城市","工廠","海灘"], answer:0, note:"village (n.) 村莊；villager = 村民。",
    example:"My grandparents live in a small village.", exampleZh:"我的祖父母住在一個小村莊。",
    scrambleSentence:"The village is famous for its tea.", zh:"這個村莊以茶聞名。" },
  { word:"concert", text:"concert 這個字的中文意思最接近：", options:["音樂會、演唱會","考試","會議","比賽"], answer:0, note:"concert (n.) 音樂會、演唱會。",
    example:"We went to a concert last night.", exampleZh:"我們昨晚去聽了一場演唱會。",
    scrambleSentence:"Never have I been to such a great concert.", zh:"我從來沒去過這麼棒的演唱會。" },
  { word:"rarely", text:"rarely 這個字的中文意思最接近：", options:["很少","常常","總是","馬上"], answer:0, note:"rarely (adv.) 很少、難得（= seldom）；放句首要倒裝。",
    example:"Rarely do we see snow in Taipei.", exampleZh:"我們在台北很少看到雪。",
    scrambleSentence:"He rarely eats fast food.", zh:"他很少吃速食。" },
  { word:"proud", text:"proud 這個字的中文意思最接近：", options:["驕傲的、自豪的","害羞的","生氣的","無聊的"], answer:0, note:"proud (adj.) 驕傲的、自豪的；be proud of = 以…為榮。",
    example:"My parents are proud of me.", exampleZh:"我的父母以我為榮。",
    scrambleSentence:"She was proud of her team.", zh:"她以她的隊伍為榮。" },
  { word:"kindness", text:"kindness 這個字的中文意思最接近：", options:["仁慈、好意","速度","力量","危險"], answer:0, note:"kindness (n.) 仁慈、好意；形容詞是 kind。",
    example:"Thank you for your kindness.", exampleZh:"謝謝你的好意。",
    scrambleSentence:"We will never forget his kindness.", zh:"我們永遠不會忘記他的好心。" },
  { word:"passenger", text:"passenger 這個字的中文意思最接近：", options:["乘客","司機","警察","店員"], answer:0, note:"passenger (n.) 乘客。",
    example:"All passengers must wear seat belts.", exampleZh:"所有乘客都必須繫安全帶。",
    scrambleSentence:"The bus was full of passengers.", zh:"公車上擠滿了乘客。" },
  { word:"contest", text:"contest 這個字的中文意思最接近：", options:["比賽、競賽","課程","禮物","假期"], answer:0, note:"contest (n.) 比賽、競賽；speech contest = 演講比賽。",
    example:"She won first prize in the speech contest.", exampleZh:"她在演講比賽中得到第一名。",
    scrambleSentence:"Our class joined the singing contest.", zh:"我們班參加了歌唱比賽。" },
  { word:"truth", text:"truth 這個字的中文意思最接近：", options:["事實、真相","謊言","秘密","故事"], answer:0, note:"truth (n.) 事實、真相；tell the truth = 說實話。",
    example:"Please tell me the truth.", exampleZh:"請告訴我實話。",
    scrambleSentence:"Had I known the truth, I would have helped.", zh:"如果我早知道真相，我就會幫忙了。" },
  { word:"notice", text:"notice 這個字的中文意思最接近：", options:["注意到","忘記","拒絕","搬家"], answer:0, note:"notice (v.) 注意到；(n.) 通知、公告。",
    example:"Did you notice the new sign?", exampleZh:"你有注意到新的標誌嗎？",
    scrambleSentence:"Not until later did I notice the mistake.", zh:"我直到後來才注意到那個錯誤。" },
  { word:"remember", text:"remember 這個字的中文意思最接近：", options:["記得","忘記","懷疑","猜測"], answer:0, note:"remember (v.) 記得；remember to V = 記得去做；remember V-ing = 記得做過。",
    example:"What I remember most is her smile.", exampleZh:"我最記得的是她的笑容。",
    scrambleSentence:"I still remember my first day at school.", zh:"我仍然記得我上學的第一天。" }
];

const SPEAKING_QUESTIONS = [
  { en:"Tell me about something amazing you have seen. Start with Never have I…", hint:"用 Never have I + p.p. 的倒裝句", sample:"Never have I seen such a beautiful sunset.", sampleZh:"我從來沒看過這麼美的夕陽。", checkType:"neverinv" },
  { en:"Your friend says, I love bubble tea. Do you agree? Answer with So or Neither.", hint:"用 So do I 或 Neither do I", sample:"So do I! I drink it every week.", sampleZh:"我也是！我每個禮拜都喝。", checkType:"soneither" },
  { en:"Tell me about something you didn't notice until later.", hint:"用 Not until…did I…", sample:"Not until I got home did I notice my phone was gone.", sampleZh:"直到回到家，我才發現手機不見了。", checkType:"notuntil" },
  { en:"Who taught you something important? Use It was…who…", hint:"用強調句 It was…who / that…", sample:"It was my grandmother who taught me to cook.", sampleZh:"是我奶奶教我煮飯的。", checkType:"cleft" },
  { en:"What do you need most right now?", hint:"用 What I need… is…", sample:"What I need most is a long holiday.", sampleZh:"我最需要的是一個長假。", checkType:"whatis" }
];
