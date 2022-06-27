
instructions = []

with open("input.txt", "r") as infile:
    for line in infile:
        iPart = line[:3].rstrip()
        numPart = line[4:].rstrip()
        instructions.append((iPart, numPart))


def executeCode(i):
    accumulator, index = 0, 0
    infiniteLoop = False
    checkedInstruct = set()
    while index < len(i):
        op, arg = i[index]

        if index in checkedInstruct:
            infiniteLoop = True
            break
        checkedInstruct.add(index)

        if op == "jmp":
            index += int(arg)
            continue

        elif op == "acc":
            accumulator += int(arg)
        
        index += 1
    
    return(accumulator, infiniteLoop)

changeOperation = {'nop':'jmp', 'jmp':'nop'}
for i, (op, arg) in enumerate(instructions):
    
    if op == "nop" or op == "jmp":
        changedOperation = [(changeOperation[op], arg)]
        newInstructions = instructions[:i] + changedOperation + instructions[i + 1:]
        accumulator, infiniteLoop = executeCode(newInstructions)
        
        if not infiniteLoop:
            print("Accumulator:",accumulator)
