with open('input.txt', 'r') as infile:
    operations = [line.rstrip() for line in infile]

cycle_counter = 0
x_value = 1
signal_list = []
for op in operations:
    flag = 0
    if op.startswith('n'):
        flag = 1
    else:
        flag = 2
    for i in range(flag):
        cycle_counter += 1
        if cycle_counter == 20 or cycle_counter % 40 == 20:
            signal_list.append(cycle_counter * x_value)
    if flag == 2:
        x_value += int(op.split()[1])

    

print(f'\nCC: {cycle_counter}', f'\nX: {x_value}', f'\nSS: {sum(signal_list)}')
