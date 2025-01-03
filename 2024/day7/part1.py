from collections import defaultdict
from itertools import product

with open('input.txt', 'r') as infile:
    data = [i.rstrip() for i in infile.readlines()]

input_dict = defaultdict(list)
for d in data:
    temp = d.split(':')
    input_dict[int(temp[0])] = [int(t) for t in temp[1].strip().split(' ')]

def eval_equation(equation):
    curr_number = ''
    curr_op = ''
    result = 0
    for c, e in enumerate(equation):
        if e.isnumeric():
            curr_number += e
        else:
            # print('OP', curr_op, result, curr_number)
            if result == 0:
                result = int(curr_number)
                curr_number = ''
                curr_op = e
            else:
                if curr_op == '+':
                    result += int(curr_number)
                elif curr_op == '*':
                    result *= int(curr_number) 
                curr_number = ''
                curr_op = e
        if c == len(equation) - 1:
            if curr_op == '+':
                result += int(curr_number)
            elif curr_op == '*':
                result *= int(curr_number)
    return result
    # print(result)

result = 0
for i in input_dict:
    num_pos = len(input_dict[i]) - 1
    ops_list = list(product(['*', '+'], repeat=num_pos))
    for op in ops_list:
        equation = ''.join(f"{input_dict[i][j]}{op[j]}" for j in range(num_pos)) + str(input_dict[i][-1])
        equation_result = eval_equation(equation)
        if equation_result == i:
            # print(equation, equation_result)
            result += i
            break

print(result)
# print(input_dict)