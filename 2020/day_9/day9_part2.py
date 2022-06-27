import itertools

preambleList, validNums, numbers = [], [], []
with open("input.txt", "r") as infile:
    for line in infile:
        part = line.rstrip()
        numbers.append(int(part))

PREAMBLE = 25
count = 0

for c in range(PREAMBLE):
    preambleList.append(numbers[c])

for c in range(PREAMBLE, len(numbers)):
    for nums in itertools.combinations(preambleList, 2):
        if sum(nums) == numbers[c]:
            preambleList.pop(0)
            preambleList.append(numbers[c])
            validNums.append(numbers[c])
            break

for c in range(len(validNums)):
    if numbers[c + PREAMBLE] != validNums[c]:
        invalidNum = numbers[c + PREAMBLE]
        break

contiguousNums, longLenList, cList = [], [], []
Sum, c1, c2, longLen = 0, 0, 0, 0
while(c2 < len(numbers)):
    if numbers[c1] < invalidNum and Sum + numbers[c1] <= invalidNum:
        contiguousNums.append(numbers[c1])
        Sum += numbers[c1]
        c1 += 1
    else:
        if sum(contiguousNums) == invalidNum:
            if longLen < len(contiguousNums):
                longLen = len(contiguousNums)
                longLenList.append(longLen)
                cList.append(contiguousNums)
        contiguousNums = []
        Sum = 0
        c2 += 1
        c1 = c2

cList.sort(key=len, reverse=True)
print(f"Longest Contiguous List: {cList[0]}\n Final Sum: {min(cList[0]) + max(cList[0])}")