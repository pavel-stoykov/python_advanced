def player_position_validator(player_position_column, player_position_row, new_player_position_column, new_player_position_row, lair, command):
    if 0 <= new_player_position_column < len(lair) and 0 <= new_player_position_row < len(lair):
        if command == 'U' or command == 'D':
            new_position = (new_player_position_row, player_position_column)
        elif command == 'L' or command == 'R':
            new_position = (player_position_row, new_player_position_column)
    else:
        return (player_position_row, player_position_column)


row_counter, column_counter = [int(x) for x in input().split()]

lair = [[] for x in range(row_counter)]
new_lair = lair

# read input for row of matrix
for row in range(row_counter):
    line = input()
    for char in line:
        lair[row].append(char)

# read player commands
commands = input()
list_of_comands = [command for command in commands]

# take a player position
for row in range(row_counter):
    for column in range(column_counter):
        if lair[row][column] == 'P':
            player_position_row = row
            player_position_column = column

for command in list_of_comands:
    new_player_position_row = player_position_row
    new_player_position_column = player_position_column
    if command == 'L':
        new_player_position_column = player_position_column - 1
        new_position = player_position_validator(
            player_position_column, player_position_row, new_player_position_column, new_player_position_row, lair, command)
        player_position_column = new_position[1]
    elif command == 'R':
        new_player_position_column = player_position_column + 1
        new_position = player_position_validator(
            player_position_column, player_position_row, new_player_position_column, new_player_position_row, lair, command)
        player_position_column = new_position[1]
    elif command == 'U':
        new_player_position_row = player_position_row - 1
        new_position = player_position_validator(
            player_position_column, player_position_row, new_player_position_column, new_player_position_row, lair, command)
        player_position_row = new_position[0]
    elif command == 'D':
        new_player_position_row = player_position_row + 1
        new_position = player_position_validator(
            player_position_column, player_position_row, new_player_position_column, new_player_position_row, lair, command)
        player_position_row = new_position[0]

print(f'{player_position_row}, {player_position_column}')
