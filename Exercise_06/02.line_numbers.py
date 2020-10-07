with open('text.txt') as fh_input:
    with open('output.txt', 'w') as fh_otput:
        for index, line in enumerate(fh_input):
            words = line.split()
            total_char = 0
            punkt_mark_counter = 0
            for word in words:
                for el in "'-.,?!":
                    if el in word:
                        punkt_mark_counter += 1
                total_char += len(word)
            print(f'Line {index + 1}: {line} ({total_char - punkt_mark_counter}) ({punkt_mark_counter})', file=fh_otput)