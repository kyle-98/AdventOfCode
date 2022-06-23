#!/usr/bin/python3

nums, letters, passwords = [], [], []

with open("input.txt", "r") as infile:
	for line in infile:
		parts = line.split(" ")
		parts[0] = parts[0].split("-")
		nums.append(parts[0])
		parts[1] = parts[1][0]
		letters.append(parts[1])
		parts[2] = parts[2].strip()
		passwords.append(parts[2])

count = 0
for c, letter in enumerate(letters):
	if passwords[c][int(nums[c][0]) - 1] == letter:
		if passwords[c][int(nums[c][1]) - 1] != letter:
			count += 1
	if passwords[c][int(nums[c][1]) - 1] == letter:
		if passwords[c][int(nums[c][0]) - 1] != letter:
			count += 1

print(count)