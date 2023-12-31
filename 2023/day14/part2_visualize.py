import numpy as np
import time
import curses

def display_data(stdscr, arr):
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val == 'O':
                color = curses.color_pair(1)
            elif val == '.':
                color = curses.color_pair(2)
            else:
                color = curses.color_pair(3)
            stdscr.addstr(i, j * 4, str(val), color)


def main(stdscr):
    with open('test_input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    
    rock_coords = np.argwhere(data == 'O')
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # north
    for rock in rock_coords:
        index = rock[0]
        while True:
            if data[index - 1, rock[1]] in ['O', '#'] or index <= 0:
                break
            else:
                data[index - 1, rock[1]] = 'O'
                data[index, rock[1]] = '.'
                index -= 1
        display_data(stdscr, data)
        stdscr.refresh()
        time.sleep(0.1)

    # west
    rock_coords = np.argwhere(data == 'O')
    rock_coords = rock_coords[rock_coords[:, 1].argsort()]
    for rock in rock_coords:
        index = rock[1]
        while True:
            if data[rock[0], index - 1] in ['O', '#'] or index <= 0:
                break
            else:
                # stdscr.addstr(str(rock) + ' ' + str([rock[0], index - 1]))
                # stdscr.refresh()
                data[rock[0], index - 1] = 'O'
                data[rock[0], index] = '.'
                index -= 1     
        display_data(stdscr, data)
        stdscr.refresh()
        time.sleep(0.1)

    
    rock_coords = np.argwhere(data == 'O')
    rock_coords = rock_coords[rock_coords[:, 0].argsort()[::-1]]
    # south
    for rock in rock_coords:
        index = rock[0]
        while index < len(data) - 1:
            if data[index + 1, rock[1]] in ['O', '#'] or index > len(data) - 1:
                break
            else:
                data[index + 1, rock[1]] = 'O'
                data[index, rock[1]] = '.'
                index += 1       
        display_data(stdscr, data)
        stdscr.refresh()
        time.sleep(0.1)
    
    # east
    rock_coords = np.argwhere(data == 'O')
    rock_coords = rock_coords[rock_coords[:, 1].argsort()[::-1]]
    for rock in rock_coords:
        index = rock[1]
        while index < len(data[0]) - 1:
            if data[rock[0], index + 1] in ['O', '#'] or index >= len(data[0]) - 1:
                break
            else:
                data[rock[0], index + 1] = 'O'
                data[rock[0], index] = '.'
                index += 1 
        display_data(stdscr, data)
        stdscr.refresh()
        time.sleep(0.1)

    height = len(data)
    rock_load = 0
    for row in data:
        rock_load += len((np.argwhere(row == 'O'))) * height
        height -= 1

    # print(data)

    stdscr.getch()
    # curses.endwin()
    # print(rock_coords)
    # stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)