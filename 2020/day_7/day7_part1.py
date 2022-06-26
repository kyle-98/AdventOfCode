
instructions, instructNums = [], []

with open("input.txt", "r") as infile:
    for line in infile:
        iPart = line[:3].rstrip()
        numPart = line[4:].rstrip()
        instructions.append(iPart)
        instructNums.append(numPart)

checkedInstruct = [0] * len(instructions)
accumulator, count = 0, 0

while(True):   
    if checkedInstruct[count] == 1:
        break

    if instructions[count] == "acc":
        if instructNums[count][0] == "+":
            checkedInstruct[count] = 1
            accumulator += int(instructNums[count][1:])
        else:
            checkedInstruct[count] = 1
            accumulator -= int(instructNums[count][1:]) 
        count += 1     
    
    if instructions[count] == "jmp":
        if instructNums[count][0] == "+":
            checkedInstruct[count] = 1
            count += int(instructNums[count][1:])
        else:
            checkedInstruct[count] = 1
            count -= int(instructNums[count][1:])

    if instructions[count] ==  "nop":
        checkedInstruct[count] = 1
        count += 1
    
print(accumulator)