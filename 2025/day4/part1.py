import numpy as np

DEBUG = False

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    data_lists = [[char for char in row] for row in data]

    forklift_grid = np.array(data_lists)
    grid_mask = forklift_grid.copy()

    rows, cols = forklift_grid.shape

    paper_moveable_count = 0

    TARGET_VAL = 'x'

    for r in range(rows):
        for c in range(cols):
            paper_count = 0
            value = forklift_grid[r, c]
            points_to_check = [
                (r - 1, c - 1),
                (r - 1, c),
                (r - 1, c + 1),
                (r, c + 1),
                (r + 1, c+ 1),
                (r + 1, c),
                (r + 1, c - 1),
                (r, c - 1)
            ]

            if value == '@':
                for coords in points_to_check:
                    x = coords[0]
                    y = coords[1]
                    # Ensure the current coords are within the grid
                    if (x >= 0 and x < rows) and (y >= 0 and y < cols):
                        if forklift_grid[x, y] == '@':
                            paper_count += 1
                if paper_count < 4:
                    grid_mask[r, c] = 'x'
                    paper_moveable_count += 1

    if DEBUG:
        print(grid_mask)

    print(paper_moveable_count)





