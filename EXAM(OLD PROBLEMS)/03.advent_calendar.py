def fix_calendar(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(1,n):
            if numbers[j-1] > numbers[j]:
                (numbers[j-1], numbers[j]) = (numbers[j], numbers[j-1])
    return numbers

numbers = [-2, 3, 1]
fixed = fix_calendar(numbers)
print(fixed)