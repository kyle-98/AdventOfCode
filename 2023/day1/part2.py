

def replace_stupid_nums(s):
    nd = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    td = {}
    for num in nd:
        if s.find(num) != -1:
            td.update({num: s.find(num)})

    l = sorted(td.items(), key=lambda x:x[1])
    try:
        s = s.replace(l[0][0], nd[l[0][0]])
    except:
        pass
    try:
        s = s.replace(l[-1][0], nd[l[-1][0]])
    except:
        pass
    return s

def find_first_num(str, dir):
    if dir == 'l':
        for i in str:
            try:
                return int(i)
            except:
                continue
    else:
        for i in reversed(str):
            try:
                return int(i)
            except:
                continue

def main():
    with open('input.txt', 'r') as input_file:
        data = [line.rstrip() for line in input_file]
    res = 0
    for d in data:
        new_str = replace_stupid_nums(d)
        #print(new_str)
        first_num = find_first_num(new_str, 'l')
        last_num = find_first_num(new_str, 'r')
        #print(str(first_num) + str(last_num))
        res += int(str(first_num) + str(last_num))
    print(res)

if __name__ == '__main__':
    main()