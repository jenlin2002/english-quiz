  } else if(q.checkType === 'asas'){
    if(!/\bas\s+(?:[a-z]+\s+){1,3}?as\b/.test(lower)){ ok = false; msg = '這一題要練習 as…as 或 not as…as，但沒有偵測到，可以再試著說像 "My sister is not as tall as I am." 這樣的句子。'; }
    else if(/\bas\s+(?:more\s+[a-z]+|taller|bigger|smaller|faster|older|younger|better|longer|shorter|happier|busier|heavier|richer|stronger|smarter|higher|cheaper)\s+as\b/.test(lower)){ ok = false; msg = 'as…as 中間要用原級，不能用比較級（例如 as tall as，不是 as taller as），可以再說一次。'; }
    else { msg = '偵測到 as…as 的同級比較，符合這題要練習的重點！記得中間用原級。'; }
  } else if(q.checkType === 'themore'){
    if(!/\bthe\s+(?:more|less|[a-z]+er)\b[^.?!]*,?\s*\bthe\s+(?:more|less|[a-z]+er)\b/.test(lower)){ ok = false; msg = '這一題要練習「The + 比較級…, the + 比較級…」，但沒有偵測到，可以再試著說像 "The more I read, the more I learn." 這樣的句子。'; }
    else { msg = '偵測到「the + 比較級, the + 比較級」，符合這題要練習的重點！'; }
  } else if(q.checkType === 'superlative'){
    if(!/\bthan\s+any\s+other\b|\bno\s+other\b|\bone\s+of\s+the\s+(?:most\s+[a-z]+|[a-z]+est|best|worst)\b|\bthe\s+(?:most\s+[a-z]+|[a-z]+est|best|worst)\s+[a-z]+\s+(?:i|we)\s+(?:have|'ve)\s+ever\b/.test(lower)){ ok = false; msg = '這一題要練習 than any other、no other 或 one of the + 最高級，但沒有偵測到，可以再試著說像 "The night market is more interesting than any other place in my city." 這樣的句子。'; }
    else if(/\bthan\s+any\s+other\s+[a-z]+s\b/.test(lower) && !/\bthan\s+any\s+other\s+(?:class|bus|glass|business|boss)\b/.test(lower)){ ok = false; msg = '偵測到 than any other，但後面好像接了複數名詞。than any other 後面要接單數名詞，例如 any other place，可以再說一次。'; }
    else { msg = '偵測到用比較級或最高級表達「最…」的句型，符合這題要練習的重點！'; }
  } else if(q.checkType === 'correl'){
    if(!/\bboth\b[^.?!]*\band\b|\beither\b[^.?!]*\bor\b|\bneither\b[^.?!]*\bnor\b/.test(lower)){ ok = false; msg = '這一題要練習 both…and、either…or 或 neither…nor，但沒有偵測到，可以再試著說像 "I like both basketball and swimming." 這樣的句子。'; }
    else { msg = '偵測到對等相關連接詞，符合這題要練習的重點！記得 both 用複數，either / neither 看最靠近的主詞。'; }
  } else if(q.checkType === 'notonly'){
    if(!/\bnot\s+only\b[^.?!]*\bbut\b/.test(lower)){ ok = false; msg = '這一題要練習 not only…but also，但沒有偵測到，可以再試著說像 "My best friend is not only funny but also helpful." 這樣的句子。'; }
    else { msg = '偵測到 not only…but also，符合這題要練習的重點！記得前後的形式要一樣（平行結構）。'; }
  } else if(q.checkType === 'neverinv'){
    if(!/\b(?:never|seldom|rarely|little|hardly|not once)\s+(?:have|has|had|do|does|did|am|is|are|was|were|can|could|will|would)\s+(?:i|you|he|she|we|they|it)\b/.test(lower)){ ok = false; msg = '這一題要練習否定副詞放句首的倒裝（Never have I…），但沒有偵測到，可以再試著說像 "Never have I seen such a beautiful sunset." 這樣的句子。'; }
    else { msg = '偵測到否定副詞 + 助動詞 + 主詞的倒裝句，符合這題要練習的重點！'; }
  } else if(q.checkType === 'soneither'){
    if(!/\b(?:so|neither|nor)\s+(?:do|does|did|am|is|are|was|were|have|has|had|can|could|will|would)\s+(?:i|we|you|he|she|they)\b/.test(lower)){ ok = false; msg = '這一題要練習 So do I 或 Neither do I，但沒有偵測到，可以再試著說像 "So do I!" 這樣的句子。'; }
    else if(/\bso\s+i\s+(?:do|am|can|did)\b/.test(lower) && !/\bso\s+(?:do|am|can|did)\s+i\b/.test(lower)){ ok = false; msg = '偵測到 So I do，這是「我確實如此」的意思。表示「我也是」要倒裝：So do I。'; }
    else { msg = '偵測到 So / Neither + 助動詞 + 主詞，符合這題要練習的重點！'; }
  } else if(q.checkType === 'notuntil'){
    if(!/\bnot\s+until\b/.test(lower)){ ok = false; msg = '這一題要練習 Not until…did I…，但沒有偵測到 not until，可以再試著說像 "Not until I got home did I notice my phone was gone." 這樣的句子。'; }
    else if(!/\bnot\s+until\b[^.?!]*?\b(?:did|do|does|had|have|has|was|were|could|would|will|can)\s+(?:i|you|he|she|we|they|it)\b/.test(lower)){ ok = false; msg = '偵測到 not until，但主要子句好像沒有倒裝。Not until 放句首時，後面要用「助動詞 + 主詞」，例如 did I notice。'; }
    else { msg = '偵測到 Not until…的倒裝句，符合這題要練習的重點！'; }
  } else if(q.checkType === 'cleft'){
    if(!/\bit\s+(?:is|was|'s)\b[^.?!]*\b(?:who|that)\b/.test(lower) && !/\bit's\b[^.?!]*\b(?:who|that)\b/.test(lower)){ ok = false; msg = '這一題要練習強調句 It was…who / that…，但沒有偵測到，可以再試著說像 "It was my grandmother who taught me to cook." 這樣的句子。'; }
    else { msg = '偵測到 It is / was…who / that…的強調句，符合這題要練習的重點！'; }
  } else if(q.checkType === 'whatis'){
    if(!/\b(?:what|all)\s+(?:i|we|you|he|she|they)\s+[a-z]+[^.?!]*?\b(?:is|was|are)\b/.test(lower)){ ok = false; msg = '這一題要練習 What I need is…，但沒有偵測到，可以再試著說像 "What I need most is a long holiday." 這樣的句子。'; }
    else { msg = '偵測到 What…is…的強調句，符合這題要練習的重點！'; }
  } else if(q.checkType === 'everyone'){
    if(!/\b(?:everyone|everybody|each|every\s+[a-z]+)\b/.test(lower)){ ok = false; msg = '這一題要練習 everyone / each / every 當主詞，但沒有偵測到，可以再試著說像 "Everyone in my family loves music." 這樣的句子。'; }
    else if(/\b(?:everyone|everybody)\b(?:\s+(?:in|at|of)\s+(?:my|our|the|this)\s+[a-z]+)?\s+(?:are|were|have|like|love|want|enjoy|play|go|eat|watch|need)\b/.test(lower)){ ok = false; msg = 'everyone / everybody 是單數，後面的動詞要用單數，例如 everyone is、everyone loves，可以再說一次。'; }
    else { msg = '偵測到 everyone / each / every 當主詞，符合這題要練習的重點！記得動詞用單數。'; }
  } else if(q.checkType === 'anumber'){
    if(!/\ba\s+number\s+of\b/.test(lower)){ ok = false; msg = '這一題要練習 A number of…，但沒有偵測到，可以再試著說像 "A number of my classmates play basketball." 這樣的句子。'; }
    else if(/\ba\s+number\s+of\s+[a-z' ]+?\b(?:is|was|has|plays|likes|goes|loves)\b/.test(lower)){ ok = false; msg = 'a number of 表示「很多」，動詞要用複數，例如 a number of students are / play，可以再說一次。'; }
    else { msg = '偵測到 a number of，符合這題要練習的重點！記得 a number of 後面用複數動詞。'; }
  } else if(q.checkType === 'theother'){
    if(!/\bthe\s+other\b/.test(lower)){ ok = false; msg = '這一題要練習 One…, and the other…，但沒有偵測到 the other，可以再試著說像 "One is reading, and the other is swimming." 這樣的句子。'; }
    else { msg = '偵測到 one…the other，符合這題要練習的重點！兩個中的另一個用 the other。'; }
  } else if(q.checkType === 'someothers'){
    if(!/\bsome\b[^.?!]*\b(?:others|the others)\b/.test(lower) && !/\bsome\b[^.]*[.;]\s*(?:others|the others)\b/.test(lower)){ ok = false; msg = '這一題要練習 Some…, others…，但沒有偵測到，可以再試著說像 "Some of my friends like rock music; others like pop." 這樣的句子。'; }
    else { msg = '偵測到 some…others，符合這題要練習的重點！'; }
  } else if(q.checkType === 'afew'){
    if(!/\b(?:a\s+few|few|a\s+little|little|each\s+other|one\s+another)\b/.test(lower)){ ok = false; msg = '這一題要練習 a few、few 或 each other，但沒有偵測到，可以再試著說像 "I have a few good friends, and we help each other." 這樣的句子。'; }
    else if(/\ba\s+little\s+(?:friends|books|people|students|questions|apples)\b/.test(lower)){ ok = false; msg = 'a little 只能接不可數名詞；可數名詞（例如 friends）要用 a few，可以再說一次。'; }
    else { msg = '偵測到 a few / few / each other 等限定詞或代名詞，符合這題要練習的重點！'; }
  } else if(q.checkType === 'reasonex'){
    const hasReason = /\b(?:because|since|the reason is|that's why|so that|so i)\b/.test(lower);
    const hasEx = /\b(?:for example|for instance|such as|last (?:week|weekend|saturday|sunday|month|year)|once)\b/.test(lower);
    if(!hasReason){ ok = false; msg = '這一題要用「回答 + 理由 + 例子」，但沒有偵測到理由（because…），可以再試著說像 "I like to go to the library on weekends because it is quiet." 這樣的句子。'; }
    else if(!hasEx){ ok = false; msg = '有偵測到理由，但沒有偵測到例子。可以再加一句 "For example, …" 讓回答更完整。'; }
    else { msg = '偵測到「理由 + 例子」的回答架構，符合英檢口說回答問題的要求！'; }
  } else if(q.checkType === 'describe'){
    const hasOpen = /\b(?:in this picture|this picture shows|in the picture|i can see|there (?:is|are))\b/.test(lower);
    const hasIng = /\b(?:am|is|are)\s+(?:[a-z]+\s+)?[a-z]+ing\b/.test(lower);
    if(!hasOpen){ ok = false; msg = '看圖敘述要先說地點或整體，例如 "In this picture, …" 或 "There are …"，可以再說一次。'; }
    else if(!hasIng){ ok = false; msg = '有偵測到開頭，但沒有偵測到人物正在做什麼（be + V-ing），可以再加一句像 "They are eating lunch." 這樣的句子。'; }
    else { msg = '偵測到「地點 + 人物動作」的看圖敘述架構，符合英檢口說的要求！可以再加上推測，例如 They seem to be happy。'; }
