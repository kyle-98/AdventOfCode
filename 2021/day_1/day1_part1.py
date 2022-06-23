#!/usr/bin/python3

#----------
#Part 1
#----------

infile = open("depths.txt")
count = 0
dl = infile.read().splitlines()

print(dl[0],"N/A - no previous measurement")
for i in range(1,len(dl)):
	if int(dl[i - 1]) < int(dl[i]):
		count += 1
		print(dl[i], "Increased", count)
	else:
		print(dl[i], "Decreased", count)

print("Final count =",count)
