def read_list_int_input(separator=" "):
    return [int(x) for x in input().split(separator)]


row_counter, column_counter = read_list_int_input(', ')

matrix = []

for row in range(row_counter):
    matrix.append(read_list_int_input(', '))

biggest_sum_submatrix = 0
biggest_submatrix = []

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        
        current_sum = 0
        submatrix = [[matrix[i][j],  matrix[i][j + 1]],
                     [matrix[i+1][j], matrix[i + 1][j+1]]]
        current_sum = sum([sum(row) for row in submatrix])

        if biggest_sum_submatrix < current_sum:
            biggest_sum_submatrix = current_sum
            biggest_submatrix = submatrix


for row in biggest_submatrix:
    print(' '.join(map(str, row)))

print(biggest_sum_submatrix)
