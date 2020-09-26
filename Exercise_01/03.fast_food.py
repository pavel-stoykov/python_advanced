from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

bigest_order = max(orders)
print(bigest_order)

while orders:
    order = orders.popleft()

    if food_quantity >= order:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break

if not orders:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(map(str, orders))}')    
