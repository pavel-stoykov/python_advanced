first_num_of_element_set, second_num_of_element_set = map(int, input().split())

first_set = set()
second_set = set()

for _ in range(first_num_of_element_set):
    current_num = int(input())
    first_set.add(current_num)

for _ in range(second_num_of_element_set):
    current_num = int(input())
    second_set.add(current_num)

result_set = first_set & second_set

print('\n'.join(map(str, result_set)))