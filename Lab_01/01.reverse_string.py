string = input()
stack  = []

for char in string:
    stack.append(char)

while len(stack) > 0:
    print(stack.pop(), end='')