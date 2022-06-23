#!/usr/bin/python3

linesList = []
with open("input.txt", "r") as infile:
    for line in infile:
        linesList.append(list(line.split()))

tempMatrix = []
mainMatrix = []
count = 0
for list in linesList:
    for i in list:
        tempMatrix.append(i)
    if list == []:
        count = -1
    if count == -1: 
        mainMatrix.append(tempMatrix)
        tempMatrix = []
        count = 0
mainMatrix.append(tempMatrix)
    
c2, mainCount = 0, 0
bool = ""
subList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for m in mainMatrix:
    for s in subList:
        bool = any(s in x for x in m)
        if bool == True:
            c2 += 1
    if c2 == 7:
        mainCount += 1
        c2 = 0
    c2 = 0
    
print(mainCount)
#print(mainMatrix)
