#!/usr/bin/python3

with open("input.txt") as infile:
	for ages in infile:
		ages = ages.split(',')

for i in range(len(ages)):
	ages[i] = int(ages[i])

finalDay = False
day = 0
ageLimits = [0,0,0,0,0,0,0,0,0]

for a in ages:
	ageLimits[a] += 1

while not finalDay:
	if day == 256:
		finalDay == True
		break

	newFish = ageLimits.pop(0)
	ageLimits.append(newFish)
	ageLimits[6] += newFish
	day += 1
	
print("final:",sum(ageLimits))