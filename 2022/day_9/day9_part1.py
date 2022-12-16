INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as infile:
    inputs = [line.rstrip() for line in infile]    

head_coords = [0, 0]
tail_pos = [0, 0]
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
    for d in range(0, dist):
        head_coords[movement[move_type]] += increment[m.split()[0]]
        curr_head_coord = head_coords[0], head_coords[1]
        head_coords_list.append(curr_head_coord)

def move_tail(curr_head_pos, prev_head_pos):
    if abs(curr_head_pos[0] - tail_pos[0]) > 1 or abs(curr_head_pos[1] - tail_pos[1]) > 1:
        tail_pos[0] += prev_head_pos[0] - tail_pos[0]
        tail_pos[1] += prev_head_pos[1] - tail_pos[1]

for move in inputs:
    move_head(move)

curr = head_coords_list[0]
prev = curr
for h in range(len(head_coords_list)):
    curr = head_coords_list[h]
    move_tail(curr, prev)
    tail_moves.append([tail_pos[0], tail_pos[1]])
    prev = curr

no_dupe_tail = []
for t in tail_moves:
    if t not in no_dupe_tail:
        no_dupe_tail.append(t)

# print(head_coords_list, '\n')
# print(tail_moves, '\n')
# print(no_dupe_tail)

#print(inputs)
print('Ans:', len(no_dupe_tail))

#   ATTEMPTS
# 6029 is too high
# 5933 is too low
# 5999 is too low
# 6026 is right