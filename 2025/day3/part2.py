DEBUG = False

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    total_joltage = 0

    for bank in data:
        digit_dict = {digit: [] for digit in '123456789'}
        # Loop through the digits in the battery bank and store the indexes inside the digit_dict dictionary
        for idx, digit in enumerate(bank):
            digit_dict[digit].append(idx)

        # Get a list of all the digits that exist at least once in the bank of digits
        valid_digits = [key for key, value in digit_dict.items() if len(value) != 0]
        valid_digits.sort(reverse=True)

        bank_length = len(bank)
        full_jolt = ''
        curr_max_jolt = 0
        curr_max_idx = 0
        # Get the first searching character range and leave at most 11 characters remaining outside of the first search
        MAX_LEN = 11
        curr_search_str = bank[:bank_length - MAX_LEN]
        current_bank = bank

        while True:
            curr_max_jolt = 0
            curr_max_idx = 0
            if len(curr_search_str) == 0 or len(full_jolt) == 12:
                break


            # Loop through the characters in the search string
            for idx, digit in enumerate(curr_search_str):
                # Find the max voalue in the search string and save the index as well as the value
                if int(digit) > curr_max_jolt:
                    curr_max_jolt = int(digit)
                    curr_max_idx = idx + 1

            # Append the max number found in the search string to the full joltage of the current bank
            full_jolt += str(curr_max_jolt)

            # Store the current bank information that we parse looking for the next search string
            current_bank = current_bank[curr_max_idx:]

            # Create the next search string based on the number of characters that are needed vs the total length of the current bank
            curr_search_str = current_bank[:len(current_bank) - (MAX_LEN - len(full_jolt))]

            # if DEBUG:
            #     print('Search String:', curr_search_str)
            #     print('Current Max Jolt:', curr_max_jolt)
            #     print('Current Max Idx:', curr_max_idx)
            #     print('Current Full Jolt:', full_jolt)
            #     print('Total Chars Needed:', (MAX_LEN - len(full_jolt) + 1))
            #     print('/' * 20)

        if DEBUG:
            print('Bank:', bank)
            print('Current Max Jolt:', curr_max_jolt)
            print('Max Digit:', 'N/A')
            print('Max Digit Indexes:', 'N/A')
            print('Valid Digits:', valid_digits)
            print('>> Highest Joltage:', full_jolt)
            print('-' * 20)

        total_joltage += int(full_jolt)


    print(total_joltage)