if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    STARTING_POS = 50
    MAX_POS = 99
    MIN_POS = 0

    curr_pos = STARTING_POS
    zero_count = 0
    for instruction in data:
        operation = instruction[:1]
        rotations = int(instruction[1:])

        if operation == 'L':
            for _ in range(1, rotations + 1):
                if curr_pos == MIN_POS:
                    curr_pos = MAX_POS + 1
                curr_pos -= 1
                if curr_pos == MIN_POS:
                    zero_count += 1
        else:
            for _ in range(1, rotations + 1):
                if curr_pos == MAX_POS:
                    curr_pos = MIN_POS - 1
                curr_pos += 1
                if curr_pos == MIN_POS:
                    zero_count += 1

    print(f'Number of times hitting 0: {zero_count}')