with open('input.txt', 'r') as infile:
    lines = [[int(l) for l in line.strip().split(' ')] for line in infile.readlines()]

safe_score = 0
for line in lines:
    prev_inc = ''
    cur_inc = ''
    valid = False
    for index in range(0, len(line) - 1):
        cur = line[index]
        new = line[index + 1]
        # print(cur, new)
        if cur - new >= 1 and cur - new <= 3:
            cur_inc = 'D'
            valid = True
        elif new - cur >= 1 and new - cur <= 3:
            cur_inc = 'I'
            valid = True
        else:
            valid = False
        # print(cur_inc, prev_inc)
        if not valid or (index != 0 and cur_inc != prev_inc):
            valid = False
            index_validation_checks = line.copy()
            fail_count = 0
            # print(cur, new)
            for ivc in range(0, len(index_validation_checks)):
                temp_line = line.copy()
                del temp_line[ivc]
                temp_prev_inc = ''
                temp_cur_inc = ''
                for temp_index in range(0, len(temp_line) - 1):
                    temp_cur = temp_line[temp_index]
                    temp_new = temp_line[temp_index + 1]
                    if temp_cur - temp_new >= 1 and temp_cur - temp_new <= 3:
                        temp_cur_inc = 'D'
                        valid = True
                    elif temp_new - temp_cur >= 1 and temp_new - temp_cur <= 3:
                        temp_cur_inc = 'I'
                        valid = True
                    else:
                        valid = False
                    if not valid or (temp_index != 0 and temp_cur_inc != temp_prev_inc):
                        valid = False
                        fail_count += 1
                        break
                    temp_prev_inc = temp_cur_inc
                if valid:
                    break
            if fail_count > 1 and not valid:
                print('unsafe', line)
                valid = False
                break
            break

        prev_inc = cur_inc

    if valid:
        print('safe', line)
        safe_score += 1

print(safe_score)
    