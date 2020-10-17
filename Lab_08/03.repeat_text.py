try:
    text = input()
    counter = int(input())
    print(text*counter)
except ValueError:
    print('Variable times must be an integer')
