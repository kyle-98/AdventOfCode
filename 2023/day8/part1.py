import re

class Node():
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

    def find_id(search_id, nodes):
        for i in range(0, len(nodes) - 1):
            if nodes[i].id == search_id:
                return nodes[i]


def main():
    with open('input.txt', 'r') as input_file:
        data = [i.rstrip() for i in input_file]
    
    nodes = []
    instructions = data[0]
    for i in range(2, len(data)):
        t = data[i].split(' = ')
        tt = re.sub(r'\(|\)', '', t[1])
        t2 = tt.split(', ')
        nodes.append(Node(
            id=t[0],
            left=t2[0],
            right=t2[1]
        ))
    
    curr_node_id = 'AAA'
    c = 0
    # print(Node.find_id('BBB', nodes))

    this_node = Node.find_id(curr_node_id, nodes)
    while curr_node_id != 'ZZZ':
        for i in instructions:
            if i == 'R':
                curr_node_id = this_node.right
                this_node = Node.find_id(this_node.right, nodes)
            else:
                curr_node_id = this_node.left
                this_node = Node.find_id(this_node.left, nodes)
            
            c += 1
    print(c)
                


        
    

if __name__ == '__main__':
    main()