search_counter = 0

phonebook = {}

while True:
    command = input()
    if command.isdigit():
        search_counter = int(command)
        break
    name, number = command.split('-')
    phonebook[name] = number

for _ in range(search_counter):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')


