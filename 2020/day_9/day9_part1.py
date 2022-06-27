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
        print(numbers[c + PREAMBLE])
        break