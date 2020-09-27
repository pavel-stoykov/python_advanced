start_number = int(input())
end_number = int(input())

numbers = [num for num in range(start_number, end_number + 1)]

divisors = [x for x in range(2, 11)]

filtred_num = [num for num in numbers  if any([num % div == 0 for div in divisors])]


print(filtred_num)

