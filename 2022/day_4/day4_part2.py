def fill_set(start, end):
    new_set = set(range(start, end + 1))
    return new_set

fully_contain_count = 0
with open('input.txt', 'r') as infile:
    for line in infile:
        elf_1, elf_2 = line.strip().split(',')
        elf_1_set = fill_set(int(elf_1.split('-')[0]), int(elf_1.split('-')[1]))
        elf_2_set = fill_set(int(elf_2.split('-')[0]), int(elf_2.split('-')[1]))
        if(elf_1_set.intersection(elf_2_set)):
            fully_contain_count += 1

print(fully_contain_count)