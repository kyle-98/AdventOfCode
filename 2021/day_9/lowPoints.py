#!/usr/bin/python3

gridMatrix = []

with open("input.txt", "r") as infile:
	gridMatrix = [[int(height) for height in line.rstrip()] for line in infile]

def adjacentLocations(x, y):
	adjLocs = []
	if x > 0:
		adjLocs.append((x - 1, y))
	if x < len(gridMatrix[0]) - 1:
		adjLocs.append((x + 1, y))
	
	if y > 0:
		adjLocs.append((x, y - 1))
	if y < len(gridMatrix) - 1:
		adjLocs.append((x, y + 1))
	return adjLocs
#print(adjacent_locations(1,2))

def isLowPoint(x, y):
	height = gridMatrix[y][x]
	adjLocs = adjacentLocations(x, y)
	
	for location in adjLocs:
		x, y = location
		if height >= gridMatrix[y][x]:
			return False
	return True

riskSum, riskLevel = 0, 0
lowPoints = []

for y, line in enumerate(gridMatrix):
#	print("y=",y)
	for x, height in enumerate(line):
#		print("x=",x)
		if isLowPoint(x, y):
			lowPoints.append((x, y))
			riskLevel = height + 1
			riskSum += riskLevel

#print(len(gridMatrix[0]))
print("Total Risk:",riskSum)

#print(grid)
