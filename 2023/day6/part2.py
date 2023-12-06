import numpy as np

def main():
    with open('input.txt', 'r') as input_file:
        data = [i.rstrip() for i in input_file]

    time = [i for i in list(filter(None, data[0].split(' ')))[1:]]
    this_time = ''
    for t in time:
        this_time += t
    time = int(this_time)
    dist = [i for i in list(filter(None, data[1].split(' ')))[1:]]
    this_dist = ''
    for d in dist:
        this_dist += d
    dist = int(this_dist)
    x, w = 0, 0
    for i in range(1, time + 1):
        t = (time - i) * (time - (time - i))
        if t > dist:
            w = time - (time - i)
            break
    for i in range(time, w + 1, -1):
        t = (time - i) * (time - (time - i))
        if t > dist:
            x = time - (time - i)
            break
    
    print((x - w) + 1)
    

if __name__ == '__main__':
    main()