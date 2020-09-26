from collections import deque, defaultdict
DATURA_BOMB = 40
CHERRY_BOMB = 60
SMOKE_DECOY_BOMB = 120


bomb_effect = deque(map(int, input().split(', ')))
bomb_casings = deque(map(int, input().split(', ')))

bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
is_not_enought_material = False

while bomb_effect:
    bomb_result = 0
    current_bomb_effect = bomb_effect.popleft()
    if not bomb_casings:
        is_not_enought_material = True
        break   
    current_bomb_casing = bomb_casings.pop()
    bomb_result = current_bomb_effect + current_bomb_casing
    if bomb_result == DATURA_BOMB:
        bombs['Datura Bombs'] += 1
    elif bomb_result == CHERRY_BOMB:
        bombs['Cherry Bombs'] += 1
    elif bomb_result == SMOKE_DECOY_BOMB:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effect.appendleft(current_bomb_effect)
        bomb_casings.append(current_bomb_casing - 5)
    if bombs['Datura Bombs'] > 2 and bombs['Cherry Bombs'] > 2 and bombs['Smoke Decoy Bombs'] > 2:
        print('Bene! You have successfully filled the bomb pouch!')
        break

if is_not_enought_material or not bomb_effect:
    print('You don\'t have enough materials to fill the bomb pouch.')

if bomb_effect:
    print(f'Bomb Effects: {", ".join(map(str, bomb_effect))}')
else:
    print('Bomb Effects: empty')
if bomb_casings:
    print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')
else:
    print('Bomb Casings: empty')

for name, value in sorted(bombs.items()):
    print(f'{name}: {value}')