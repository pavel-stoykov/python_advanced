bunker_items = {category: {} for category in input().split(', ')}

line_counter = int(input())

for line in range(line_counter):
    line = input().split(' - ')
    category = line[0]
    item_name = line[1]
    performance = line[2].split(';')
    quantity = performance[0]
    quality = performance[1]
    token_quantity = quantity.split(':')
    token_quality = quality.split(':')
    quantity = int(token_quantity[1])
    quality = int(token_quality[1])
    bunker_items[category][item_name] = (quantity, quality)

count_items = 0
quality_sum = 0
categories_count = len(bunker_items)

for name, items in bunker_items.items():
    for item, value in items.items():
        count_items += value[0]
        quality_sum += value[1]
print(f'Count of items: {count_items}')
print(f'Average quality: {(quality_sum/categories_count):.2f}')

for name, items in bunker_items.items():
    print(f'{name} -> {", ".join(items)}')