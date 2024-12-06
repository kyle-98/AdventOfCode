import numpy as np

with open('input.txt', 'r') as infile:
    data = [list(l.rstrip()) for l in infile]

data = np.array(data)
count = 0
ARRAY_SHAPE = data.shape

def isOOB(coords: tuple[int, int]) -> bool:
    return (coords[0] >= ARRAY_SHAPE[0] or coords[0] < 0) or (coords[1] >= ARRAY_SHAPE[1] or coords[1] < 0)

def gen_new_coords(direction: str, coords: tuple[int, int]) -> tuple[int, int]:
    match direction:
        case '--':
            return(coords[0] - 1, coords[1] - 1)
        case '+-':
            return(coords[0] + 1, coords[1] - 1)
        case '-+':
            return(coords[0] - 1, coords[1] + 1)
        case '++':
            return(coords[0] + 1, coords[1] + 1)


def validate_A(A_coords):
    md = {
        '--': (A_coords[0] - 1, A_coords[1] - 1),
        '+-': (A_coords[0] + 1, A_coords[1] - 1),
        '-+': (A_coords[0] - 1, A_coords[1] + 1),
        '++': (A_coords[0] + 1, A_coords[1] + 1)
    }
    is_valid = False

    if (data[md['--']] == 'M') and (data[md['++']] == 'S') or (data[md['--']] == 'S') and (data[md['++']] == 'M'):
        is_valid = True
    else:
        return False
    
    if (data[md['+-']] == 'M') and (data[md['-+']] == 'S') or (data[md['+-']] == 'S') and (data[md['-+']] == 'M'):
        is_valid = True
    else:
        return False
    
    return is_valid

for row in range(0, ARRAY_SHAPE[1]):
    for col in range(0, ARRAY_SHAPE[0]):
        # print((row,col), data[(row,col)])
        skip = False
        if data[(row, col)] == 'A':
            # print(row, col)
            for y_movement, x_movement in [(row - 1, col - 1), (row + 1, col - 1), (row - 1, col + 1), (row + 1, col + 1)]:
                cur_coords = (y_movement, x_movement)
                if isOOB(cur_coords):
                    skip = True
                    break

            if not skip:
                if validate_A((row, col)):
                    # print((row,col))
                    count += 1

print(count)