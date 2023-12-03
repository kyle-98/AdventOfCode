import numpy as np
import re

def main():
    with open('input.txt', 'r') as in_file:
        data = [[l.rstrip()] for l in in_file]
    fd = []
    for d in data:
        t = []
        for x in d[0]:
            t.append(x)
        fd.append(t)
    da = np.array(fd)
    ignore = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    num_check = re.compile(r"[0-9]")
    nums = []
    checked = []
    for row in range(0, len(da) - 1):
        for col in range(0, len(da[0]) - 1):
            # (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1) 
            temp_num = []
            for y_movement, x_movement  in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
                temp_row = row + x_movement
                temp_col = col + y_movement
                c = 1
                tn_flag = False
                if (temp_row == row and temp_col == col) or (temp_row < 0 or temp_col < 0):
                    continue
                elif da[(col, row)] == '*':
                    if re.search(num_check, str(da[(temp_col, temp_row)])):
                        t_num = str(da[(temp_col, temp_row)])
                        
                        while True:
                            try:
                                if re.search(num_check, str(da[(temp_col, temp_row + c)])):
                                    if (temp_col, temp_row + c) in checked:
                                        # print('p-found', (temp_col, temp_row + c))
                                        break
                                    t_num += str(da[(temp_col, temp_row + c)])
                                    checked.append((temp_col, temp_row))
                                    checked.append((temp_col, temp_row + c))
                                    # print('p', c, [temp_col, temp_row + c], t_num)
                                    c += 1
                                    tn_flag = True
                                else: 
                                    break
                            except:
                                break
                        c = 1
                        while True:
                            try:
                                if re.search(num_check, str(da[(temp_col, temp_row - c)])):
                                    if c < 0 or (temp_col, temp_row - c) in checked:
                                        # print('n-found', (temp_col, temp_row - c))
                                        break
                                    t_num = str(da[(temp_col, temp_row - c)]) + t_num
                                    checked.append((temp_col, temp_row))
                                    checked.append((temp_col, temp_row - c))
                                    # print('n', c, [temp_col, temp_row - c], t_num)
                                    c += 1
                                    tn_flag = True
                                else: 
                                    break
                            except:
                                break
                        # print(checked)
                        
                        if tn_flag:
                            # print(t_num)
                            #nums.append(t_num)
                            temp_num.append(t_num)
                        else:
                            if not (temp_col, temp_row) in checked:
                                #nums.append(str(da[(temp_col, temp_row)]))
                                temp_num.append(str(da[(temp_col, temp_row)]))
                        
            if len(temp_num) > 1:
                nums.append(np.prod([int(i) for i in temp_num]))
                        #print([col, row], [temp_col, temp_row], da[(temp_col, temp_row)])
    print(nums, sum(nums))
    #print(nums, sum([int(i) for i in nums]))
                    
                        
                    


if __name__ == '__main__':
    main()

# checked
# 531492 <- too low