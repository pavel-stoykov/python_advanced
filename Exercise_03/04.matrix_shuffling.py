def read_list_int_input(separator=' '):
    return [int(x) for x in input().split(separator)]


row_counter, column_counter = read_list_int_input()

matrix = []
for row in range(row_counter):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break
    tokens = command.split()
    if len(tokens) == 5 and tokens[0] == 'swap':
        
        command = tokens[0]
        row_1 = int(tokens[1])
        col_1 = int(tokens[2])
        row_2 = int(tokens[3])
        col_2 = int(tokens[4])
        if (0 <= row_1 < row_counter) and (0 <= row_2 < row_counter) and (0 <= col_1 < column_counter) and (0 <= col_2 < column_counter):

            first_number = matrix[row_1][col_1]
            second_number = matrix[row_2][col_2]
            matrix[row_1][col_1] = second_number
            matrix[row_2][col_2] = first_number
            for i in matrix:
                print(' '.join(map(str, i)))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')