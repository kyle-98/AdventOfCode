import numpy as np

def get_area(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)


def is_valid_rectangle(prefix_sum: np.array, point1: tuple[int, int], point2: tuple[int, int], x_map: dict[int, int], y_map: dict[int, int]) -> bool:
    x1, x2 = sorted([x_map[point1[0]] * 2, x_map[point2[0]] * 2])
    y1, y2 = sorted([y_map[point1[1]] * 2, y_map[point2[1]] * 2])
    
    expected_sum = (x2 - x1 + 1) * (y2 - y1 + 1)
    current_sum = prefix_sum[y2 + 1, x2 + 1] - prefix_sum[y1, x2 + 1] - prefix_sum[y2 + 1, x1] + prefix_sum[y1, x1]
    
    return current_sum == expected_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [tuple(map(int, val.strip().split(','))) for val in f]

    sorted_x = sorted(list(set(coord[0] for coord in data)))
    sorted_y = sorted(list(set(coord[1] for coord in data)))
    x_map = {val: idx for idx, val in enumerate(sorted_x)}
    y_map = {val: idx for idx, val in enumerate(sorted_y)}

    grid_height = 2 * len(sorted_y) - 1
    grid_width = 2 * len(sorted_x) - 1
    grid = np.zeros((grid_height, grid_width), dtype=int)
    complete_border_coords = data + [data[0]]

    for idx in range(len(complete_border_coords) - 1):
        point1, point2 = complete_border_coords[idx], complete_border_coords[idx + 1]
        x_1 = x_map[point1[0]] * 2
        y_1 = y_map[point1[1]] * 2
        x_2 = x_map[point2[0]] * 2
        y_2 = y_map[point2[1]] * 2
        grid[min(y_1, y_2):max(y_1, y_2) + 1, min(x_1, x_2):max(x_1, x_2) + 1] = 1

    for y_value in range(1, grid_height, 2):
        in_area = False
        for x_value in range(grid_width):
            if grid[y_value, x_value] == 1:
                in_area = not in_area
            elif in_area:
                grid[y_value, x_value] = 1
    
    for y_value in range(0, grid_height, 2):
        for x_value in range(grid_width):
            if grid[y_value, x_value] == 0:
                above = grid[y_value-1, x_value] if y_value > 0 else 0
                below = grid[y_value+1, x_value] if y_value < grid_height - 1 else 0
                if above == 1 or below == 1:
                    grid[y_value, x_value] = 1

    valid_tiles = np.zeros((grid_height + 1, grid_width + 1), dtype=int)
    for y_value in range(grid_height):
        for x_value in range(grid_width):
            valid_tiles[y_value + 1, x_value + 1] = grid[y_value, x_value] + valid_tiles[y_value, x_value + 1] + valid_tiles[y_value + 1, x_value] - valid_tiles[y_value, x_value]

    max_area = 0
    for point1_idx in range(len(data)):
        for point2_idx in range(point1_idx + 1, len(data)):
            point1 = data[point1_idx]
            point2 = data[point2_idx]
            
            if is_valid_rectangle(valid_tiles, point1, point2, x_map, y_map):
                area = get_area(point1, point2)
                if area > max_area:
                    max_area = area

    print(max_area)

# 2998015284 > Too High
# 2998024779 > Too High
# 2997951946 > Too High
# 4712092762 > Too High