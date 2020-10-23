size_of_matrix = int(input())
bomb_numbers = int(input())

matrix = [[0 for _ in range(size_of_matrix)] for row in range(size_of_matrix)]


def bobmb_position(position):
    y = ''
    x = ''
    for i in range(1, len(position)):
        if position[i] != ',':
            y += str(position[i])
        else:
            for j in range(i + 2, len(position) - 1):
                x += str(position[j])
            break
    return int(y), int(x)


dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


for _ in range(bomb_numbers):
    position = input()
    y, x = bobmb_position(position)
    matrix[y][x] = '*'
    for i in range(len(dy)):
        exp_y, exp_x = y+dy[i], x+dx[i]
        if 0 <= exp_y < size_of_matrix and 0 <= exp_x < size_of_matrix and matrix[exp_y][exp_x] != '*':
            matrix[exp_y][exp_x] += 1


for row in matrix:
    print(f'{" ".join(map(str, row))}')
