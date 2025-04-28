import sys

n=int(sys.stdin.readline().rstrip())
if n%10==n//10:
    print(1)
else:
    print(0)