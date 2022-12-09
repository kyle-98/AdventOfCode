from anytree import Node, RenderTree

INPUT_FILE = 'input.txt'

"""
TESTING: 

main = Node('main')
main_items = [Node('dir a', parent=main), Node('14848514 b.txt', parent=main), Node('8504156 c.dat', parent=main), Node('dir d', parent=main)]
a_items = [Node('die e', parent=main_items[0]), Node('29116 f', parent=main_items[0]), Node('2557 g', parent=main_items[0]), Node('62596 h.lst', parent=main_items[0])]
e_items = [Node('584 i', parent=a_items[0])]
d_items = [Node('4060174 j', parent=main_items[len(main_items) - 1]), Node('8033020 d.log', parent=main_items[len(main_items) - 1]), Node('5626152 d.ext', parent=main_items[len(main_items) - 1]), Node('7214296 k', parent=main_items[len(main_items) - 1])]

#for pre, fill, node in RenderTree(main):
#    print("%s%s" % (pre, node.name))


$ cd e
$ ls
50 e.exe
50 x.exe
$ cd d
$ ls
50 e.exe
50 x.exe
$ cd f
$ ls
50 e.exe
50 x.exe

"""

root = Node('dir /')
with open(INPUT_FILE, 'r') as infile:
    curr_dir = root
    prev_dir = root
    read_files = False
    dir_files = []
    dir_sum = 0
    dir_sums = []
    dir_path = ['/']
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
                """
                if curr_dir.parent != None:
                    #print(curr_dir.name, curr_dir.parent, prev_dir.name, curr_dir.parent.name)
                    
                    for s in dir_sums[::-1]:
                        if curr_dir.parent.name in s:
                            s[1] += dir_sum
                            break
                """
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


    """
    for s in dir_sums[::-1]:
        if curr_dir.parent.name in s:
            s[1] += dir_sum
            break
    """
print()
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

#dir_sums[0] = sum(dir_sums[1:]) + dir_sums[0]

print(dir_sums)



under_sums = []
for s in dir_sums:
    if s[1] <= 100000:
        under_sums.append(s[1])

print('Ans: ', sum(under_sums))



"""
new_sum = 0
new_sums = []
rev_root_desc = root.descendants[::-1]


count = 1
for d in root.descendants:
    if d.name.startswith('dir'):
        print(d)


prev_parent = rev_root_desc[0].parent
for d in rev_root_desc:
    if not d.name.startswith('dir') and prev_parent == d.parent:
        new_sum += int(d.name.split()[0])
        prev_parent = d.parent

    elif prev_parent == d.parent:
        new_sum += int(d.name.split()[0])
        prev_parent = d.parent
    
    elif prev_parent != d.parent:
        new_sums.append(new_sum)
        new_sum = 0    
        prev_parent = d.parent
        
print(root.descendants)

   returns tuple of entire tree
root.descendants

   returns name at bottom of tree
print(root.descendants[len(root.descendants) - 1].name)

   returns parent of descendant
print(root.descendants[len(root.descendants) - 1].parent)


for r in root.children:
    if r.name.startswith('dir'):
        print(r)
"""     

#   ATTEMPTS:
# 658579 is too low
# 775863 is too low
# 1002295 not right
# 1430771 not right
# 1325919 right