expression = input()
stack = []

for char in expression:
    if char == '(':
        stack.append('')

    for index in range(len(stack)):
        stack[index] += char

    if char == ')':
        sub_expresion = stack.pop()
        print(sub_expresion)