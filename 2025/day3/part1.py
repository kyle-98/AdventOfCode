

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

        # Get a list of the max digit's indexes that exist in the bank
        max_digit = valid_digits[0]
        max_digit_indexes = digit_dict[max_digit]

        highest_jolt = 0
        for idx in max_digit_indexes:
            # This means that we do not search forward to avoid comparing against the same number
            if idx == 0:
                before_set = set()
            else:
                before_set = set(bank[:idx])

            # This means that we do not search after to avoid comparing against the same number
            if idx == len(bank) - 1:
                after_set = set()
            else:
                after_set = set(bank[idx + 1:])

            for i in before_set:
                if highest_jolt == '99':
                    break

                curr_jolt = i + max_digit

                if int(curr_jolt) > int(highest_jolt):
                    highest_jolt = curr_jolt

            for i in after_set:
                if highest_jolt == '99':
                    break

                curr_jolt = max_digit + i

                if int(curr_jolt) > int(highest_jolt):
                    highest_jolt = curr_jolt

        if DEBUG:
            print('Bank:', bank)
            print('Max Digit:', max_digit)
            print('Max Digit Indexes:', max_digit_indexes)
            print('Valid Digits:', valid_digits)
            print('>> Highest Joltage:', highest_jolt)
            print('-' * 20)

        total_joltage += int(highest_jolt)
    print(total_joltage)