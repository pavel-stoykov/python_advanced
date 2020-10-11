from collections import deque
DATURA = 40
CHERRY = 60
SMOKE_DECOY = 120

bomb_effect = deque(int(x) for x in input().split(','))
bomb_casing = [int(x) for x in input().split(',')]

bombs_dict = {'Datura Bombs': 0,
              'Cherry Bombs': 0,
              'Smoke Decoy Bombs': 0}

is_succeeded = False

while True:
    if bomb_effect and bomb_casing:
        current_bomb_effect = bomb_effect.popleft()
        current_bomb_casing = bomb_casing.pop()
        bomb_material_sum = current_bomb_effect + current_bomb_casing
        if bomb_material_sum == DATURA:
            bombs_dict['Datura Bombs'] += 1
        elif bomb_material_sum == CHERRY:
            bombs_dict['Cherry Bombs'] += 1
        elif bomb_material_sum == SMOKE_DECOY:
            bombs_dict['Smoke Decoy Bombs'] += 1
        else:
            bomb_effect.appendleft(current_bomb_effect)
            bomb_casing.append(current_bomb_casing - 5)

        if bombs_dict['Datura Bombs'] >= 3 and bombs_dict['Cherry Bombs'] >= 3 and bombs_dict['Smoke Decoy Bombs'] >= 3:
            is_succeeded = True
            break

    else:
        break


if is_succeeded:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')
if bomb_effect:
    print(f'Bomb Effects: {", ".join(map(str, bomb_effect))}')
else:
    print('Bomb Effects: empty')
if bomb_casing:
    print(f'Bomb Casings: {", ".join(map(str, bomb_casing))}')
else:
    print('Bomb Casings: empty')
for name, value in sorted(bombs_dict.items()):
    print(f'{name}: {value}')