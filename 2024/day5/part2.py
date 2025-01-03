from collections import defaultdict, deque

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

def topological_sort(page):
    indegree = defaultdict(int)

    for update in page:
        if update in ordering_dict:
            for vertex in ordering_dict[update]:
                if vertex in page:
                    indegree[vertex] += 1

    for update in page:
        if update not in indegree:
            indegree[update] = 0

    q = deque([node for node in indegree if indegree[node] == 0])
    # print(indegree)
    sorted_page = []

    while q:
        node = q.popleft()
        sorted_page.append(node)
        for adjacent in ordering_dict[node]:
            if adjacent in page:
                indegree[adjacent] -= 1
                if indegree[adjacent] == 0:
                    q.append(adjacent)
    
    return [update for update in sorted_page if update in page]


# print(ordering_dict)
for page in instructions:
    update_rank = {}
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
                # print(page)
                fails += 1
                break
        except:
            prev = curr
            continue
        prev = curr

    if fails != 0:
        # print(page)
        sorted_page = topological_sort(page)
        # print(sorted_page)
        result += sorted_page[int(len(sorted_page) / 2)]

print(result)

# print(ordering_dict)