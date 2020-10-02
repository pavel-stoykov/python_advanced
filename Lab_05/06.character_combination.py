from itertools import permutations

perm = permutations(list(input()))

for i in perm:
    print(''.join(i))