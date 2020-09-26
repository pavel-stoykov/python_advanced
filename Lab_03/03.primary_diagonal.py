def read_list_int_input(separataor = ' '):
    return [int(x) for x in input().split(separataor)]

size_of_matrix = int(input())

matrix = []

for row in range(size_of_matrix):
    matrix.append(read_list_int_input())

sum_prymari_diagonal = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum_prymari_diagonal += matrix[i][j]
            break

print(sum_prymari_diagonal)