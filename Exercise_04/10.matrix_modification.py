size_of_matrix = int(input())

matrix = [[int(x) for x in input().split()] for row in range(size_of_matrix)]

while True:
    command = input()
    if command == 'END':
        break
    tokens = command.split()
    command = tokens[0]
    row = int(tokens[1])
    col = int(tokens[2])
    value = int(tokens[3])
    if 0 <= row < size_of_matrix and 0 <= col < size_of_matrix:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(' '.join(str(x) for x in row))
