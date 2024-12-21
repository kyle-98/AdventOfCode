
with open('test_input.txt', 'r') as infile:
    data = infile.read()

data = data.split('\n\n')
ordering_dict = {}

ordering_rules = [[int(i) for i in d.split('|')] for d in data[0].split('\n')]
instructions = [[int(i) for i in d.split(',')] for d in data[1].split('\n')]

for o in ordering_rules:
    print(o)
    if o[0] not in ordering_dict:
        ordering_dict[o[0]] = [o[1]]
    else:
        ordering_dict[o[0]].append(o[1])


print(instructions)