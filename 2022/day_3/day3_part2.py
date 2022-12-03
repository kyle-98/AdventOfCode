
def convert_chars(intersect):
    if intersect.isupper():
        return ord(intersect) - 38
    else:
        return ord(intersect) - 96

intersect_sum = 0
count = 1
group = []
with open("input.txt", "r") as infile:
    for line in infile:
        if count == 3:
            group.append(line.strip())
            ruck_1, ruck_2, ruck_3 = group[0], group[1], group[2]
            intersect_1 = ''.join(set(ruck_1).intersection(ruck_2))
            intersect_2 = ''.join(set(intersect_1).intersection(ruck_3))
            intersect_sum += convert_chars(intersect_2)
            count = 0
            group = []
        else:
            group.append(line.strip())

        
        count += 1

    
print(intersect_sum)