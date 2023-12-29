import numpy as np

def expand_universe(arr):
    row_indexes = []
    new_arr = arr
    for index, row in enumerate(arr):
        if all(d == '.' for d in row):
            row_indexes.append(index)
    for i in row_indexes:
        new_arr = np.insert(new_arr, i + row_indexes.index(i), np.array(['.' for _ in range(len(arr[0]))]), axis=0)
    
    return new_arr

def get_distance(g1, g2):
    return np.abs(g2[0] - g1[0]) + np.abs(g2[1] - g1[1])

def main():
    with open('input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    
    
    # print(data, '\n')
    # expand universe
    exp_data = expand_universe(data)
    # print(exp_data, '\n')
    exp_data = np.transpose(exp_data)
    exp_data = expand_universe(exp_data)
    exp_data = np.transpose(exp_data)  
    # print(exp_data, '\n')

    galaxy_locs = np.argwhere(exp_data == '#')
    galaxy_dist = 0
    # print(galaxy_locs, '\n')
    temp_galaxies = galaxy_locs
    # np.where(np.array([np.array_equal(row, [0,4]) for row in galaxy_locs]))[0]
    for i in range(len(galaxy_locs)):
        temp_galaxies = np.delete(temp_galaxies, 0, axis=0)
        for tg in temp_galaxies:
            galaxy_dist += get_distance(galaxy_locs[i], tg)
            # print('MAIN:', galaxy_locs[i], 'ALT', tg, 'DISTANCE', get_distance(galaxy_locs[i], tg))
            # print(get_distance(galaxy_locs[i], tg))
    print(galaxy_dist)    
        

if __name__ == '__main__':
    main()