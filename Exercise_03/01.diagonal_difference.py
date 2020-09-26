size_of_matrix = int(input())

matrix = []

for row in range(size_of_matrix):
    line = [int(x) for x in input().split()]
    matrix[row].append(line)

primari_diagonal_sum = 0
secondary_diagonal_sum = 0

for row in range(len(matrix)):
    col = row
    primari_diagonal_sum += matrix[row][col]
    # for column in range(len(matrix[row])):
    #     if row == column:
    #         primari_diagonal_sum += matrix[row][column]
    #         break

for row in range(len(matrix)):
    col = size_of_matrix - 1 - row
    secondary_diagonal_sum += matrix[row](col)
    # for column in range(len(matrix[row])):
    #     if column == len(matrix[row]) - row - 1:
    #         secondary_diagonal_sum += matrix[row][column]
    #         break

abs_difference_beetwen_diagonals = abs(primari_diagonal_sum - secondary_diagonal_sum)
print(abs_difference_beetwen_diagonals)