import os

while True:
    command = input()
    if command == 'End':
        break
    token = command.split('-')
    command = token[0]
    file_name = token[1]
    if command == 'Create':
        f = open(file_name, 'w')
        f.truncate(0)
    elif command == 'Add':
        content = token[2]
        try:
            with open(file_name, 'a') as fh:
                fh.write(f'{content}\n')
        except FileNotFoundError:
            with open(file_name, 'ax') as fh:
                fh.write(f'{content}\n')
    elif command == 'Replace':
        old_string = token[2]
        new_string = token[3]
        try:
            with open(file_name) as fh:
                filedata = fh.read()
                filedata = filedata.replace(old_string, new_string)
                with open(file_name, 'w') as fh_write:
                    fh_write.write(filedata)
        except FileNotFoundError:
            print('An error occurred')
    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
