command = input()
numbers = [int(x) for x in input().split()]

odd_numbers = []
even_numbers = []
n = len(numbers)

for num in numbers:
    if command == 'Odd' and num % 2 !=0:
        odd_numbers.append(num)
    elif command == 'Even' and num % 2 == 0:
        even_numbers.append(num)

if command == 'Odd':
    print(sum(odd_numbers)*n)
elif command == 'Even':
    print(sum(even_numbers)*n)