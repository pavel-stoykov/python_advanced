def read_list_int_input(separator = ' '):
    return [int(x) for x in input().split(separator)]

row_counter, column_counter = read_list_int_input(', ')

matrix = []

for row in range(row_counter):
    matrix.append(read_list_int_input())

sum_of_column = [0 for _ in range(column_counter)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum_of_column[j] += matrix[i][j]

print('\n'.join(map(str, sum_of_column)))

