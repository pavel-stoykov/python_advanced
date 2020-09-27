text = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'O', "E", 'I', 'U']

new_text = ''.join([char for char in text if char not in vowels])

print(new_text)
