import numpy as np

DEBUG = False

if __name__ == '__main__':

    with open('input.txt', 'r') as f: 
        data_array = np.array([[char for char in row] for row in [line.strip() for line in f]])

    rows, columns = data_array.shape

    timelines = np.zeros((rows, columns), dtype=np.int64)
    STARTING_VALUE = 'S'

    starting_coords = np.where(data_array == STARTING_VALUE)
    start_row, start_column = list(zip(starting_coords[0], starting_coords[1]))[0]
    timelines[start_row, start_column] = 1

    # Pascal was cookin too hard https://en.wikipedia.org/wiki/Pascal%27s_triangle (saving this for later so when i get hit with the retardinator-3000 i can remember wtf i was cookin)
    for row in range(start_row, rows - 1):
        for column in range(columns):

            # Store the number of beams arriving at the current point
            beam_count = timelines[row][column]
            if beam_count == 0:
                continue

            point = data_array[row][column]

            # Account for the fact that there are potentially missing ^ to make it not an even triangle, this will send the beam straight downwards
            if point in ('.', 'S'):
                timelines[row + 1][column] += beam_count

            # Split the beam
            elif point == '^':
                # v>
                if column - 1 >= 0:
                    timelines[row + 1][column - 1] += beam_count

                # v<
                if column + 1 < columns:
                    timelines[row + 1][column + 1] += beam_count

    total = timelines[-1].sum()
    
    if DEBUG:
        print('Number timelines grid:\n', timelines)
    print('\nTotal timelines:', total)


# 9572 > Too low
# 6789424 > Too Low