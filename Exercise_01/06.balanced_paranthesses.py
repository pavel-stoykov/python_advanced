parantheses = input()
stack = []

is_not_parantheses = False

for char in parantheses:
    if char == '(' or char == '[' or char == '{':
        stack.append(char)
    else:
        if not stack:
            is_not_parantheses = True
            break
        current_char = stack.pop()
        if current_char == '(' and char == ')':
            continue
        elif current_char == '[' and char == ']':
            continue
        elif current_char == '{' and char == '}':
            continue
        else:
            is_not_parantheses = True
            break

if is_not_parantheses:
    print('NO')
else:
    print('YES')
