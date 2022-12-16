INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as infile:
    inputs = [line.rstrip() for line in infile]    

head_coords = [0, 0]
tail_pos_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
head_coords_list = [(0, 0)]
tail_moves = []

def move_head(m):
    movement = {
        'R':0,
        'L':0,
        'U':1,
        'D':1
    }
    increment = {
        'R': 1,
        'L': -1,
        'U': 1,
        'D': -1
    }

    dist = int(m.split()[1])
    move_type = m.split()[0]
    for _ in range(0, dist):
        head_coords[movement[move_type]] += increment[m.split()[0]]
        curr_head_coord = head_coords[0], head_coords[1]
        head_coords_list.append(curr_head_coord)
    
def move_tail(c_pos, tail_pos):
    if abs(c_pos[0] - tail_pos[0]) > 1 or abs(c_pos[1] - tail_pos[1]) > 1:
        if c_pos[0] != tail_pos[0]:
            tail_pos[0] += (c_pos[0] - tail_pos[0]) // abs(c_pos[0] - tail_pos[0])
        if c_pos[1] != tail_pos[1]:
            tail_pos[1] += (c_pos[1] - tail_pos[1]) // abs(c_pos[1] - tail_pos[1])

for move in inputs:
    move_head(move)

curr_input = head_coords_list
for c, t in enumerate(tail_pos_list):
    x = []
    #print(f'curr_input {c + 1} ->', curr_input)
    for a in range(len(curr_input)):
        move_tail(curr_input[a], t)
        x.append((t[0], t[1]))
    tail_moves.append(x)
    curr_input = tail_moves[len(tail_moves) - 1]

# print(tail_pos_list, '\n')

# for c, t in enumerate(tail_moves):
#     print(f'Tail {c + 1}:', t, '\n')


no_dupe_tail = []
for t in tail_moves[8]:
    if t not in no_dupe_tail:
        no_dupe_tail.append(t)

# print(head_coords_list, '\n')
print('no dupe tail:', no_dupe_tail)

#print(inputs)
print('Ans:', len(no_dupe_tail))

#   ATTEMPTS
