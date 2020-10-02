from itertools import combinations, permutations, chain, product

numbers = [x for x in input().split(', ')]

n = len(numbers)

comb = product('+-', repeat=n)

for i in comb:
    expresion = ''.join(chain(*zip(i, numbers)))
    result = eval(expresion)
    print(f'{expresion}={result}')