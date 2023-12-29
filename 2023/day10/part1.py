import numpy as np


def main():
    with open('input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    start_point = np.argwhere(data == 'S')[0]
    # next_element(data, start_point[1], start_point[0])
    loop_pos_list = []
    curr_pos = [0,0]
    for y_val, x_val in ((0,-1), (0,1), (1,0), (-1,0)):
        temp_x = start_point[1] + x_val
        temp_y = start_point[0] + y_val
        # left
        if ([y_val, x_val] == [0, -1]) and (data[temp_y, temp_x] in ['-', 'L', 'F']):
            curr_pos = [temp_y, temp_x]
            loop_pos_list.append(curr_pos)
            break
        # right
        elif ([y_val, x_val] == [0, 1]) and (data[temp_y, temp_x] in ['-', 'J', '7']):
            curr_pos = [temp_y, temp_x]
            loop_pos_list.append(curr_pos)
            break
        # up
        elif ([y_val, x_val] == [1, 0]) and (data[temp_y, temp_x] in ['L', '|', 'J']):
            curr_pos = [temp_y, temp_x]
            loop_pos_list.append(curr_pos)
            break
        # down
        elif ([y_val, x_val] == [-1, 0]) and (data[temp_y, temp_x] in ['|', '7', 'F']):
            curr_pos = [temp_y, temp_x]
            loop_pos_list.append(curr_pos)
            break
        else:
            continue

    prev_pos = [start_point[0], start_point[1]]
    while curr_pos != [start_point[0], start_point[1]]:
        # print('C:', curr_pos, data[temp_y, temp_x], 'P:', prev_pos, 'POS LIST:', loop_pos_list, 'TMPY', temp_y, 'TMPX:', temp_x)
        flag = False
        for y_val, x_val in ((0,-1), (0,1), (1,0), (-1,0)):
            temp_x = curr_pos[1] + x_val
            temp_y = curr_pos[0] + y_val
            if temp_x >= len(data[0]) or temp_y >= len(data) or temp_x < 0 or temp_y < 0:
                continue
            else:
                # print('C:', curr_pos, data[temp_y, temp_x], 'P:', prev_pos, 'POS LIST:', loop_pos_list, 'TMPY', temp_y, 'TMPX:', temp_x)
                # left
                if ([y_val, x_val] == [0, -1]) and (data[temp_y, temp_x] in ['-', 'L', 'F']) and (prev_pos != [temp_y, temp_x]) and (data[curr_pos[0], curr_pos[1]] not in ['L', 'F', '|']):
                    prev_pos = curr_pos
                    curr_pos = [temp_y, temp_x]
                    loop_pos_list.append(curr_pos)
                    flag = True
                    break
                # right
                elif ([y_val, x_val] == [0, 1]) and (data[temp_y, temp_x] in ['-', 'J', '7']) and (prev_pos != [temp_y, temp_x]) and (data[curr_pos[0], curr_pos[1]] not in ['J', '7', '|']):
                    prev_pos = curr_pos
                    curr_pos = [temp_y, temp_x]
                    loop_pos_list.append(curr_pos)
                    flag = True
                    break
                # down
                elif ([y_val, x_val] == [1, 0]) and (data[temp_y, temp_x] in ['L', '|', 'J']) and (prev_pos != [temp_y, temp_x]) and (data[curr_pos[0], curr_pos[1]] not in ['J', '-', 'L']):
                    prev_pos = curr_pos
                    curr_pos = [temp_y, temp_x]
                    loop_pos_list.append(curr_pos)
                    flag = True
                    break
                # up
                elif ([y_val, x_val] == [-1, 0]) and (data[temp_y, temp_x] in ['|', '7', 'F']) and (prev_pos != [temp_y, temp_x]) and (data[curr_pos[0], curr_pos[1]] not in ['7', 'F', '-']):
                    prev_pos = curr_pos
                    curr_pos = [temp_y, temp_x]
                    loop_pos_list.append(curr_pos)
                    flag = True
                    break

        # check for starting character
        if data[temp_y, temp_x] == 'S' and prev_pos != [temp_y, temp_x] and not flag:
            curr_pos = [temp_y, temp_x]
            loop_pos_list.append(curr_pos)
            break
    
    print(len(loop_pos_list) / 2)

    

if __name__ == '__main__':
    main()

# 6863 <- too low
# 6864 <- correct