import numpy as np


def main():
    with open('input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    TOTAL_CYCLES = 1_000_000_000
    platforms = {}
    cycle_index = 0
    rock_loads = []
    while True:
        rock_coords = np.argwhere(data == 'O')
        rock_coords = rock_coords[rock_coords[:, 0].argsort()]
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

        height = len(data)
        rock_load = 0

        cycle_index += 1
        for row in data:
            rock_load += len((np.argwhere(row == 'O'))) * height
            height -= 1
        rock_loads.append(rock_load)
        if tuple(map(tuple, data)) in platforms:
            ending_cycle = cycle_index
            starting_cycle = platforms[tuple(map(tuple, data))]
            size = ending_cycle - starting_cycle
            finl_cycle = ((TOTAL_CYCLES - starting_cycle) % size) + starting_cycle
            print(rock_loads[finl_cycle - 1])
            print(rock_loads)
            break
        else:
            platforms[tuple(map(tuple, data))] = cycle_index
        

        

    # print(data)

    # stdscr.getch()
    # curses.endwin()
    # print(rock_coords)
    # stdscr.getch()

if __name__ == '__main__':
    # curses.wrapper(main)
    main()

# 95305 <- too high
# 95285 <- too high
# 95284 <- too high