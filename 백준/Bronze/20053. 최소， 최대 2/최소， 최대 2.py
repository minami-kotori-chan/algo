import sys
t=int(sys.stdin.readline().rstrip())
for i in range(t):
    n=int(sys.stdin.readline().rstrip())
    arr=list(map(int,sys.stdin.readline().rstrip().split()))
    print(min(arr),max(arr))