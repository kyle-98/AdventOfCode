#!/usr/bin/python3

import numpy as np

infile = open("input.txt","r").read().strip().splitlines()

coordsMatrix = [[[int(k) for k in line.split(',')] for line in line2.split(' -> ')] for line2 in infile]


coordsMatrix = [data for data in coordsMatrix if data != []]

freq = [[0 for x in range(1000)] for y in range(1000)] 

for c in coordsMatrix:
    if c[0][0] == c[1][0] or c[0][1] == c[1][1]:
        continue
    else:
        c.clear()
coordsMatrix = [coord for coord in coordsMatrix if coord != []]

for c in coordsMatrix:
	if c[0][0] == c[1][0]:
		for i in range(abs(c[0][1] - c[1][1]) + 1):
			freq[c[0][0]][min(c[1][1], c[0][1]) + i] += 1
			
	elif c[0][1] == c[1][1]:
		for i in range(abs(c[0][0] - c[1][0]) + 1):
			freq[min(c[0][0], c[1][0]) + i][c[1][1]] += 1

total = 0
freq = np.rot90(np.fliplr(freq))
for row in freq:
	print(row)
	for i in row:
		if i >= 2:
			total += 1
print(sorted(coordsMatrix))
print("Total:",total)
