from collections import defaultdict
from itertools import product

with open('test_input.txt', 'r') as infile:
    data = [i.rstrip() for i in infile.readlines()]

input_dict = defaultdict(list)
for d in data:
    temp = d.split(':')
    input_dict[int(temp[0])] = [int(t) for t in temp[1].strip().split(' ')]

def eval_equation(equation):
    curr_number = ''
    ops = []
    for char in equation:
        if char.isdigit():
            curr_number += char
        elif char in '+*':
            if curr_number:
                ops.append((int(curr_number)))
                curr_number = ''
            ops.append(char)

    if curr_number:
        ops.append(int(curr_number))

    result = ops[0]
    i = 1
    while i < len(ops):
        curr_op = ops[i]
        opd = ops[i + 1]
        if curr_op == '+':
            result += opd
        elif curr_op == '*':
            result *= opd

        i += 2

    # print(result)
    return result

result = 0
for i in input_dict:
    num_pos = len(input_dict[i]) - 1
    ops_list = list(product(['*', '+'], repeat=num_pos))
    for op in ops_list:
        equation = ''.join(f"{input_dict[i][j]}{op[j]}" for j in range(num_pos)) + str(input_dict[i][-1])
        equation_result = eval_equation(equation)
        print(equation_result, i, equation)
        if equation_result == i:
            # print(equation, equation_result)
            result += i
            #break

print(result)
# print(input_dict)


# 3245122494055 > too low