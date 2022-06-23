#!/usr/bin/python3

matrix = []

with open('input.txt','r')as infile:
	for line in infile: 
		line = line.rstrip()
		line = line.split(" ")
		matrix.append(line[11:])

matrix = [array for array in matrix if len(array) != 11]

for i in matrix:
	print(i)

def lettersConvert(L):
    dict_letter = { 2 : 1, 4 : 4, 3 : 7, 7 : 8 }
    
    if L in dict_letter:
        return dict_letter.get(L)
    else:
        return 0

finalNums = []
for i in matrix:
	for x in range(len(i)):
		finalNums.append(lettersConvert(len(i[x])))

finalNums = [zeros for zeros in finalNums if zeros != 0]

print(len(finalNums))