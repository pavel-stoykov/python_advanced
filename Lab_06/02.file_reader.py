total_sum = 0

with open('numbers.txt', 'r') as fh:
    for num in fh:
        total_sum += int(num)

print(total_sum)
