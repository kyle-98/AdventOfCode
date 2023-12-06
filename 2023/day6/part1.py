import numpy as np

def main():
    with open('input.txt', 'r') as input_file:
        data = [i.rstrip() for i in input_file]

    times = [int(i) for i in list(filter(None, data[0].split(' ')))[1:]]
    dist = [int(i) for i in list(filter(None, data[1].split(' ')))[1:]]

    wins = []
    for x,time in enumerate(times):
        w = 0
        for i in range(1, time + 1):
            t = (time - i) * (time - (time - i))
            if t > dist[x]:
                w += 1
        wins.append(w)
    print(np.prod(wins))
if __name__ == '__main__':
    main()