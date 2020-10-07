import os

path = input()

files_dict = {}

for root, sub_dir, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extention = file.split('.')[-1]
        if extention not in files_dict:
            files_dict[extention] = []
        files_dict[extention].append(file)

with open('report.txt', "w") as fh_output:
    for extention, files in sorted(files_dict.items()):
        print(f'.{extention}', file=fh_output)
        for file in sorted(files):
            print(f'- - - {file}', file=fh_output)
