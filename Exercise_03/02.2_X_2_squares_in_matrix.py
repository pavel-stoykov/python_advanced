def read_list_int_input(separator=' '):
    return [int(x) for x in input().split(separator)]


row_counter, column_counter = read_list_int_input()

matrix = []

for row in range(row_counter):
    matrix.append([x for x in input().split()])

sub_matrix = []
ocuurance_counter = 0

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        sub_matrix = [[matrix[i][j], matrix[i][j + 1]],
                      [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        sub_matrix_symbol = sub_matrix[0][0]
        if sub_matrix_symbol == sub_matrix[0][1] and sub_matrix_symbol == sub_matrix[1][1] and sub_matrix_symbol == sub_matrix[1][0]:
            ocuurance_counter += 1

print(ocuurance_counter)


