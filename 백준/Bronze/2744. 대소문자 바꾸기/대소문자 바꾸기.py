import sys

for i in sys.stdin.readline().rstrip():
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')