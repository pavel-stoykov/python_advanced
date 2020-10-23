def get_repeating_DNA(test):
    repated_sequence = []
    if len(test) > 10:
        for i in range(len(test) - 10):
            current_sequence = test[i:i + 10]
            for j in range(i + 1, i + 11):
                temp_sequence = test[j: j + 10]
                if temp_sequence == current_sequence and temp_sequence not in repated_sequence:
                    repated_sequence.append(current_sequence)
                    break
    return repated_sequence


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
