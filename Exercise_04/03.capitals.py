countries = input().split(', ')
cities = input().split(', ')

d = {countries[x]:cities[x] for x in range(len(countries))}
 
[print(f'{key} -> {value}') for key, value in d.items()]
    