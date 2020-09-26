counter = int(input())

longest_set = []

for _ in range(counter):
    ranges = input().split('-')
    first_start, first_end = ranges[0].split(',')
    second_start, second_end = ranges[1].split(',')
    first_set = set([int(x) for x in range(int(first_start), int(first_end) + 1)])
    second_set = set([int(y) for y in range(int(second_start), int(second_end) + 1)])
    intersection = first_set & second_set

    if len(intersection) > len(longest_set):
        longest_set = intersection

print(f'Longest intersection is [{", ".join(map(str, longest_set))}] with length {len(longest_set)}')