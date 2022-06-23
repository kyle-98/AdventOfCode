#!/usr/bin/python3

from itertools import combinations

linesList = []

with open("input.txt", "r") as infile:
	lines = infile.readlines()
	for line in lines:
		l = line.rstrip("\n")	
		linesList.append(int(l))
#print(linesList)

for x, num in enumerate(list(combinations(linesList, 3))):
	if sum(num) == 2020:
		correctNums = num
	
ans = 1	
for num in correctNums:
	ans *= num

print(ans)