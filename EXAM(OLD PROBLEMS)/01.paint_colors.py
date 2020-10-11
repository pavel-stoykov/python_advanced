from collections import deque
from itertools import product

main_colors = ['red', 'yellow', 'blue']
seconadary_colors = ['orange', 'purple', 'green'] 

substring = deque(input().split())

find_colors = []

while substring:
    current_color = []
    first_substring = substring.popleft()
    if substring:
        last_substring = substring.pop()
        current_color = [first_substring + last_substring, last_substring + first_substring]
    else:
        color = first_substring

    for color in current_color:
        if color in seconadary_colors:
            if color == 'orange' and 'red' in find_colors and 'yellow' in find_colors:
                find_colors.append(color)
            elif color == 'purple' and 'red' in find_colors and 'blue' in find_colors:
                find_colors.append(color)
            elif color == 'green' and 'blue' in find_colors and 'yellow' in find_colors:
                find_colors.append(color)
        if color in main_colors:
            find_colors.append(color)
            break
    # first_substring = first_substring[:-1]
    # last_substring = last_substring[:-1]
    # color = first_substring + last_substring
    # middle = len(substring) // 2
    # substring.insert(middle, color)
print(find_colors)