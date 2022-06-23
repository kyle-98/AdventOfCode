#!/usr/bin/python3

linesList = []
TARGET = 2020

with open("input.txt", 'r') as infile:
	lines = infile.readlines()
	for line in lines:
		l = line.rstrip("\n")	
		linesList.append(int(l))
#print(linesList)

for i, num in enumerate(linesList[:-1]):
	comp = TARGET - num
	if(comp in linesList[i + 1:]):
		ans = num * comp

print(ans)
	
