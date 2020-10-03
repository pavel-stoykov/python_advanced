from collections import deque

cups_capacity = deque(int(x) for x in input().split())
filled_bottles = [int(x) for x in input().split()]
waste_water = 0
is_cups_end = False

while filled_bottles:
    if cups_capacity:
        difference = 0
        current_bottle = filled_bottles.pop()
        current_cup = cups_capacity.popleft()
        difference = current_bottle - current_cup
        if difference >= 0:
            waste_water += difference
        else:
            current_cup = abs(difference)
            cups_capacity.appendleft(current_cup)
    else:
        is_cups_end = True
        break

if is_cups_end:
    print(f'Bottles: {" ".join(map(str, filled_bottles))}')
    print(f'Wasted litters of water: {waste_water}')
else:
    print(f'Cups: {" ".join(map(str, cups_capacity))}')
    print(f'Wasted litters of water: {waste_water}')