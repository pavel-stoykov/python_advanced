size_of_matrix = int(input())

matrix = [[] for row in range(size_of_matrix)]

for row in range(size_of_matrix):
    line = input().split(', ')
    for col in range(size_of_matrix):
        matrix[row].append(int(line[col]))

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

print(f'First diagonal: {", ".join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}')