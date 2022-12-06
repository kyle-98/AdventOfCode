INPUT_FILE = 'input.txt'

def check_chars(data):
    count = 14
    chars_queue = []
    for i in range(count):
        chars_queue.append(data[i])
    for d in range(count, len(data)):
        if len(set(chars_queue)) == len(chars_queue):
            break
        else:
            chars_queue.pop(0)
            chars_queue.append(data[d])
            count += 1
    return count


with open(INPUT_FILE, 'r') as infile:
    print(check_chars(infile.read()))