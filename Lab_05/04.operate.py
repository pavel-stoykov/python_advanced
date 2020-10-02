from functools import reduce

def operate(op, *args):
    operators_dict = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    return reduce(operators_dict[op], args)


print(operate("+", 1, 2, 3))
