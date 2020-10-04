from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())

bullet_counter = 0
total_bullet = 0

while bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    bullet_counter += 1
    total_bullet += 1
    if not bullets:
        break
    if bullet_counter == gun_barrel_size:
        print('Reloading!')
        bullet_counter = 0
    if not locks:
        break

locks_left = len(locks)
bullets_left = len(bullets)
bullets_cost = total_bullet * bullet_price
money_earned = intelligence_value - bullets_cost


if not locks:
    print(f'{bullets_left} bullets left. Earned ${money_earned}')
elif not bullets:
    print(f'Couldn\'t get through. Locks left: {locks_left}')
