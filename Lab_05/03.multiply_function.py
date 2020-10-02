from functools import reduce


def multiply(*args):
    return reduce(lambda a, b: a*b, args)


print(multiply(4, 5, 6, 1, 3))
