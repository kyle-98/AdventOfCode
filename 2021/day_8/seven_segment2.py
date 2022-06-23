#!/usr/bin/python3

uniqueNums = []
output = []

with open('input.txt','r')as infile:
	for line in infile: 
		line = line.split(" | ")[0].rstrip("\n")
		uniqueNums.append(line)

with open('input.txt', 'r') as infile:
	for line in infile:
		line = line.split(" | ")[1].rstrip("\n")
		output.append(line)

def subNumCheck(subNum, newNum):
	return all(part in newNum for part in subNum)


def partsUndo(part, unknown):
	temp = unknown[0:]
	for characters in part:
		if characters in temp:
			temp.remove(characters)
#	print(temp)
	return temp

def partsCombine(part, unknown):
	temp = unknown[0:]
	for characters in part:
		if characters not in temp:
			temp.append(characters)
#	print(temp)
	return sorted(temp)

answer = 0
for i in range(len(uniqueNums)):
	unknownMatrix = [sorted(parts) for parts in uniqueNums[i].split()]
	knownMatrix = [""] * 10
	outputSort = [sorted(parts) for parts in output[i].split()]

	for part in unknownMatrix:
		if len(part) == 2:
			knownMatrix[1] = part
		elif len(part) == 3:
			knownMatrix[7] = part
		elif len(part) == 4:
			knownMatrix[4] = part
		elif len(part) == 7:
			knownMatrix[8] = part

	for part in unknownMatrix:
		if len(part) == 5:
			if subNumCheck(knownMatrix[1], part):
				knownMatrix[3] = part
			elif subNumCheck(partsUndo(knownMatrix[1], knownMatrix[4]), part):
				knownMatrix[5] = part
			else:
				knownMatrix[2] = part
	#print(knownMatrix[5])
	knownMatrix[9] = partsCombine(knownMatrix[1], knownMatrix[5])
	knownMatrix[6] = partsCombine(partsUndo(knownMatrix[1], knownMatrix[8]), knownMatrix[5])

	for part in unknownMatrix:
		if part not in knownMatrix:
			knownMatrix[0] = part

	temp = ""
	for part in outputSort:
		temp += str(knownMatrix.index(part))
		print(temp)
	answer += int(temp)

print("answer:",answer)