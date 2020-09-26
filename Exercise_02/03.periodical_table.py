lines_count = int(input())

compounds_set = set()

for _ in range(lines_count):
    compounds = input().split()
    for compound in compounds:
        if compound not in compounds_set:
            compounds_set.add(compound)

print('\n'.join(compounds_set))