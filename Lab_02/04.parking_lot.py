car_numbers = int(input())

parking = set()

for _ in range(car_numbers):
    direction, car_id = input().split(', ')
    if direction == 'IN':
        parking.add(car_id)
    elif direction == 'OUT':
        parking.remove(car_id)
if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')