# charachters = input().split(', ')

# ascii_dictionary = {char: ord(char) for char in charachters}


start_ascii_value, end_ascii_value = [int(x) for x in input().split(', ')]

ascii_dict = {chr(value): value for value in range(
    start_ascii_value, end_ascii_value)}


for char, value in ascii_dict.items():
    print(f'{char} : {value}')
