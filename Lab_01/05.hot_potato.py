from collections import deque

children = deque(input().split())
n_toss = int(input())

while len(children) > 1:
    children.rotate(-n_toss)
    looser = children.pop()
    print(f'Removed {looser}')

winner = children.pop()
print(f'Last is {winner}')