s = '君不見黃河之水天上來，奔流到海不復迴。\
君不見高堂明鏡悲白髮，朝如青絲暮成雪。\
人生得意須盡歡，莫使金樽空對月。\
天生我材必有用，千金散盡還復來。\
烹羊宰牛且為樂，會須一飲三百杯。\
岑夫子，丹丘生。將進酒，君莫停。\
與君歌一曲，請君為我側耳聽。\
鐘鼓饌玉不足貴，但願長醉不願醒。\
古來聖賢皆寂寞，惟有飲者留其名。\
陳王昔時宴平樂，斗酒十千恣讙謔。\
主人何為言少錢，徑須沽取對君酌。五花馬，千金裘。\
呼兒將出換美酒，與爾同銷萬古愁。'    #將進酒  李白
dic = {w:s.count(w) for w in set(s) if w != '，' and w != '。' and s.count(w) > 2}
print(dic)
dic2 = {k:v for k,v in dic.items() if v ==3}
print(dic2)