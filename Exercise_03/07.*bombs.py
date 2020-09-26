def position_vaidator(damage_row, damage_column, field, is_valid):
    if 0 <= damage_row < len(field) and 0 <= damage_column < len(field):
        return True


def bomb_damage(bomb_value, field, bomb_row, bomb_column):
    field[bomb_row][bomb_column] = 0
    row_position = [-1, -1, -1, 0, 1, 1, 1, 0]
    column_position = [-1, 0, 1, 1, 1, 0, -1, -1]
    for idx in range(len(row_position)):
        is_valid = False
        damage_row = bomb_row + row_position[idx]
        damage_column = bomb_column + column_position[idx]
        is_valid = position_vaidator(damage_row, damage_column, field, is_valid)
        if is_valid:
            if field[damage_row][damage_column] > 0:
                field[damage_row][damage_column] -= bomb_value
    return field

size_of_field = int(input())

field = [[] for x in range(size_of_field)]

for row in range(size_of_field):
    line = [int(x) for x in input().split()]
    for col in range(size_of_field):
        field[row].append(line[col])

cordinates = input().split()

for cordinate in cordinates:
    token = cordinate.split(',')
    bomb_row = int(token[0])
    bomb_column = int(token[1])
    bomb_value = field[bomb_row][bomb_column]
    field = bomb_damage(bomb_value, field, bomb_row, bomb_column)
    

alive_cell = 0
total_sum = 0

for row in range(size_of_field):
    for col in range(size_of_field):
        if field[row][col] > 0:
            alive_cell += 1
            total_sum += field[row][col]
print(f'Alive cells: {alive_cell}')
print(f'Sum: {total_sum}')

for row in field:
    print(' '.join([str(x) for x in row]))