board_size = int(input())

board = [[col for col in input()] for row in range(board_size)]

removed_knight = 0

while True:

    max_shots = 0
    knight_pos_max_shots = (0, 0)

    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'K':

                shoots = 0
                knight_pos_row = row
                knight_pos_col = col
                attack_pos_row = [-2, -1, 1, 2, 2, 1, -1, -2]
                attack_pos_col = [1, 2, 2, 1, -1, -2, -2, -1]

                for i in range(len(attack_pos_row)):
                    attack_knight_pos_row = knight_pos_row + attack_pos_row[i]
                    attack_knight_pos_col = knight_pos_col + attack_pos_col[i]
                    if 0 <= attack_knight_pos_row < board_size and 0 <= attack_knight_pos_col < board_size:
                        if board[attack_knight_pos_row][attack_knight_pos_col] == 'K':
                            shoots += 1

                if shoots > max_shots:
                    max_shots = shoots
                    knight_pos_max_shots = (knight_pos_row, knight_pos_col)

    if max_shots == 0:
        break

    board[knight_pos_max_shots[0]][knight_pos_max_shots[1]] = '0'
    removed_knight += 1

print(removed_knight)

# def position_validator(board_size, new_row, new_col):
#     if 0 <= new_row < board_size and 0 <= new_col < board_size:
#         return new_row, new_col
#     else:
#         return None


# def knight_battle(board, row, col, shoot_counter):
#     row_position = [-2, -2, -1, 1, 2, 2, 1]
#     col_position = [-1, 1, 2, 2, 1, -1, -2]
#     for index in range(len(row_position)):
#         new_row = row + row_position[index]
#         new_col = col + col_position[index]
#         current_position = position_validator(board_size, new_row, new_col)
#         if current_position:
#             current_r = current_position[0]
#             current_c = current_position[1]
#             if board[current_r][current_c] == 'K':
#                 # board[current_r][current_c] = '0'
#                 shoot_counter += 1
#     return shoot_counter


# board_size = int(input())

# board = [[] for _ in range(board_size)]
# total_shoots = 0
# shoot_counter = 0
# # TO DO
# # most_shoots_counter =

# for row in range(board_size):
#     line = input()
#     for char in line:
#         board[row].append(char)

# for row in range(board_size):
#     for col in range(board_size):
#         symbol = board[row][col]
#         if symbol == 'K':
#             total_shoots += knight_battle(board, row, col, shoot_counter)

# print(total_shoots)
