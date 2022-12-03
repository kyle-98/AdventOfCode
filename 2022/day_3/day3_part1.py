#each side is equal chars


def count(intersect):
    if intersect.isupper():
        return ord(intersect) - 38
    else:
        return ord(intersect) - 96

intersect_sum = 0
with open("input.txt", "r") as infile:
    for line in infile:
        rucksack = line.strip()
        left, right = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        intersect = ''.join(set(left).intersection(right))
        
        if(intersect):
            intersect_sum += count(intersect)

print(intersect_sum)