from collections import deque

water_in_dispenser = int(input())
people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        name = command
        people.append(name)

while True:
    command = input()
    if command.isdigit():
        water_to_drink = int(command)
        person = people.popleft()
        if water_in_dispenser >= water_to_drink:
            water_in_dispenser -= water_to_drink
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif command.startswith('refill '):
        refill_dispenser = int(command.split()[1])
        water_in_dispenser += refill_dispenser
    else:
        break

print(f'{water_in_dispenser} liters left')