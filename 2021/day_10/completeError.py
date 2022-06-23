#!/usr/bin/python3

with open("input.txt") as infile:
	syntaxArr = infile.read().strip().split("\n")

print(syntaxArr)

syntaxPairs = {
	"(" : ")", 
	"[" : "]", 
	"{" : "}",
	"<" : ">"
}

illegalChars = [")", "]", "}", ">"]

illegalPoints = {
	")" : 3,
	"]" : 57,
	"}" : 1197,
	">" : 25137
}

completePoints ={
	")" : 1,
	"]" : 2,
	"}" : 3,
	">" : 4
}

pointsArr = []
completeArr = []

for incomplete in syntaxArr:
	errorScore = 0
	illegalsFound = []

	for char in incomplete:
		if char not in illegalChars:
			illegalsFound.append(char)
		else:
			if char == syntaxPairs[illegalsFound[-1]]:
				illegalsFound.pop()
			else:
				pointsArr.append(illegalPoints[char])
				illegalsFound = []
				break
	if illegalsFound:
		for i in [syntaxPairs[j] for j in illegalsFound[::-1]]:
			errorScore = (errorScore * 5) + completePoints[i]
		completeArr.append(errorScore)

print("Final Score:",sorted(completeArr)[len(completeArr) // 2])