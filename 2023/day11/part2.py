import numpy as np
"""
- find what index empty rows are at in the 2darray
    - for every point passed a given empty index add (number of empty indexes passed) * (our multiplied value {1_000_000}) to the x coordinate
- transpose the 2darray
    - run previous steps to find empty rows and calulate the "y-values" which are actually x bc of transpose
- run the manhattan calculations to get distances between each point

"""
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

def get_empty_rows(arr):
    row_indexes = []
    for index, row in enumerate(arr):
        if all(d == '.' for d in row):
            row_indexes.append(index)
    return row_indexes



def main():
    with open('input.txt', 'r') as input_file:
        data = np.array([list(line.rstrip()) for line in input_file])
    GALAXY_AGE = 1_000_000

    galaxy_locs = np.argwhere(data == '#')
    empty_yvals = get_empty_rows(data)
    transpose_data = np.transpose(data)
    empty_xvals = get_empty_rows(transpose_data)
    GALAXY_LOCATIONS = np.copy(galaxy_locs)
    print(empty_xvals, empty_yvals)
    # rows
    for xval in empty_xvals:
        for index, galaxy in enumerate(galaxy_locs):
            if GALAXY_LOCATIONS[index][1] > xval:
                galaxy[1] += GALAXY_AGE - 1
    # columns 
    for yval in empty_yvals:
        for index, galaxy in enumerate(galaxy_locs):
            if GALAXY_LOCATIONS[index][0] > yval:
                galaxy[0] += GALAXY_AGE - 1

    # print(galaxy_locs)
    galaxy_dist = 0
    temp_galaxies = galaxy_locs
    for i in range(len(galaxy_locs)):

        temp_galaxies = np.delete(temp_galaxies, 0, axis=0)
        for tg in temp_galaxies:
            # print('MAIN:', galaxy_locs[i], 'ALT', tg, 'DISTANCE', get_distance(galaxy_locs[i], tg))
            galaxy_dist += get_distance(galaxy_locs[i], tg)
    # print(galaxy_dist)
if __name__ == '__main__':
    main()