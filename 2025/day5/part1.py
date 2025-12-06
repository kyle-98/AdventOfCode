if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

    ingredients = data.split('\n\n')

    ingredient_ids = [line.strip() for line in ingredients[0].split('\n') if line.strip()]
    avail_ingredients = [int(line.strip()) for line in ingredients[1].split('\n') if line.strip()]

    id_ranges = [tuple(map(int, id_range.split('-'))) for id_range in ingredient_ids]

    fresh_ingredients = 0

    for avail_ingredient in avail_ingredients:
        for id_range in id_ranges:
            start_id = id_range[0]
            end_id = id_range[1]

            if avail_ingredient >= start_id and avail_ingredient <= end_id:
                fresh_ingredients += 1
                break

    print(fresh_ingredients)