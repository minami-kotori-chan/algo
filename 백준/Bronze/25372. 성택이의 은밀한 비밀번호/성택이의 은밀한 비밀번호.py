import sys

n=int(sys.stdin.readline().rstrip())
for i in range(n):
    string = sys.stdin.readline().rstrip()
    if len(string)>=6 and len(string)<=9:
        print('yes')
    else:
        print('no')