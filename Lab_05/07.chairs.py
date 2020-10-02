from itertools import permutations, combinations

names = input().split(', ')
num = int(input())

perm = combinations(names, num)

for i in perm:
    print(', '.join(i))
