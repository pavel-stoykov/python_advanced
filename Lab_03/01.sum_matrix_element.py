def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

row_counter, column_counter = read_int_list_from_input(', ')

# matrix = [0 for x in range(row_counter)]
matrix = []

for row in range(row_counter):
    matrix.append(read_int_list_from_input(', '))

total_sum = 0

for curr_sum in matrix:
    current_sum = sum(curr_sum)
    total_sum += current_sum

print(total_sum)
print(matrix)