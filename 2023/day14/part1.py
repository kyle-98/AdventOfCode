import numpy as np

def main():
    with open('input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    
    rock_coords = np.argwhere(data == 'O')
    # print(rock_coords)
    for rock in rock_coords:
        index = rock[0]
        while True:
            if data[index - 1, rock[1]] in ['O', '#'] or index <= 0:
                break
            else:
                data[index - 1, rock[1]] = 'O'
                data[index, rock[1]] = '.'

                index -= 1
    height = len(data)
    rock_load = 0
    for row in data:
        rock_load += len((np.argwhere(row == 'O'))) * height
        height -= 1
    print(rock_load)


if __name__ == '__main__':
    main()