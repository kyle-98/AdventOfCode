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

pointsArr = []

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

print("Final Syntax Error Score:",sum(pointsArr))