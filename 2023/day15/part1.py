
def main():
    with open('input.txt', 'r') as input_file:
        data = input_file.readline().rstrip().split(',')
    sum_hashes = 0
    for string in data:
        curr_val = 0
        for s in string:
            curr_val += ord(s)
            curr_val *= 17
            curr_val %= 256
        sum_hashes += curr_val
    print(sum_hashes)


if __name__ == '__main__':
    main()
