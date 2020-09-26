from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = deque(map(int, input().split(', ')))


total_time=0
is_all_customer_pass = True

while customers:
    current_customer=customers.popleft()
    if taxis:
        current_taxy=taxis.pop()
        if current_taxy >= current_customer:
            total_time += current_customer
        else:
            customers.appendleft(current_customer)
    else:
        customers.appendleft(current_customer)
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join(map(str, (customers)))}')
        is_all_customer_pass = False
        break
if is_all_customer_pass:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')