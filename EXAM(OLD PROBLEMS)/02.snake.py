territory_size = int(input())

snake_territory = [[] for row in range(territory_size)]

burrow_position = []
food_counter = 0
is_over = False

for row in range(territory_size):
    line = input()
    for col in range(territory_size):
        snake_territory[row].append(line[col])

for row in range(territory_size):
    for col in range(territory_size):
        if snake_territory[row][col] == 'S':
            current_snake_position = [row, col]
        if snake_territory[row][col] == 'B':
            burrow_position.append([row, col])
new_snake_position = current_snake_position.copy()
while True:
    command = input()
    if command == 'up':
        new_snake_position[0] = current_snake_position[0] - 1
    elif command == 'down':
        new_snake_position[0] = current_snake_position[0] + 1
    elif command == 'left':
        new_snake_position[1] = current_snake_position[1] - 1
    elif command == 'right':
        new_snake_position[1] = current_snake_position[1] + 1
    if 0 <= new_snake_position[0] < territory_size and 0 <= new_snake_position[1] < territory_size:
        if snake_territory[new_snake_position[0]][new_snake_position[1]] == "B":
            for burrow in burrow_position:
                if new_snake_position == burrow:
                    snake_territory[burrow[0]][burrow[1]] = '.'
                    burrow_position.remove(burrow)
                    new_snake_position = burrow_position.pop()
                    snake_territory[new_snake_position[0]
                                    ][new_snake_position[1]] = 'S'
        elif snake_territory[new_snake_position[0]][new_snake_position[1]] == "*":
            food_counter += 1
            snake_territory[new_snake_position[0]][new_snake_position[1]] = "."
        else:
            snake_territory[new_snake_position[0]][new_snake_position[1]] = 'S'
        snake_territory[current_snake_position[0]
                        ][current_snake_position[1]] = '.'
        current_snake_position = new_snake_position.copy()
    else:
        is_over = True
        break

    if food_counter >= 10:
        snake_territory[current_snake_position[0]
                        ][current_snake_position[1]] = 'S'
        break

if is_over:
    print('Game over!')
else:
    print('You won! You fed the snake.')
print(f'Food eaten: {food_counter}')
for row in snake_territory:
    print(''.join(row))
