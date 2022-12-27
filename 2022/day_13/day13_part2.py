packets_data = []

with open('input.txt', 'r') as infile:
    for line in infile:
        if line.strip() != '':
            packets_data.append(eval(line.strip()))

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
count = 1
for packet in packets_data:
    if compare_pairs(packet, [[2]]) <= 0:
        count += 1
indicies.append(count)

count = 2
for packet in packets_data:
    if compare_pairs(packet, [[6]]) <= 0:
        count += 1
indicies.append(count)

print('Product of indicies:', indicies[0] * indicies[1])


# print(compare_pairs([7,7,7], [[2]]))