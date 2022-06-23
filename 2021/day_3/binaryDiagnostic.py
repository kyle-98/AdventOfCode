#!/usr/bin/python3

#bl = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def binDiag(binList, gamma, epsilon):
	bits = {"0" : 0, "1" : 0}
	if len(binList[0]) == 0:
		print("gamma=",gamma,"epsilon=",epsilon)
		print(int(gamma, 2) * int(epsilon, 2))
	
	elif(len(binList[0]) == 1):
		for i in range(len(binList)):
			if "0" in binList[i]:
				if("0" in bits):
					bits["0"] += 1
				else:
					bits["0"] = 1
			else:
				if("1" in bits):
					bits["1"] += 1
				else:
					bits["1"] = 1
		if bits["0"] > bits["1"]:
			gamma = "0" + gamma
			epsilon = "1" + epsilon 
		else:
			gamma = "1" + gamma
			epsilon = "0" + epsilon
		for x in range(len(binList)):
			binList.append(binList[x][:0])
		for z in range(len(binList) - 1):
			binList.pop(0)
		
		return (binDiag(binList, gamma, epsilon))


	else:
		for i in range(len(binList)):
			if "0" in binList[i][len(binList[i]) - 1]:
				if("0" in bits):
					bits["0"] += 1
				else:
					bits["0"] = 1
			else:
				if("1" in bits):
					bits["1"] += 1
				else:
					bits["1"] = 1
		if bits["0"] > bits["1"]:
			gamma = "0" + gamma
			epsilon = "1" + epsilon 
		else:
			gamma = "1" + gamma
			epsilon = "0" + epsilon	

		for x in range(len(binList)):
			binList.append(binList[x][:len(binList[x]) - 1])

		for z in range(len(binList) // 2):
			binList.pop(0)
		return (binDiag(binList, gamma, epsilon))
		

	
infile = open("input.txt")
bl = infile.read().splitlines()
g = ""
e = ""

print(binDiag(bl, g, e))