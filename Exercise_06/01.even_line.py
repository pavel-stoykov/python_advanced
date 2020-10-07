with open("text.txt") as fh_line:
    for index, line in enumerate(fh_line):
        new_line = []
        if index % 2 == 0:
            for el in "-.,?!":
                line = line.replace(el, '@')
            words = line.split()
            while words:
                new_line.append(words.pop())
            print(' '.join(new_line))
                        