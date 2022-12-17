import math

with open('input.txt', 'r') as infile:
    all_data = []
    monkey_data = {}
    count = 1
    for line in infile:
        if count == 1:
            monkey_data['name'] = line.strip().replace(':','').split()[1]
        elif count == 2:
            monkey_data['items'] = line.strip().replace(',','').split()[2:]
        elif count == 3:
            monkey_data['op'] = line.strip().split()[3:]
        elif count == 4:
            monkey_data['test'] = line.strip().split()[-1]
        elif count == 5:
            monkey_data['cond1'] = line.strip().split()[-1]
        elif count == 6:
            monkey_data['cond2'] = line.strip().split()[-1]
        if count == 7:
            monkey_data['inspect'] = 0
            all_data.append(monkey_data)
            monkey_data = {}
            count = 0
        count += 1
    all_data.append(monkey_data)
    monkey_data['inspect'] = 0
        
# [print(s) for s in all_data]
monkey_inspects = []
test = False
for _ in range(20):
    for data in all_data:
        d = 0
        for i in data['items']:
            # print(f'Monkey {data["name"]} inspecting... {i}')
            worry_level = 0
            temp_eq = [i if x == 'old' else x for x in data['op']]
            if temp_eq[1] == '+':
                worry_level = int(temp_eq[0]) + int(temp_eq[2])
            else:
                worry_level = int(temp_eq[0]) * int(temp_eq[2])
            worry_level = math.floor(worry_level / 3)
            # print(worry_level)
            if worry_level % int(data['test']) == 0:
                test = True
            else:
                test = False
            
            if test:
                for b in range(len(all_data)):
                    if all_data[b]['name'] == data['cond1']:
                        all_data[b]['items'].append(worry_level)
            else:
                for b in range(len(all_data)):
                    if all_data[b]['name'] == data['cond2']:
                        all_data[b]['items'].append(worry_level)
            data['inspect'] += 1
            d += 1

        if data['items'] != []:
            for dd in range(d):
                data['items'].pop(0)
        
        
    # print('Round', _)
    # [print(a) for a in all_data]

t = []
for a in all_data:
    t.append((a['name'], a['inspect']))

t.sort(key=lambda t: t[1], reverse=True)
print(t[0][1] * t[1][1])



# Reference        
# all_data[0]['items'].append('69')

#   ATTEMPTS
