def read_list_int_input():
    return [int(x) for x in input().split()]


row_counter, column_counter = read_list_int_input()

matrix = []

for row in range(row_counter):
    matrix.append(read_list_int_input())


biggest_sum_of_submatrix = -999999999
biggest_submatrix = []

for i in range(len(matrix) -2):
    for j in range(len(matrix[i]) - 2):
        submatrix = []
        sum_of_submatrix = 0    
        submatrix = [[matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
        [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],
        [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]]
    
        for line in submatrix:
            sum_of_submatrix += sum(line)

        if sum_of_submatrix > biggest_sum_of_submatrix:
            biggest_sum_of_submatrix = sum_of_submatrix
            biggest_submatrix = submatrix

print(f'Sum = {biggest_sum_of_submatrix}')
for row in biggest_submatrix:
    print(' '.join([str(x) for x in row]))