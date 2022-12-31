import numpy as np
import curses
from curses import wrapper
import time

data = [line.rstrip() for line in open('test_input2.txt')]
coords_lists = [d.split(' -> ') for d in data]

max_width = 0
min_width = 500
max_depth = 0
for coord in coords_lists:
    for c in coord:
        curr_height = int(c.split(',')[0])
        curr_depth = int(c.split(',')[1])
        if curr_height > max_width:
            max_width = curr_height
        if curr_height < min_width:
            min_width = curr_height
        if curr_depth > max_depth:
            max_depth = curr_depth
cave = np.full((max_depth + 1, (max_width + 1) - min_width), '.')
cave[0][499 - max_width] = '+'
for coord in coords_lists:
    prev_x = 0
    prev_y = 0
    for c in coord:
        x = int(c.split(',')[0])
        y = int(c.split(',')[1])
        if prev_x == x:
            for i in range(prev_y + 1, y + 1):
                cave[i][(x - 1) - max_width] = '#'
        if prev_y == y:
            for i in range(min(prev_x, x), max(prev_x, x)):
                cave[y][(i - 1) - max_width] = '#'
        cave[y][(x - 1) - max_width] = '#'
        prev_x = x
        prev_y = y


def display(stdscr):
    count = 0
    sand_moving = True
    sand_complete = True
    stdscr.clear()
    
    while(sand_complete):
        curr_y = np.where(cave == '+')[0][0] + 1
        curr_x = np.where(cave == '+')[1][0]
        count += 1
        while(sand_moving):
            try:
                if cave[curr_y + 1][curr_x] == '.':
                    curr_y += 1
                else:
                    if cave[curr_y + 1][curr_x - 1] != '.' and cave[curr_y + 1][curr_x + 1] != '.':
                        cave[curr_y][curr_x] = 'o'
                        sand_moving = False
                        break
                    #left
                    if cave[curr_y + 1][curr_x - 1] == '.':
                        curr_y += 1
                        curr_x -= 1
                    #right
                    elif cave[curr_y + 1][curr_x + 1] == '.':
                        curr_y += 1
                        curr_x += 1
            except:
                sand_complete = False
                sand_moving = False
                break
        sand_moving = True
        if not sand_complete:
            break
        stdscr.addstr(0,0, f'Sand Count: {count}\n' + '\n'.join([''.join(i) for i in cave]))
        stdscr.refresh()
        time.sleep(.8)
    stdscr.getch()


wrapper(display)

# print('\n'.join([''.join(i) for i in cave]), '\n')
# print(count)


#   ATTEMPTS
# 730 is too low