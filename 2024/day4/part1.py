import numpy as np
import re

with open('input.txt', 'r') as infile:
    data = [list(l.rstrip()) for l in infile]

data = np.array(data)
regex_f = r'XMAS'
regex_b = r'SAMX'

count = 0
for d in data:
    row = ''.join(d)
    count += len(re.findall(regex_f, row))
    count += len(re.findall(regex_b, row))

# print(data)
# print(count)

data_t = np.copy(data)
data_t = data_t.transpose()
for d in data_t:
    row = ''.join(d)
    count += len(re.findall(regex_f, row))
    count += len(re.findall(regex_b, row))

# print(count)

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


for row in range(0, ARRAY_SHAPE[1]):
    for col in range(0, ARRAY_SHAPE[0]):
        # print((row,col), data[(row,col)])
        if data[(row, col)] == 'X':
            movement_dict = {
                (row - 1, col - 1): '--',
                (row + 1, col - 1): '+-',
                (row - 1, col + 1): '-+',
                (row + 1, col + 1): '++'
            }
            for y_movement, x_movement in movement_dict.keys():
                current_direction = ''
                if not isOOB((y_movement, x_movement)) and data[(y_movement, x_movement)] == 'M':
                    current_direction = movement_dict[(y_movement, x_movement)]
                    cur_coords = gen_new_coords(current_direction, (y_movement, x_movement))
                    if not isOOB(cur_coords) and data[cur_coords] == 'A':
                        cur_coords = gen_new_coords(current_direction, cur_coords)
                        if not isOOB(cur_coords) and data[cur_coords] == 'S':
                            # print(cur_coords)
                            count += 1
                # print((row,col), data[(row,col)], (y_movement, x_movement))

print(count)