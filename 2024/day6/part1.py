import numpy as np
import curses
import time

class GuardInfo:
    def __init__(self, row: int = 0, col: int = 0) -> None:
        self.row = row
        self.col = col

# def print_matrix(stdscr: curses.wrapper, matrix: np.array, y: int, x: int) -> None:
#     for i, row in enumerate(matrix):
#         stdscr.addstr(y + i, x, " ".join(map(str, row)))
#     stdscr.refresh()

def get_guard_char(matrix: np.array, coords: tuple[int, int]) -> str:
    return matrix[(coords[0], coords[1])]

def is_OOA(coords: tuple[int, int]) -> bool:
    return (coords[0] >= ARRAY_SHAPE[0] or coords[0] < 0) or (coords[1] >= ARRAY_SHAPE[1] or coords[1] < 0)

with open('input.txt', 'r') as infile:
    matrix = [list(l.rstrip()) for l in infile]

matrix =  np.array(matrix)
ARRAY_SHAPE = matrix.shape

def main():
    guard = GuardInfo(
        int(np.where(matrix == '^')[0]),
        int(np.where(matrix == '^')[1])
    )

    visited = [ [False for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
    visited[guard.row][guard.col] = True
    has_left = False

    while not has_left:
        #(guard.row, guard.col)
        # print_matrix(stdscr, matrix, 3, 0)
        # stdscr.addstr(0, 0, f'Guard Row: {guard.row} ~ Guard Col: {guard.col}')
        # stdscr.addstr(1, 0, f'Visit Count: {sum(sum(visits) for visits in visited)}')
        # stdscr.refresh()
        match get_guard_char(matrix, (guard.row, guard.col)):
            case '^':
                new_pos = (guard.row - 1, guard.col)
                if is_OOA(new_pos):
                    has_left = True
                elif matrix[new_pos] == '#':
                    matrix[(guard.row, guard.col)] = '>'
                else:
                    matrix[(guard.row, guard.col)] = 'X'
                    guard.row = new_pos[0]
                    guard.col = new_pos[1] 
                    matrix[(guard.row, guard.col)] = '^'
                    visited[guard.row][guard.col] = True
            case '>':
                new_pos = (guard.row, guard.col + 1)
                if is_OOA(new_pos):
                    has_left = True
                elif matrix[new_pos] == '#':
                    matrix[(guard.row, guard.col)] = 'V'
                else:
                    matrix[(guard.row, guard.col)] = 'X'
                    guard.row = new_pos[0]
                    guard.col = new_pos[1] 
                    matrix[(guard.row, guard.col)] = '>'
                    visited[guard.row][guard.col] = True
            case '<':
                new_pos = (guard.row, guard.col - 1)
                if is_OOA(new_pos):
                    has_left = True
                elif matrix[new_pos] == '#':
                    matrix[(guard.row, guard.col)] = '^'
                else:
                    matrix[(guard.row, guard.col)] = 'X'
                    guard.row = new_pos[0]
                    guard.col = new_pos[1] 
                    matrix[(guard.row, guard.col)] = '<'
                    visited[guard.row][guard.col] = True
            case 'V':
                new_pos = (guard.row + 1, guard.col)
                if is_OOA(new_pos):
                    has_left = True
                elif matrix[new_pos] == '#':
                    matrix[(guard.row, guard.col)] = '<'
                else:
                    matrix[(guard.row, guard.col)] = 'X'
                    guard.row = new_pos[0]
                    guard.col = new_pos[1] 
                    matrix[(guard.row, guard.col)] = 'V'
                    visited[guard.row][guard.col] = True
        
        #time.sleep(0.2)


    # stdscr.addstr(1, 0, 'GOOD MORNING MINTO!!! EXIT BY HITTING ANY KEY')
    # stdscr.getch()    
    # curses.endwin()
        
        #print(CD(f'Guard Row: {guard.row}', 'green'), CD(f'Guard Col: {guard.col}', 'green'))
    print(sum(sum(visits) for visits in visited))

if __name__ == '__main__':
    # curses.wrapper(main)
    main()