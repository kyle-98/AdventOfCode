INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as infile:
    rows_matrix = []
    for line in infile:
        t = []
        for l in line.strip():
            t.append(int(l))
        rows_matrix.append(t)

columns_matrix = list(zip(*rows_matrix))
scenic_scores = []

for row in range(1, len(rows_matrix) - 1):
    for col in range(1, len(columns_matrix[0]) - 1):
        curr_score = 1

        for x_movement, y_movement  in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            distance = 0
            temp_row = row + x_movement
            temp_col = col + y_movement

            while 0 <= temp_row < len(rows_matrix) and 0 <= temp_col < len(columns_matrix[0]):
                distance += 1
                if(rows_matrix[row][col] <= rows_matrix[temp_row][temp_col]):
                    break
                temp_row += x_movement
                temp_col += y_movement

            curr_score *= distance
        scenic_scores.append(curr_score)

print(scenic_scores)
print(max(scenic_scores))

#   ATTEMPTS
# 332640 is right