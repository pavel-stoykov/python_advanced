row_counter = int(input())

matrix = [[int(num) for num in input().split(', ')] for row in range(row_counter)]

even_matrix = [[matrix[row][col] for col in range(len(matrix[row])) if matrix[row][col] % 2== 0]for row in range(len(matrix))]

print(even_matrix)