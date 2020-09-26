counter_of_names = int(input())

set_of_names = set()

for _ in range(counter_of_names):
    name = input()
    if name not in set_of_names:
        set_of_names.add(name)

print('\n'.join(set_of_names))