#!/usr/bin/python3
infile = open("input.txt")
bl = infile.read().splitlines()

infile2 = open("input.txt")
bl2 = infile2.read().splitlines()


def oxygenRating(binList, oxygen, n):
	bits = {"0" : 0, "1" : 0}
	if len(binList) == 1:
		oxygen = binList[0]
		return int(oxygen, 2)

	else:
		if n == 8:
			n == 7
		for i in range(len(binList)):
			if "0" in binList[i][n]:
				if("0" in bits):
					bits["0"] += 1
				else:
					bits["0"] = 1
			else:
				if("1" in bits):
					bits["1"] += 1
				else:
					bits["1"] = 1
		if bits["0"] == bits["1"]:
			for x in range(len(binList)):
				if "0" in binList[x][n]:
					binList[x] = "R"
		elif bits["0"] > bits["1"]:
			for j in range(len(binList)):
				if binList[j][n] == "1":
					binList[j] = "R"
		else:
			for j in range(len(binList)):
				if binList[j][n] == "0":
					binList[j] = "R"
		
		binList = list(filter(lambda a: a != "R", binList))
		return (oxygenRating(binList, oxygen, n + 1))

def co2Rating(binList, co2, n):
	bits = {"0" : 0, "1" : 0}
	if len(binList) == 1:
		co2 = binList[0]
		return int(co2, 2)

	else:
		if n == 8:
			n == 7
		for i in range(len(binList)):
			if "0" in binList[i][n]:
				if("0" in bits):
					bits["0"] += 1
				else:
					bits["0"] = 1
			else:
				if("1" in bits):
					bits["1"] += 1
				else:
					bits["1"] = 1
		if bits["0"] == bits["1"]:
			for x in range(len(binList)):
				if "1" in binList[x][n]:
					binList[x] = "R"
		elif bits["0"] > bits["1"]:
			for j in range(len(binList)):
				if binList[j][n] == "0":
					binList[j] = "R"
		else:
			for j in range(len(binList)):
				if binList[j][n] == "1":
					binList[j] = "R"
		
		binList = list(filter(lambda a: a != "R", binList))
		return (co2Rating(binList, co2, n + 1))

o = ""
c = ""
n = 0
print(oxygenRating(bl, o, n))
print(co2Rating(bl2, c, n))
print("Final Answer =",oxygenRating(bl, o, n) * co2Rating(bl2, c, n))