numbers = [int(x) for x in input().split()]

positiv_num = []
negative_num = []

for num in numbers:
    if num >= 0:
        positiv_num.append(num)
    else:
        negative_num.append(num)

print(sum(negative_num))
print(sum(positiv_num))

if abs(sum(negative_num)) > sum(positiv_num):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
