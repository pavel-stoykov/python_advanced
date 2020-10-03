heroes_items = {x: [] for x in input().split(', ')}
item_cost = {name: 0 for name, value in heroes_items.items()}

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    name = tokens[0]
    item = tokens[1]
    cost = int(tokens[2])
    if item not in heroes_items[name]:
        heroes_items[name].append(item)
        item_cost[name] += cost

print('\n'.join(
    [f'{name} -> Items: {len(items)}, Cost: {item_cost[name]}'
     for name, items in heroes_items.items()]
)
)
