from collections import deque

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as infile:
    count = 0
    for line in infile:
        if '[' not in line:
            NUMBER_OF_CRATES = int(line.strip().split(' ')[len(line.strip().split(' ')) - 1])
            CRATE_COUNT_LINES = count
            break
        count += 1
infile.close()

def move_crates(num_crates, start_stack, dest_stack):
    temp_list = []
    for x in range(num_crates):
        length = len(start_stack) - 1
        temp_list.append(start_stack[length])
        start_stack.pop()

    temp_list.reverse()
    for y in temp_list:
        dest_stack.append(y)


    for c in range(num_crates):
        length = len(start_stack) - 1
        #dest_stack.append(start_stack[length])
        #start_stack.pop()

with open(INPUT_FILE, 'r') as infile:
    main_count = 0
    count = 0
    crates_list = []
    stuff_list = []
    list_of_stacks = []

    for c, line in enumerate(infile):
        if c >= CRATE_COUNT_LINES:
            break
        else:
            #print(line.replace(' ', '.').replace('..', '.').replace('[', '').replace(']', '').rstrip())
            crates_list.append(line.replace(' ', '.').replace('..', '.').replace('[', '').replace(']', '').rstrip())

    #print(crates_list)
    while True:

        if main_count >= NUMBER_OF_CRATES * 2:
            break
        else:
            y = []
            for entry in crates_list:
                if entry[main_count] != '.':
                    y.append(entry[main_count])
                count += 1
            y.reverse()
            stuff_list.append(y)
        main_count += 2

infile.close()

for things in stuff_list:
    stack = deque()
    for t in things:
        stack.append(t)
    list_of_stacks.append(stack)


with open(INPUT_FILE, 'r') as infile:
    count_lines = 0
    temp = []
    t = []
    for line in infile:
        #done reading stack inputs?
        #done        
        if count_lines > CRATE_COUNT_LINES + 1:
            instruct = line.rstrip().split(' ')
            move_crates(int(instruct[1]), list_of_stacks[int(instruct[3]) - 1], list_of_stacks[int(instruct[5]) - 1])
        count_lines += 1

ans = ''
for s in list_of_stacks:
    ans += s[len(s) - 1]

print(ans)