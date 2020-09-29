list_with_numbers = input().split('|')
l = [num.split() for num in list_with_numbers]
print(' '.join([' '.join(l[i]) for i in range(len(l) - 1, -1, -1)]))
