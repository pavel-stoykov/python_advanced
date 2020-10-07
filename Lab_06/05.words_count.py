import re

with open('words.txt') as fh_words:
    words = fh_words.read().split()

with open('input.txt') as fh_text:
    text = fh_text.read()

word_occurances = {}

for word in words:
    matches = re.findall(fr"[\s-]({word})[\s.?!,]", text, re.IGNORECASE + re.MULTILINE)
    word_occurances[word.lower()] = len(matches)

with open('output.txt', 'w') as fh_output:
    for word, occurances in sorted(word_occurances.items(), key=lambda t: -t[1]):
        print(f'{word} - {occurances}', file=fh_output)