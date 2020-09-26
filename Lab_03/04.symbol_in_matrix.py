size_of_matrix = int(input())

matrix = [[] for x in range(size_of_matrix)]

is_find_occurance = False

for row in range(size_of_matrix):
    line = input()
    for j in range(size_of_matrix):
        matrix[row].append(line[j])

symbol = input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if symbol == matrix[i][j]:
            is_find_occurance = True
            break
    if is_find_occurance:
        break
if is_find_occurance:
    print(f'({i}, {j})')
else:
    print(f'{symbol} does not occur in the matrix')
