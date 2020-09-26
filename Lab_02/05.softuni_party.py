guest_numbers = int(input())

guest_list = set()

for _ in range(guest_numbers):
    name = input()
    guest_list.add(name)

while True:
    command = input()
    if command == 'END':
        break
    else:
        guest_come_to_party = command
        guest_list.remove(guest_come_to_party)
print(len(guest_list))
print('\n'.join(sorted(guest_list)))
