from collections import defaultdict

with open('input.txt', 'r') as infile:
    data = infile.read()

data = data.split('\n\n')
ordering_dict = defaultdict(list)

ordering_rules = [[int(i) for i in d.split('|')] for d in data[0].split('\n')]
instructions = [[int(i) for i in d.split(',')] for d in data[1].split('\n')]

for o in ordering_rules:
    # print(o)
    ordering_dict[o[0]].append(o[1])

result = 0

for page in instructions:
    fails = 0
    curr = 0
    prev = curr
    for c, i in enumerate(page):
        curr = i
        # if first element in the list, we don't compare it
        if c == 0:
            prev = curr
            continue
        try:
            if prev in ordering_dict[curr]:
                print(page)
                fails += 1
                break
        except:
            prev = curr
            continue
        prev = curr

    if fails != 0:
        # print(page)
        
        result += page[int(len(page) / 2)]

print(result)

# print(ordering_dict)