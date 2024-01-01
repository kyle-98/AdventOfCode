import re

def hash(string):
    label = re.split('-|=', string)[0]
    hash_val = 0
    for l in label:
        hash_val += ord(l)
        hash_val *= 17
        hash_val %= 256
    return hash_val


def main():
    with open('input.txt', 'r') as input_file:
        data = input_file.readline().rstrip().split(',')
    boxes = {i: [] for i in range(256)}

    for string in data:
        box_num = hash(string)
        if '-' in string:
            for contents in boxes[box_num]:
                if string.split('-')[0] == contents.split(' ')[0]:
                    boxes[box_num].pop(boxes[box_num].index(contents))
                    break
        else:
            rp_check = False
            for contents in boxes[box_num]:
                if string.split('=')[0] == contents.split(' ')[0]:
                    boxes[box_num][boxes[box_num].index(contents)] = ' '.join(string.split('='))
                    rp_check = True
                    break
            if not rp_check:
                boxes[box_num].append(' '.join(string.split('=')))

    total_power = 0
    for box in boxes:
        for lenses in boxes[box]:
            total_power += (box + 1) * (boxes[box].index(lenses) + 1) * int(lenses.split(' ')[1])
    print(total_power)


if __name__ == '__main__':
    main()