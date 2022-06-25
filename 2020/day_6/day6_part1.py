
linesList = []
with open("input.txt", "r") as infile:
    for line in infile:
        linesList.append(list(line.split()))

tempMatrix = []
mainMatrix = []
count = True
for list in linesList:
    for i in list:
        tempMatrix.append(i)
    if list == []:
        count = False
    if count == False: 
        mainMatrix.append(tempMatrix)
        tempMatrix = []
        count = True
mainMatrix.append(tempMatrix)

sum = 0
for list in mainMatrix:
    questionsDict = {}
    for sublist in list:
        if len(sublist) > 1:
            for char in sublist:
                if char in questionsDict:
                    questionsDict[char] += 1
                else:
                    questionsDict[char] = 1 
        else:
            if sublist in questionsDict:
                questionsDict[sublist] += 1
            else:
                questionsDict[sublist] = 1
    sum += len(questionsDict.keys())

print(sum)