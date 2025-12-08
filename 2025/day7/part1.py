import numpy as np
from curses import wrapper
import time

DEBUG = False

def main(stdscr):
    stdscr.clear()
    with open('input.txt', 'r') as f:
        data_array = np.array([[char for char in row] for row in [line.strip() for line in f]])

    STARTING_VALUE = 'S'

    starting_coords = np.where(data_array == STARTING_VALUE)
    start_row, start_column = list(zip(starting_coords[0], starting_coords[1]))[0]

    rows, columns = data_array.shape

    data_array_mask = data_array.copy() # visualization

    current_row = start_row
    current_col = start_column
    is_splitting = False
    split_starts = set()
    total_split_count = 0
    previous_starts = set()
    split_coords = []

    while True:
        current_row += 1

        if current_row >= rows:
            is_splitting = True

        if is_splitting:
            if len(split_starts) == 0:
                break
            for split_start in split_starts:
                current_row = split_start[0]
                current_col = split_start[1]
                break
            split_starts.remove((current_row, current_col))
            previous_starts.add((current_row, current_col))
            is_splitting = False

        # Split the beam to the left and right of the ^
        if data_array_mask[current_row, current_col] == '^':
            if current_col + 1 < columns and data_array_mask[current_row, current_col + 1] == '.':
                data_array_mask[current_row, current_col + 1] = 'x'
                if (current_row, current_col + 1) not in previous_starts:
                    split_starts.add((current_row, current_col + 1))
            if current_col - 1 >= 0 and data_array_mask[current_row, current_col - 1] == '.':
                data_array_mask[current_row, current_col - 1] = 'x'
                if (current_row, current_col - 1) not in previous_starts:
                    split_starts.add((current_row, current_col - 1))
            is_splitting = True
            total_split_count += 1
            if DEBUG:
                stdscr.addstr(0, 0, ' ' * 200)
                stdscr.addstr(1, 0, ' ' * 200)
                stdscr.addstr(0, 0, ' | '.join([f'{split_start}' for split_start in split_starts]))
                stdscr.addstr(1, 0, str(total_split_count) + '\t' + f'Splitting At: {current_row}, {current_col}')
                split_coords.append((current_row, current_col))
                stdscr.refresh()

        elif data_array_mask[current_row, current_col] == '.':
            data_array_mask[current_row, current_col] = 'x'

        if current_row + 1 < rows:
            if data_array_mask[current_row + 1, current_col] == 'x':
                current_row = rows

        if DEBUG:
            stdscr.addstr(3, 0, '\n'.join([''.join(i) for i in data_array_mask]))
            stdscr.refresh()
            time.sleep(0.2)
    
    stdscr.addstr(0, 0, ' ' * 200)
    stdscr.addstr(0, 0, 'DONE.')
    stdscr.getch()

    if DEBUG:
        print(data_array_mask)
        print(split_coords)
    # print(split_starts)
    print('Total Split Count: ', total_split_count)
    return data_array_mask


if __name__ == '__main__':
    data = wrapper(main)

    # print(data)




# 1839 > Too High
# 1275 > Too Low