DEBUG = False

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    numbers = []
    instructions = []
    for d in data:
        split_data = [x for x in d.split(' ') if x != '']
        if split_data[0] in ['+', '*']:
            instructions.append(split_data)
        else:
            numbers.append([int(val) for val in split_data])

    instructions = instructions[0]
    total_value = 0
    for idx, operation in enumerate(instructions):
        if operation == '+':
            column_value = 0
        else:
            column_value = 1

        for number_row in numbers:
            if DEBUG:
                print('Column Index: ', idx)
                print('Column Value: ', number_row[idx])
                print(number_row)
            if operation == '+':
                column_value += number_row[idx]
                if DEBUG:
                    print('Adding: ', column_value)
            elif operation == '*':
                column_value *= number_row[idx]
                if DEBUG:
                    print('Multiplying: ', column_value)

        total_value += column_value

    print(total_value)