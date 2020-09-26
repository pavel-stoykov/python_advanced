number_of_quaries = int(input())

stack = []

for _ in range(number_of_quaries):
    command = input()
    if ' ' in command:
        token = command.split()
        command = token[0]
        if command == '1':
            stack.append(int(token[1]))
    if not stack:
        continue
    else:
        if command == '2':
                stack.pop()
        elif command == '3':
            max_number = max(stack)
            print(max_number)
        elif command == '4':
            min_number = min(stack)
            print(min_number)

reverse_stack = reversed(stack)

print(", ".join([str(x) for x in reverse_stack]))