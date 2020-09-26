def position_validator(start_row, start_col, new_row, new_col, field, command):
    if 0 <= new_row < len(field) and 0 <= new_col < len(field):
        if command == 'up' or command == 'down':
            return (new_row, start_col)
        elif command == 'left' or command == 'right':
            return (start_row, new_col)
    else:
        return (start_row, start_col)


field_size = int(input())
commands = input().split()

field = [[] for row in range(field_size)]

coal_counter = 0

for row in range(field_size):
    line = input().split()
    for column in range(field_size):
        field[row].append(line[column])

for line in field:
    coal_counter += line.count('c')

for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == 's':
            start_row = row
            start_col = col
            break

is_collect = False
is_game_over = False

for command in commands:
    new_row = start_row
    new_col = start_col
    if command == 'up':
        new_row = start_row - 1
        new_position = position_validator(
            start_row, start_col, new_row, new_col, field, command)
        start_row = new_position[0]
    elif command == 'down':
        new_row = start_row + 1
        new_position = position_validator(
            start_row, start_col, new_row, new_col, field, command)
        start_row = new_position[0]
    elif command == 'right':
        new_col = start_col + 1
        new_position = position_validator(
            start_row, start_col, new_row, new_col, field, command)
        start_col = new_position[1]
    elif command == 'left':
        new_col = start_col - 1
        new_position = position_validator(
            start_row, start_col, new_row, new_col, field, command)
        start_col = new_position[1]
    if field[new_position[0]][new_position[1]] == 'c':
        field[new_position[0]][new_position[1]] = '*'
        coal_counter -= 1
        if coal_counter == 0:
            is_collect = True
            break
    elif field[new_position[0]][new_position[1]] == 'e':
        is_game_over = True
        break

if is_collect:
    print(f'You collected all coals! ({start_row}, {start_col})')
elif is_game_over:
    print(f"Game over! ({start_row}, {start_col})")
else:
    print(f'{coal_counter} coals left. ({start_row}, {start_col})')
