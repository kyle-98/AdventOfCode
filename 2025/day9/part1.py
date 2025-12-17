def get_area(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1] + 1) + 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [tuple(map(int, val.strip().split(','))) for val in f]

    # print(data)
    max_area = 0

    for idx, point1 in enumerate(data):
        compare_list = data.copy()
        del compare_list[idx]

        for point2 in compare_list:
            area = get_area(point1, point2)
            # print(point1, point2, area)

            if area > max_area:
                max_area = area

    print(max_area)