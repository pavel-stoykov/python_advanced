from collections import deque


def list_manipulator(*args):
    list_numbers = args[0]
    command = args[1]
    possition = args[2]
    number = 0
    if command == 'add':
        numbers = deque(args[3:])
        while numbers:
            if possition == 'beginning':
                current_num = numbers.pop()
                list_numbers.insert(0, current_num)
            elif possition == 'end':
                current_num = numbers.popleft()
                list_numbers.append(current_num)
    elif command == 'remove' and possition == 'beginning':
        if len(args) > 3:
            number = int(args[3])
            for _ in range(number):
                list_numbers = list_numbers[1::]
        else:
            list_numbers = list_numbers[1::]
    elif command == 'remove' and possition == 'end':
        if len(args) > 3:
            number = int(args[3])
            for _ in range(number):
                list_numbers = list_numbers[:-1]
        else:
            list_numbers = list_numbers[:-1]
    return list_numbers                 
print(list_manipulator([1,2,3], "remove", "end", 2))                


