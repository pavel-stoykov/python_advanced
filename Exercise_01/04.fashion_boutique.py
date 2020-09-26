clothes_in_box = input().split()
capacity = int(input())

counter = 0
total_sum = 0

while len(clothes_in_box):

    curennt_clothes = int(clothes_in_box.pop())
    total_sum += curennt_clothes
    if total_sum > capacity:
        clothes_in_box.append(curennt_clothes)
        counter += 1
        total_sum = 0
    elif total_sum == capacity:
        counter += 1
        total_sum = 0
    elif not clothes_in_box:
        counter += 1
print(counter)
