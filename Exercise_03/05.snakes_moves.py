from collections import deque

row_counter, column_counter = [int(x) for x in input().split()]

text = deque(input())

matrix = []

for row in range(row_counter):
    matrix.append([])
    for col in range(column_counter):
        matrix[row].append(' ')

for row in range(row_counter):
    for col in range(column_counter):
        char = text.popleft()
        if row % 2 == 0:
            matrix[row][col] = char
        else:
            new_col = column_counter - col - 1
            matrix[row][new_col] = char
        text.append(char)

for line in matrix:
    print(''.join(line))