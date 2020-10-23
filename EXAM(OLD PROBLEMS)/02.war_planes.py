field_size = int(input())
battlefield = [input().split() for row in range(field_size)]

command_counter = int(input())
game_over = False
target_counter = 0
target = 0

for row in battlefield:
    for char in row:
        if char == 't':
            target += 1


def search_plane(battlefield):
    for row in range(field_size):
        for col in range(field_size):
            if battlefield[row][col] == 'p':
                return row, col


plane_position = search_plane(battlefield)


def move(dy, dx, cmd):
    global plane_position, game_over, target_counter
    y, x = plane_position
    new_y = y + dy
    new_x = x + dx
    if new_y > (field_size - 1) or new_y < 0 or new_x > (field_size - 1) or new_x < 0:
        return y, x
    at_pos = battlefield[new_y][new_x]
    if cmd == 'move':
        if at_pos == '.':
            battlefield[y][x] = '.'
            battlefield[new_y][new_x] = 'p'
            plane_position = (new_y, new_x)
        else:
            plane_position = (y, x)
    elif cmd == 'shoot':
        if at_pos == 't':
            target_counter += 1
        battlefield[new_y][new_x] = 'x'


directions = {
    'left': lambda: move(0, -step, cmd),
    'right': lambda: move(0, step, cmd),
    'up': lambda: move(-step, 0, cmd),
    'down': lambda: move(step, 0, cmd),
}

for _ in range(command_counter):
    command = input().split()
    cmd = command[0]
    direction = command[1]
    step = int(command[2])
    move_fn = directions[direction]
    move_fn()
    if target_counter > 0 and target - target_counter <= 0:
        break

left_targets = target - target_counter
if left_targets <= 0:
    print(f'Mission accomplished! All {target_counter} targets destroyed.')
else:
    print(f'Mission failed! {left_targets} targets left.')
for row in battlefield:
    print(' '.join(row))
