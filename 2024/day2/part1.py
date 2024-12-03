with open('input.txt', 'r') as infile:
    lines = [[int(l) for l in line.strip().split(' ')] for line in infile.readlines()]

sc = 0
for line in lines:
    prev_inc = ''
    cur_inc = ''
    c = False
    for l in range(0, len(line) - 1):
        cur = line[l]
        new = line[l + 1]
        # print(cur, new)
        if cur - new >= 1 and cur - new <= 3:
            cur_inc = 'D'
            c = True
        elif new - cur >= 1 and new - cur <= 3:
            cur_inc = 'I'
            c = True
        else:
            c = False
        # print(cur_inc, prev_inc)
        if not c or (l != 0 and cur_inc != prev_inc):
            c = False
            # print('unsafe', line)
            break

        prev_inc = cur_inc

    if c:
        # print('safe', line)
        sc += 1

print(sc)
    