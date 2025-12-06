def extract_number(number: str) -> int:
    return_number = ''
    for char in number:
        if char != 'x':
            return_number += char
    
    return int(return_number)


def perform_operation(chars_list: list[str], operation: str) -> int:
    if operation == '+':
        return_number = 0
    else:
        return_number = 1
    for char in chars_list:
        current_number = extract_number(char)
        if operation == '+':
            return_number += current_number
        else:
            return_number *= current_number

    return return_number


"""
Read through the lines and ignore the line with operations. Wait until all lines have a space and break. Save spaces as 'x's. Store each character of each line in a string to form entire strings with x's

Summary:
    This will transpose the data set from the input while replacing needed spaces with 'x's and removing the spaces which we break the numbers on. This will retain the digits in the correct column for each number as shown in the
    example.

"""
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip('\n\r') for line in f]

    # Filter out the operations from number values
    operations = [d for d in data[-1].split(' ') if d]

    # Remove the operations row from the list
    del data[-1]
    # print(data)

    data_length = len(data[0])
    # print(data_length)

    converted_data = []
    [converted_data.append([]) for _ in operations]
    # print(converted_data)

    total_break_count = 0

    for idx in range(0, data_length):
        space_count = 0
        string_break = False
        current_number = ''

        # Looking through all the elements of the data for the current index
        for data_row in data:
            # We are starting or continuing a row
            if data_row[idx] != ' ':
                current_number += data_row[idx]

            if data_row[idx] == ' ':
                space_count += 1
                if space_count != len(data):
                    current_number += 'x'


            # If the number of spaces we have found in a single column is equal to the number rows in a column, it is a string split space
            if space_count == len(data):
                space_count = 0
                string_break = True
                total_break_count += 1
                current_number = 0
        
        # If we are not splitting the data yet, append the current number to the converted data set on the index in which we are currently breaking on
        if not string_break:
            converted_data[total_break_count].append(current_number)

    # print(converted_data)

    total_value = 0
    for idx, operation in enumerate(operations):
        data_row = converted_data[idx]
        total_value += perform_operation(data_row, operation)

    print(total_value)