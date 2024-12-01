with open('input.txt', 'r') as infile:
    lines = [line.strip() for line in infile.readlines()]

l1 = []
l2 = []

for i in lines:
    s = i.split('   ')
    l1.append(int(s[0]))
    l2.append(int(s[1]))

def ret_dict(l):
    c = {}
    for i in l:
        c[i] = c.get(i, 0) + 1
    return c

def main():
    d1 = ret_dict(l1)
    d2 = ret_dict(l2)
    t = 0
    for k in d1.keys():
        if k in d2.keys():
            t += k * d2.get(k) * d1.get(k)
    print(t)


if __name__ == '__main__':
    main()