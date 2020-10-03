# from collections import defaultdict

list_of_numbers = map(float, input().split())

# nums_dict = defaultdict(int)
nums_dict = {}

for num in list_of_numbers:
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

for number, counter in nums_dict.items():
    print(f'{number} - {counter} times')
