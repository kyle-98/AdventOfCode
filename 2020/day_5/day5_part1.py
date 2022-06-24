#!/usr/bin/python3

seatList = []

with open("input.txt", "r") as infile:
    for line in infile:
        data = line.rstrip()
        seatList.append(data)

ROW, COLUMN = 0, 0
seatID = 0
seatIDList = []

for seat in seatList:
    FRONT_ROW = 0
    BACK_ROW = 127
    FRONT_COLUMN = 0
    BACK_COLUMN = 7
    for row in range(7):
        if seat[row] == "B":
            FRONT_ROW = BACK_ROW - abs(FRONT_ROW - BACK_ROW) // 2
        else:
            BACK_ROW = FRONT_ROW + abs(FRONT_ROW - BACK_ROW) // 2
    for column in range(7, 10):
        if seat[column] == "R":
            FRONT_COLUMN = BACK_COLUMN - abs(FRONT_COLUMN - BACK_COLUMN) // 2
        else:
            BACK_COLUMN = FRONT_COLUMN + abs(FRONT_COLUMN - BACK_COLUMN) // 2
        
    ROW = FRONT_ROW
    COLUMN = FRONT_COLUMN
    seatID = (ROW * 8) + COLUMN
    seatIDList.append(seatID)

seatIDList.sort(reverse=True)
print(seatIDList[0])