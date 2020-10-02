from functools import reduce

def operate(op, *args):
    operators_dict = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    return reduce(operators_dict[op], args)
    # if op == "+":
    #    return operators_dict['+']
    # elif op == '-':
    #     return operators_dict['-']
    # elif op == '*':
    #     return operators_dict['*']
    # elif op == '/':
    #     return operators_dict['/']


print(operate("+", 1, 2, 3))
