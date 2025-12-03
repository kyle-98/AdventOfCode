import re

DEBUG = False


def increment_invalid(invalid_sum: int, id_val: int, start_val: int, end_val: int) -> int:
    invalid_sum += id_val
    print(f'Invalid ID found in range ({start_val, end_val}): {id_val}')
    return invalid_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [tuple(map(int, id_vals.split('-'))) for id_vals in [line.strip().split(',') for line in f][0]]

    invalid_id_total = 0
    for id_range in data:
        start_id = id_range[0]
        end_id = id_range[1]

        for id_val in range(start_id, end_id + 1):
            integer_dict = {
                '0': 0,
                '1': 0,
                '2': 0,
                '3': 0,
                '4': 0,
                '5': 0,
                '6': 0,
                '7': 0,
                '8': 0,
                '9': 0,
                '10': 0,
            }
            id_val_str = str(id_val)

            quo, remain = divmod(len(id_val_str), 2)
            first_half, second_half = id_val_str[:quo + remain], id_val_str[quo + remain:]

            # If the first half of the string is equivalent to the second half of the string, the id value is invalid for a repeating sequence of numbers
            if first_half == second_half:
                if DEBUG:
                    print('FIRST HALF = SECOND HALF', id_val)
                invalid_id_total = increment_invalid(invalid_id_total, id_val, start_id, end_id)
                continue
                
            
            for character in id_val_str:
                integer_dict[character] += 1

            non_zero_counts = [key for key, value in integer_dict.items() if value != 0]

            mid_point = len(id_val_str) // 2
            char_regex = r''
            is_invalid = False
            for idx, character in enumerate(id_val_str):
                # Dont let the loop go for more than half the string, if going over half way without being matched for invalid, it will be a valid id
                if idx > mid_point:
                    break

                char_regex += character

                matches = re.findall(char_regex, id_val_str)

                # Avoid single digit integers from being marked as invalid
                if len(matches) == 1:
                    continue

                # Check to see if combining all the matches makes the original id string value, if it does, the current id is invalid
                matches_str = ''.join(matches)
                if matches_str == id_val_str:
                    is_invalid = True
                    break

            if is_invalid:
                invalid_id_total = increment_invalid(invalid_id_total, id_val, start_id, end_id)
                continue

            # If the len of the current id value's character is an odd number
            if len(id_val_str) % 2 != 0:
                # If the number of integer characters in the current id is equal to 1 then the value is invalid
                if len(non_zero_counts) == 1 and len(id_val_str) != 1:
                    if DEBUG:
                        print('NUMBER OF INT CHARS = 1', id_val)
                    invalid_id_total = increment_invalid(invalid_id_total, id_val, start_id, end_id)
                    continue
                # If the id value is odd # of characters in length it is valid as long as it isnt the same repeating character over and over
                else:
                    continue

            non_zero_sum = sum([integer_dict[character] for character in non_zero_counts])

            is_invalid = False
            for character in non_zero_counts:
                # If the total length of the id value string is not even, the current id value is invalid
                if integer_dict[character] % 2 == 0:
                    is_invalid = True
                    if DEBUG:
                        print('NUMBER OF CHARACTERS BAD', id_val)
                else:
                    is_invalid = False

                if integer_dict[character] == len(id_val_str):
                    is_invalid = True
                    if DEBUG:
                        print('SAME LENGTH AS ID LEN', id_val)
                else:
                    is_invalid = False

            if is_invalid:
                invalid_id_total = increment_invalid(invalid_id_total, id_val, start_id, end_id)

    print(invalid_id_total)


# 29997908999 > Too low