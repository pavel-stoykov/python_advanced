username_count = int(input())

usernames = set()

for _ in range(username_count):
    username = input()
    if username not in usernames:
        usernames.add(username)

print('\n'.join(usernames))