from collections import deque


def next_second(h, minutes, sec):
    sec += 1
    if sec == 60:
        minutes += 1
        sec = 0
    if minutes == 60:
        h += 1
        minutes = 0
    if h == 24:
        h = 0
    return h, minutes, sec

robots_info = input().split(';')
time = list(map(int, input().split(':')))

available_robots = deque()
waiting_robots = deque()
robots_dict = {}
products = deque()

while True:
    command = input()
    if command == 'End':
        break
    product_name = command
    products.append(product_name)

for robot in robots_info:
    token = robot.split('-')
    robot_name = token[0]
    process_time = int(token[1])
    available_robots.append([robot_name, process_time])
    robots_dict[robot_name] = process_time

while products:
    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([robot_name, robots_dict[robot_name]])
        waiting_robots = [r for r in waiting_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()

    if not available_robots:
        products.append(current_product)
        continue

    current_robot = available_robots.popleft()
    print(f'{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]')
    waiting_robots.append(current_robot)