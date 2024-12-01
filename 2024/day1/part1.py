with open('input.txt', 'r') as infile:
    lines = [line.strip() for line in infile.readlines()]

l1 = []
l2 = []

for i in lines:
    s = i.split('   ')
    l1.append(int(s[0]))
    l2.append(int(s[1]))

l1.sort()
l2.sort()

t = 0

for i in range(0, len(l1)):
    t += abs(l1[i] - l2[i])


print(t)