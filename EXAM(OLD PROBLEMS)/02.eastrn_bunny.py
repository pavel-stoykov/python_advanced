filed_size = int(input())

field = [input().split() for row in range(filed_size)]

for row in range(filed_size):
    for col in range(filed_size):
        if field[row][col] == 'B':
            bunny_position_row = row
            bunny_position_col = col

directions = ['up', 'down', 'left', 'right']
max_eggs = -9999999999999
max_eggs_direct = ''
max_eggs_pos = []


for direct in directions:
    current_eggs = 0
    current_eggs_position = []
    if direct == 'up':
        for row in range(bunny_position_row - 1, -1, -1):
            if field[row][bunny_position_col].isdigit():
                current_eggs += int(field[row][bunny_position_col])
                current_eggs_position.append([row, bunny_position_col])
            elif field[row][bunny_position_col] == 'X':
                break
    elif direct == 'down':
        for row in range(bunny_position_row + 1, filed_size):
            if field[row][bunny_position_col].isdigit():
                current_eggs += int(field[row][bunny_position_col])
                current_eggs_position.append([row, bunny_position_col])
            elif field[row][bunny_position_col] == 'X':
                break
    elif direct == 'left':
        for col in range(bunny_position_col - 1, -1, -1):
            if field[bunny_position_row][col].isdigit():
                current_eggs += int(field[bunny_position_row][col])
                current_eggs_position.append([bunny_position_row, col])
            elif field[bunny_position_row][col] == 'X':
                break
    elif direct == 'right':
        for col in range(bunny_position_col + 1, filed_size):
            if field[bunny_position_row][col].isdigit():
                current_eggs += int(field[bunny_position_row][col])
                current_eggs_position.append([bunny_position_row, col])
            elif field[bunny_position_row][col] == 'X':
                break
    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        max_eggs_direct = direct
        max_eggs_pos = current_eggs_position

print(max_eggs_direct)
for pos in max_eggs_pos:
    print(pos)
print(max_eggs)