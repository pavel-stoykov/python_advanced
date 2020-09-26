from collections import deque

pumps_number = int(input())

pumps = deque()


index = 0

for _ in range(pumps_number):
    pumps_info = list(map(int, (input().split())))
    pumps.append(pumps_info[0] - pumps_info[1])


while index < pumps_number:
    tank = 0
    for i in range(pumps_number):
        tank += pumps[i]
        if tank < 0:
            pumps.rotate(-1)
            index += 1
            break
    else:
        break
print(index)
