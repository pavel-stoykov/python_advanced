from collections import defaultdict

list_of_numbers = map(float, input().split())

nums_dict = defaultdict(int)

for num in list_of_numbers:
    nums_dict[num] += 1

for number, counter in nums_dict.items():
    print(f'{number} - {counter} times')
