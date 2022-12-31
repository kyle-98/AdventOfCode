import numpy as np

data = [line.rstrip() for line in open('input.txt')]
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
FLOOR_LEN = 900
cave = np.full(((max_depth + 1) + 2, FLOOR_LEN), '.')
# cave = np.full(((max_width + 1) - min_width, max_depth + 1), '.')
cave[0][(499 - max_width) - FLOOR_LEN // 2] = '+'
# print('\n'.join([''.join(i) for i in cave]), '\n')
# print((max_width + 1) - min_width)

#floor
cave[(max_depth + 2)] = len(cave[0][0]) * '#'
(print)

for coord in coords_lists:
    prev_x = 0
    prev_y = 0
    for c in coord:
        x = int(c.split(',')[0])
        y = int(c.split(',')[1])
        cave[y][((x - 1) - max_width) + FLOOR_LEN // 2] = '#'
        if prev_x == x:
            for i in range(min(prev_y, y) + 1, max(prev_y, y) + 1):
                cave[i][((x - 1) - max_width) + FLOOR_LEN // 2] = '#'
        if prev_y == y:
            for i in range(min(prev_x, x), max(prev_x, x)):
                cave[y][((i - 1) - max_width) +  FLOOR_LEN // 2] = '#'
        prev_x = x
        prev_y = y

print('\n'.join([''.join(i) for i in cave]), '\n')
print('Sand Falling...\n')
count = 0
sand_moving = True
sand_complete = True
temp_x = np.where(cave == '+')[0][0]
temp_y = np.where(cave == '+')[1][0]

while(sand_complete):
    try:
        curr_y = np.where(cave == '+')[0][0]
        curr_x = np.where(cave == '+')[1][0]
    except:
        break

    while(sand_moving):
        try:
            #check if area under is clear, if so move down 1
            if cave[curr_y + 1][curr_x] == '.':
                curr_y += 1
            #if area isnt clear check down left & down right
            else:
                #if both places are blocked, sand comes to rest
                if cave[curr_y + 1][curr_x - 1] != '.' and cave[curr_y + 1][curr_x + 1] != '.':
                    cave[curr_y][curr_x] = 'o'
                    sand_moving = False
                    break
                #left
                elif cave[curr_y + 1][curr_x - 1] == '.':
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
    count += 1

    # print('Sand count:', count + 1)
    # print('\n'.join([''.join(i) for i in cave]), '\n')

print('\n'.join([''.join(i) for i in cave]), '\n')
print(count)


#   ATTEMPTS
# 730 is too low
# 731 is too low