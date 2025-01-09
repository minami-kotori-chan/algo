import sys

a1,a0 = map(int,sys.stdin.readline().rstrip().split())
c=int(sys.stdin.readline().rstrip())
n0=int(sys.stdin.readline().rstrip())

if c-a1>0:
    if (c-a1)*n0>=a0:
        print(1)
    else:
        print(0)
elif c-a1==0 and a0<=0:
    print(1)
else:
    print(0)