def find_strongest_eggs(*args):
    egg_sequence = args[0]
    num_of_sublist = args[1]
    list_of_sublist = [egg_sequence[i::num_of_sublist] for i in range(num_of_sublist)]
    storngest_eggs = []
    for sublist in list_of_sublist:
        is_strongest = False
        middle_of_subllist = len(sublist) // 2
        current_egg = sublist[middle_of_subllist]
        if sublist[middle_of_subllist - 1] < current_egg > sublist[middle_of_subllist + 1]:
            for i in range(1, len(sublist) - middle_of_subllist):
                right_egg = sublist[middle_of_subllist + i]
                left_egg = sublist[middle_of_subllist - i]
                if right_egg > left_egg:
                    is_strongest = True
                else:
                    is_strongest = False
                    break
            if is_strongest:
                storngest_eggs.append(current_egg)
    return storngest_eggs
test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
