row_counter = int(input())

matrix = [[int(num) for num in input().split(', ')] for row in range(row_counter)]

flatt_matrix = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row]))]

print(flatt_matrix)