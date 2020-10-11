import collections
import itertools

substring = collections.deque(input().split())

find_colors = []

while substring:
    current_color = []
    first_substring = substring.popleft()
    if substring:
        last_substring = substring.pop()
    current_color = [first_substring + last_substring, last_substring + first_substring]
    for color in current_color:
        if color in 