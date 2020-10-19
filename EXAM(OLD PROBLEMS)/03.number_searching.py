def numbers_searching(*args):
    numbers = list(args)
    min_num = min(numbers)
    max_num = max(numbers)
    nums = []
    duplicate_num = []
    for num in range(min_num, max_num + 1):
        if numbers.count(num) > 1:
            duplicate_num.append(num)
        if num not in numbers:
            nums.append(num)
    nums.append(duplicate_num)
    return nums

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
