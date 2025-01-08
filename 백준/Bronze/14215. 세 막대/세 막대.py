import sys

b1,b2,b3 = map(int,sys.stdin.readline().rstrip().split())

if max(b1,b2,b3) < (b1+b2+b3-max(b1,b2,b3)):
    print(b1+b2+b3)
else:
    print((b1+b2+b3-max(b1,b2,b3))*2-1)