DEBUG = True

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

    ingredients = data.split('\n\n')

    ingredient_ids = [line.strip() for line in ingredients[0].split('\n') if line.strip()]

    id_ranges = [tuple(map(int, id_range.split('-'))) for id_range in ingredient_ids]
    id_ranges.sort(key=lambda id_range: id_range[0])
    fresh_ids = [list(id_ranges[0])]
    total_fresh_ids = 0

    for id_range in id_ranges:
        start_id = id_range[0]
        end_id = id_range[1]

        # Get the previously stored range values
        prev_start_id, prev_end_id = fresh_ids[-1]

        # If the current start id is <= the previous end ID, this is an overlap and we take the max between the current end id and the previous end id
        if start_id <= prev_end_id:
            fresh_ids[-1][1] = max(end_id, prev_end_id)

        # If this is a new range, add it to the list of fresh id ranges
        else:
            fresh_ids.append([start_id, end_id])


    for fresh_id in fresh_ids:
        total_fresh_ids += (fresh_id[1] - fresh_id[0] + 1)

        
    print(total_fresh_ids)