
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
        first_num = find_first_num(d, 'l')
        last_num = find_first_num(d, 'r')
        res += int(str(first_num) + str(last_num))
    print(res)

if __name__ == '__main__':
    main()