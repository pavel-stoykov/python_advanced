def validate_player_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'P':
                return [row, col]


string = input()
matrix_size = int(input())

matrix = [[char for char in input()]for row in range(matrix_size)]

player_position = validate_player_position(matrix)

movment_count = int(input())

for _ in range(movment_count):

    direction = input()
    if direction == 'right':
        new_player_position = [player_position[0], player_position[1] + 1]
    elif direction == 'left':
        new_player_position = [player_position[0], player_position[1] - 1]
    elif direction == 'up':
        new_player_position = [player_position[0] - 1, player_position[1]]
    elif direction == 'down':
        new_player_position = [player_position[0] + 1, player_position[1]]

    if 0 <= new_player_position[0] < matrix_size and 0 <= new_player_position[1] < matrix_size:
        matrix[player_position[0]][player_position[1]] = '-'
        if matrix[new_player_position[0]][new_player_position[1]].isalpha():
            string += matrix[new_player_position[0]][new_player_position[1]]
            player_position = new_player_position
            last_simbol = matrix[player_position[0]][player_position[1]]
            matrix[new_player_position[0]][new_player_position[1]] = 'P'
    else:
        if last_simbol == string[-1]:
            string = string[:-1]
            matrix[player_position[0]][player_position[1]] = 'P'
            break
    player_position = new_player_position
    
print(string)
for row in matrix:
    print(''.join(row))
