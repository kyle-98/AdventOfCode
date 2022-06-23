#!/usr/bin/python3

with open("input.txt") as infile:
	for ages in infile:
		ages = ages.split(',')

for i in range(len(ages)):
	ages[i] = int(ages[i])

finalDay = False
day = 0

while not finalDay:
	if day == 80:
		finalDay == True
		break

	for i in range(len(ages)):	
		if ages[i] == 0:
			ages[i] += 6
			ages.append(8)
		else:
			ages[i] -= 1
	day += 1
	print("Day:",day)
	print(len(ages))

print("final:",len(ages))



