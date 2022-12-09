from anytree import Node, RenderTree

INPUT_FILE = 'input.txt'

root = Node('dir /')
with open(INPUT_FILE, 'r') as infile:
    curr_dir = root
    prev_dir = root
    read_files = False
    dir_files = []
    dir_sum = 0
    dir_sums = []
    dir_path = ['/']
    TOTAL_DISK_SIZE = 70_000_000
    UPDATE_SPACE = 30_000_000
    for line in infile:
        curr = line.strip()

        if read_files:
            if curr.startswith('$ cd'):
                read_files = False
                for d in dir_files:
                    if d.split()[0].isdigit():
                        dir_sum += int(d.split()[0])
                    Node(d, parent=curr_dir)
                dir_sums.append(['/'.join(dir_path), dir_sum])
                dir_sum = 0
                dir_files = []
            else:
                dir_files.append(curr)
                if(curr.split()[0].isdigit()):
                    for i in range(len(dir_path)):
                        curr_path = '/'.join(dir_path[:i + 1])
                        for s in dir_sums:
                            if s[0] == curr_path:
                                s[1] += int(curr.split()[0])
                                break

        if curr == '$ ls':
            read_files = True

        elif curr == '$ cd ..':
            curr_dir = prev_dir
            prev_dir = prev_dir.parent
            dir_path.pop()
            

        elif curr.startswith('$ cd') and curr != '$ cd /':
            prev_dir = curr_dir
            found = False
            for i in curr_dir.children:
                if 'dir ' + curr.split(' ')[2] == i.name:
                    curr_dir = i
                    found = True
                    break
                
            if not found:
                curr_dir = Node('dir ' + curr.split(' ')[2], parent=prev_dir)
            
            dir_path.append(curr_dir.name.split()[1])

            

    for d in dir_files:
        Node(d, parent=curr_dir)
        if d.split()[0].isdigit():
            dir_sum += int(d.split()[0])

    dir_sums.append(['/'.join(dir_path), dir_sum])


print()
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

full_space = dir_sums[0][1]
unused_space = TOTAL_DISK_SIZE - full_space
needed_space = UPDATE_SPACE - unused_space
possible_delete = []
for s in dir_sums:
    if s[1] >= needed_space:
        possible_delete.append(s[1])

print(possible_delete)
print(min(possible_delete))


#   ATTEMPTS:
# 42036703 is too high
# 2108829 is too high
# 2050735 is right