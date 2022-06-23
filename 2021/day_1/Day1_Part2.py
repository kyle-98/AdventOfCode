#!/usr/bin/python3

count = 0

#dl = [199,200,208,210,200,207,240,269,260,263]
dl = [int(n) for n in open("depths.txt", "r")]

for i in range(len(dl) - 3):
	r = sum(dl[i + 1:i + 4])
	l = sum(dl[i:i + 3])
	if l < r:
		count += 1


print("Final count =",count)
