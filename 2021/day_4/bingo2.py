#!/usr/bin/python3


bingoMatrix=[]

flag = False
with open('input.txt','r')as infile:
    c = 0
    flag = False
    board = []
    for line in infile:
        line = line.rstrip()
        if not flag:
            line = line.rstrip()
            draw = line.split(',')
            flag = True
            continue


        if len(line) == 0:
            c = 0
            #print("test")
            continue
        else:
            board.append(line.split())
        if c == 4:
            bingoMatrix.append(board)
            board = []
            c = 0
        c += 1


winner = False
winningBoard = []

for i in draw:
    if winner:
        break
    for card in bingoMatrix:
        if not card:
            continue
        for line in card:
            for j in range(len(line)):
                if line[j] == i:
                    line[j] = "x"
    counter = -1
    for card in bingoMatrix:
        counter += 1
        if not bingoMatrix[counter]:
            continue
        for line in card:
            if line == ["x", "x", "x", "x", "x"]:
                bingoMatrix[counter].clear()
                winningNum = i

        if not bingoMatrix[counter]:
            continue

        for x in range(5):
            if (card[0][x] == "x" and card[1][x] == "x" and card[2][x] == "x"  and card[3][x] == "x"  and card[4][x] == "x"):
                bingoMatrix[counter].clear() 
                winningNum = i
                break
    j = 0
    for card in bingoMatrix:
    	if len(card) > 0:
    		j += 1
    		lastCard = card
    if j == 1:
    	break

winner = False
card = lastCard
winningBoard = []

for i in draw:
	if winner:
		break
	
	for line in card:
		for j in range(len(line)):
			if line[j] == i:
				line[j] = "x"
	for line in card:
		if line == ["x", "x", "x", "x", "x"]:
			if card not in winningBoard:
				winningBoard.append(card)
				winner = True
				winningNum = i
	
	for x in range(5):
		if (card[0][x] == "x" and card[1][x] == "x" and card[2][x] == "x"  and card[3][x] == "x"  and card[4][x] == "x"):
			if card not in winningBoard:
				winningBoard.append(card)
				winner = True
				winningNum = i


print(card)
print(winningNum)
Sum = 0
for row in card:
    for column in row:
        if column.isnumeric():
            Sum += int(column)
print(Sum)
print(Sum * int(winningNum))