from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
crash = deque()
crossroads = deque()
green_light_left = 0
car_counter = 0
is_crashed = False

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
                        car_counter +=1
                    else:
                        break
                current_car.popleft()
                timer -= 1
            if current_car:
                while second_timer and current_car:
                        current_car.popleft()
                        second_timer -= 1
            if current_car:
                print('A crash happened!')
                print(f"{copy_car} was hit at {current_car.popleft()}.")
                is_crashed = True
                break
            else:
                car_counter +=1
    else:
        car = command
        cars.append(car)

if not is_crashed:
    print('Everyone is safe.')
    print(f'{car_counter} total cars passed the crossroads.')