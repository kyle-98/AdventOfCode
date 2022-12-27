packets_data = []

with open('input.txt', 'r') as infile:
    data = infile.read().split('\n\n')

for d in data:
    packets_data.append(d.split('\n'))
        
for pair in packets_data:
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])

# print(packets_data)

def compare_pairs(left, right):
    if left == []:
        if right == []:
            return 0
        else:
            return -1

    if right == []:
        return 1

    if isinstance (left, list):
        if isinstance (right, list):
            lists = compare_pairs(left[0], right[0])
            if lists:
                return lists
            else:
                return compare_pairs(left[1:], right[1:])
        return compare_pairs(left, [right])

    if isinstance (right, list):
        return compare_pairs([left], right)

    if left < right:
        return -1
    elif right < left:
        return 1
    else:
        return 0

indicies = []
for index, pair in enumerate(packets_data, 1):
    if compare_pairs(pair[0], pair[1]) <= 0:
        indicies.append(index)
print('Sum of indicies:', sum(indicies))