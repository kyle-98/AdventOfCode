#!/usr/bin/python3
import re 

linesList, tempMatrix, mainMatrix = [], [], []
with open("input.txt", "r") as infile:
    for line in infile:
        linesList.append(list(line.split()))

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

mainCount, c2 = 0, 0
regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
for m in mainMatrix:
    m.sort(key=lambda x: x[0])
    for element in m:
        if element.startswith("byr") and int(element[4:]) >= 1920 and int(element[4:]) <= 2002:
            c2 += 1
        if element.startswith("iyr") and int(element[4:]) >= 2010 and int(element[4:]) <= 2020:
            c2 += 1
        if element.startswith("eyr") and int(element[4:]) >= 2020 and int(element[4:]) <= 2030:
            c2 += 1
        if element.startswith("hgt") and element[-2:] == "in" and int(element[4:-2:]) >= 59 and int(element[4:-2:]) <= 76:
            c2 += 1
        if element.startswith("hgt") and element[-2:] == "cm" and int(element[4:-2:]) >= 150 and int(element[4:-2:]) <= 193:
            c2 += 1
        if element.startswith("hcl") and re.search(regex, element[4:]):
            c2 += 1
        if element.startswith("ecl") and (element[4:] == "amb" or element[4:] == "blu" or element[4:] == "brn" or element[4:] == "gry" or element[4:] == "grn" or element[4:] == "hzl" or element[4:] == "oth"):
            c2 += 1
        if element.startswith("pid") and len(element[4:]) == 9:
            c2 += 1
    if c2 == 7:
        mainCount += 1
    c2 = 0 

print(mainCount)
#print(mainMatrix)