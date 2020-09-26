from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
crash = deque()
crossroads = deque()
green_light_left = 0

while True:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        if cars:
            timer = green_light_duration 
            second_timer = free_window_duration
            copy_car = cars.popleft() 
            current_car = deque(copy_car)
            while timer:
                if not current_car:
                    if cars:
                        copy_car = cars.popleft()
                        current_car = deque(copy_car)
                    else:
                        break
                current_car.popleft()
                timer -= 1
            if current_car:
                while second_timer:
                        current_car.popleft()
                        second_timer -= 1
            if current_car:
                print('A crash happened!')
                print(f"{copy_car} Was hit at {current_car.popleft()}.")
                break
    else:
        car = command
        cars.append(car)
