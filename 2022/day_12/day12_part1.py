import numpy as np

class Item:
    def __init__(self, row, col, dist) -> None:
        self.row = row
        self.col = col
        self.dist = dist

def min_distance(matrix):
    s = Item(0, 0, 0)
    s.row = int(np.where(matrix == 'S')[0])
    s.col = int(np.where(matrix == 'S')[1])
    visited = [ [False for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
    queue = []
    queue.append(s)
    visited[s.row][s.col] = True

    while len(queue) != 0:
        s = queue.pop(0)
        if(matrix[s.row, s.col] == 'E'):
            return s.dist
        
        if is_valid(s.row - 1, s.col, s.row, s.col, matrix, visited):
            queue.append(Item(s.row - 1, s.col, s.dist + 1))
            visited[s.row - 1][s.col] = True
        
        if is_valid(s.row + 1, s.col, s.row, s.col, matrix, visited):
            queue.append(Item(s.row + 1, s.col, s.dist + 1))
            visited[s.row + 1][s.col] = True
        
        if is_valid(s.row, s.col - 1, s.row, s.col, matrix, visited):
            queue.append(Item(s.row, s.col - 1, s.dist + 1))
            visited[s.row][s.col - 1] = True
        
        if is_valid(s.row, s.col + 1, s.row, s.col, matrix, visited):
            queue.append(Item(s.row, s.col + 1, s.dist + 1))
            visited[s.row][s.col + 1] = True
    return -696969

        
def is_valid(new_x, new_y, old_x, old_y, matrix, visited):
    old_matrix_ord = ord(matrix[old_x, old_y])
    if old_matrix_ord == ord('S'):
        old_matrix_ord = 97
    try:
        new_matrix_ord = ord(matrix[new_x, new_y])
        if new_matrix_ord == ord('E'):
            new_matrix_ord = 122
    except:
        pass
    
    if ( (new_x >= 0 and new_y >= 0) and (new_x < len(matrix) and new_y < len(matrix[0])) and (old_matrix_ord - new_matrix_ord >= -1 and visited[new_x][new_y] == False) ):
        return True
    return False

matrix = np.genfromtxt('input.txt', delimiter=1, dtype=str)
print('Shortest Path:', min_distance(matrix))

# get value of S in the matrix
# print(np.where(matrix == 'S'))