from collections import deque

DOLL = 150
WOODEN_TRAIN = 250
TEDDY_BEAR = 300
BICYCLE = 400


materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
gifts = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic_level:
    total_magic_level = 0
    current_materials = materials.pop()
    current_magic_level = magic_level.popleft()
    total_magic_level = current_materials * current_magic_level
    if total_magic_level == DOLL:
        gifts['Doll'] += 1
    elif total_magic_level == WOODEN_TRAIN:
        gifts['Wooden train'] += 1
    elif total_magic_level == TEDDY_BEAR:
        gifts['Teddy bear'] += 1
    elif total_magic_level == BICYCLE:
        gifts['Bicycle'] += 1
    elif current_magic_level == 0:
        materials.append(current_materials)
        continue
    elif current_materials == 0:
        magic_level.appendleft(current_magic_level)
        continue
    elif current_magic_level == 0 and current_materials == 0:
        continue
    elif total_magic_level < 0:
        materials.append(current_magic_level + current_materials)
    elif total_magic_level > 0:
        materials.append(current_materials + 15)

if gifts['Doll'] >= 1 and gifts['Wooden train'] >= 1\
        or gifts['Teddy bear'] >= 1 and gifts['Bicycle'] >= 1:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')
for name, value in sorted(gifts.items()):
    if value == 0:
        continue
    else:
        print(f'{name}: {value}')
