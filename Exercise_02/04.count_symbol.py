text = input()

array = []
for char in text:
    array.append(char)

array.sort()

char_and_occurance = {}

for char in array:
    if char not in char_and_occurance:
        char_and_occurance[char] = 0
    char_and_occurance[char] += 1

for char, occurance in char_and_occurance.items():
    print(f'{char}: {occurance} time/s')