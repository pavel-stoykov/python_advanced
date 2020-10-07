import os

try:
    os.remove('my_first_file.txt')
    print('File is deleted')
except FileNotFoundError:
    print('File already deleted!')