from collections import deque


def add(a, b):
    
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def devision(a, b):
    return a // b


expression_string = input().split()

numbers = deque()
result = 0

for char in expression_string:
    if char.isdigit() or len(char) >= 2:
        numbers.append(int(char))
    else:
        operator = char
        while numbers:
            if result:
                a = result
            else:
                a = numbers.popleft()
            if numbers:
                b = numbers.popleft()
            else:
                b = result 
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = subtract(a, b)
            elif operator == '*':
                result = multiply(a, b)
            elif operator == '/':
                result = devision(a, b)
print(result)