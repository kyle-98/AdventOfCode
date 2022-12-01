all_elves = []

with open('input.txt', 'r') as infile:
    elf = []
    for line in infile:
        if line.strip() == '':
            all_elves.append(elf)
            elf = []
        else:
            elf.append(int(line.strip()))
    
    all_elves.append(elf)

elves_sums = []

for elf in all_elves:
    num_sum = 0
    for num in elf:
        num_sum += num
    elves_sums.append(num_sum)


elves_sums.sort(reverse=True)
print('Part 1:', elves_sums[0])
top_three = [elves_sums[0], elves_sums[1], elves_sums[2]]
print('Part 2:', sum(top_three))
