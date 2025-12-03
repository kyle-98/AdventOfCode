if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [tuple(map(int, id_vals.split('-'))) for id_vals in [line.strip().split(',') for line in f][0]]

    invalid_id_total = 0
    for id_range in data:
        start_id = id_range[0]
        end_id = id_range[1]

        for id_val in range(start_id, end_id + 1):
            id_val_str = str(id_val)
            quo, remain = divmod(len(id_val_str), 2)
            first_half, second_half = id_val_str[:quo + remain], id_val_str[quo + remain:]

            if first_half == second_half:
                print(f'Invalid ID found in range ({start_id, end_id}): {id_val}')
                invalid_id_total += id_val

    print(invalid_id_total)



            # integer_dict = {
            #     '0': 0,
            #     '1': 0,
            #     '2': 0,
            #     '3': 0,
            #     '4': 0,
            #     '5': 0,
            #     '6': 0,
            #     '7': 0,
            #     '8': 0,
            #     '9': 0,
            #     '10': 0,
            # }
            # id_val_str = str(id_val)

            # # If the total length of the id value string is not even, the current id value is not invalid
            # if len(id_val_str) % 2 != 0:
            #     continue

            # for character in id_val_str:
            #     integer_dict[character] += 1

            # non_zero_counts = [key for key, value in integer_dict.items() if value != 0]
            # is_invalid = True
            # non_zero_sum = sum([integer_dict[character] for character in non_zero_counts])

            # # If the value of the sum of the # of occurences for the digits does not equal the length of the current id value, it is not invalid
            # if non_zero_sum != len(id_val_str):
            #     is_invalid = False
            #     continue

            # for character in non_zero_counts:
            #     # If the current digit's occurence count is not even, the current id value is not invalid
            #     if integer_dict[character] % 2 != 0:
            #         is_invalid = False
            #         break



                # if integer_dict[character] != len(id_val_str):
                #     is_invalid = False
                #     break

            # if is_invalid:
            #     print(f'Invalid ID found in range ({start_id, end_id}): {id_val}')
            #     invalid_ids.append(id_val)
