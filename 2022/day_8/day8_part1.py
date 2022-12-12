INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as infile:
    rows_matrix = []
    for line in infile:
        t = []
        for l in line.strip():
            t.append(int(l))
        rows_matrix.append(t)

columns_matrix = list(zip(*rows_matrix))
count = ((len(rows_matrix[0]) - 2) * 2) + ((len(columns_matrix[0])) * 2)
debug_list_row = []
debug_list_col = []
x = 1
for row in range(1, len(rows_matrix) - 1):
    for col in range(1, len(columns_matrix) - 1):
        #print(rows_matrix[r][c], columns_matrix[c][r]) || or all(rows_matrix[row][col] > rows_matrix[row][r] for r in range(rows_matrix[row].index(rows_matrix[row][col]), len(rows_matrix[row]) - 1))
        #first check left, then check right, then check top, then check bottom
       
        if (all(rows_matrix[row][col] > rows_matrix[row][r] for r in range(0, col)) or 
            all(rows_matrix[row][col] > rows_matrix[row][r] for r in range(col + 1, len(rows_matrix[row])))):
            
            #debug_list_row.append([rows_matrix[row][col], x])
            count += 1
        
        elif (all(rows_matrix[row][col] > rows_matrix[c][col] for c in range(0, row)) or 
            all(rows_matrix[row][col] > rows_matrix[c][col] for c in range(row + 1, len(rows_matrix[col])))):
            #debug_list_col.append([rows_matrix[row][col], x])
            count += 1

        x += 1
#print(debug_list_row)
#print(debug_list_col)
[print(*m) for m in rows_matrix][0]
print()
[print(*m) for m in columns_matrix][0]  
print()
print('Visible trees:', count)

"""
elif(all(columns_matrix[row][col] > columns_matrix[row][c] for c in range(0, col)) or
    all(columns_matrix[row][col] > columns_matrix[row][c] for c in range(col + 1, len(columns_matrix[row])))):

    debug_list_col.append([columns_matrix[row][col], x])
    count += 1
    print(columns_matrix[row])
"""

#   ATTEMPTS
# 2071 is too high
# 1859 is right