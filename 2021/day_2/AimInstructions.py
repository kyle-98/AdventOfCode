#!/usr/bin/python3

infile = open("instructions.txt")
dl = infile.read().splitlines()
x = 0
y = 0
aim = 0

for i in range(len(dl)):
	if "forward" in dl[i]:
		x += int(dl[i][len(dl[i]) - 1])
		if(aim > 0):
			y += aim * int(dl[i][len(dl[i]) - 1])
	elif "up" in dl[i]:
		aim -= int(dl[i][len(dl[i]) - 1])
	else:
		aim += int(dl[i][len(dl[i]) - 1])
	print("x=",x, "aim=",aim, "y=",y)
print("x=",x, "aim=",aim, "y=",y)
print(x * y)