string = input().split()

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}

find_colors = []

while string:
    first_substring = string.pop(0)
    if string:
        last_substring = string.pop()
    else:
        last_substring = ''

    first_string = first_substring + last_substring
    second_string = last_substring + first_substring

    if first_string in main_colors or first_string in secondary_colors:
        find_colors.append(first_string)
    elif second_string in main_colors or second_string in secondary_colors:
        find_colors.append(second_string)
    else:
        middle_of_string = len(string) // 2
        if len(first_substring) > 1:
            first_substring = first_substring[:-1]
            string.insert(middle_of_string, first_substring)
        if len(last_substring) > 1:
            last_substring = last_substring[:-1]
            string.insert(middle_of_string, last_substring)
for color in find_colors:
    if color in secondary_colors:
        if any(x not in find_colors for x in secondary_colors[color]):
            find_colors.remove(color)
print(find_colors)
