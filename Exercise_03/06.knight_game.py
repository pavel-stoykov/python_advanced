def position_validator(board_size, new_row, new_col):
    if 0 <= new_row < board_size and 0 <= new_col < board_size:
        return new_row, new_col
    else:
        return None


def knight_battle(board, row, col, shoot_counter):
    row_position = [-2, -2, -1, 1, 2, 2, 1]
    col_position = [-1, 1, 2, 2, 1, -1, -2]
    for index in range(len(row_position)):
        new_row = row + row_position[index]
        new_col = col + col_position[index]
        current_position = position_validator(board_size, new_row, new_col)
        if current_position:
            current_r = current_position[0]
            current_c = current_position[1]
            if board[current_r][current_c] == 'K':
                # board[current_r][current_c] = '0'
                shoot_counter += 1
    return shoot_counter


board_size = int(input())

board = [[] for _ in range(board_size)]
total_shoots = 0
shoot_counter = 0
# TO DO 
# most_shoots_counter = 

for row in range(board_size):
    line = input()
    for char in line:
        board[row].append(char)

for row in range(board_size):
    for col in range(board_size):
        symbol = board[row][col]
        if symbol == 'K':
            total_shoots += knight_battle(board, row, col, shoot_counter)

print(total_shoots)
