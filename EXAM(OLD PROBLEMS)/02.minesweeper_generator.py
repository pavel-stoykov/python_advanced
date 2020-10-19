size_of_matrix = int(input())
bomb_numbers = int(input())

matrix = [[0 for _ in range(size_of_matrix)] for row in range(size_of_matrix)]

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


for _ in range(bomb_numbers):
    position = input()
    y = int(position[1])
    x = int(position[4])
    matrix[y][x] = '*'
    for i in range(len(dy)):
        exp_y, exp_x = y+dy[i], x+dx[i]
        if 0 <= exp_y < size_of_matrix and 0 <= exp_x < size_of_matrix and matrix[exp_y][exp_x] != '*':
            matrix[exp_y][exp_x] += 1


for row in matrix:
    print(f'{" ".join(map(str, row))}')
