#!/usr/bin/python3

infile = open("instructions.txt")
dl = infile.read().splitlines()
x = 0
y = 0

for i in range(len(dl)):
	if "forward" in dl[i]:
		x += int(dl[i][len(dl[i]) - 1])
		print("x =",x)
	elif "up" in dl[i]:
		y -= int(dl[i][len(dl[i]) - 1])
		print("y=",y)
	else:
		y += int(dl[i][len(dl[i]) - 1])
		print("y=",y)

print("x =",x, "y=",y)
print(x * y)
