from collections import deque

male = deque(map(int, input().split()))  # input male intiger values
female = deque(map(int, input().split()))  # input female intiger values

matches = 0

while female:
    if not male:
        break
    current_female = female.popleft()
    current_male = male.pop()
    if current_female <= 0:
        male.append(current_male)
        continue
    if current_male <= 0:
        female.appendleft(current_female)
        continue
    if current_female % 25 == 0:
        female.popleft()
        male.append(current_male)
        continue
    if current_male % 25 == 0:
        male.pop()
        female.appendleft(current_female)
        continue
    if current_female != current_male:
        male.append(current_male - 2)
    else:
        matches += 1
print(f'Matches: {matches}')
if not male:
    print('Males left: none')
else:
    print(f'Males left: {", ".join(map(str, reversed(male)))}')
if not female:
    print('Females left: none')
else:
    print(f'Females left: {", ".join(map(str, female))}')
