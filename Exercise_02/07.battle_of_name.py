counter = int(input())

odd_numbers = set()
even_numbers = set()

for idx in range(1, counter + 1):
    name = input()
    sum_of_char = sum([ord(char) for char in name]) // idx
    if sum_of_char % 2 == 0:
        even_numbers.add(sum_of_char)
    else:
        odd_numbers.add(sum_of_char)

if sum(odd_numbers) == sum(even_numbers):
    sum_of_set = odd_numbers | even_numbers
    print(', '.join(map(str, sum_of_set)))
elif sum(odd_numbers) > sum(even_numbers):
    different_values = odd_numbers - even_numbers
    print(', '.join(map(str, different_values)))
else:
    symmetric_difference = even_numbers ^ odd_numbers
    print(', '.join(map(str, symmetric_difference)))