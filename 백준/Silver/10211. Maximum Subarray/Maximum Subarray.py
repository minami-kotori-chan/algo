import sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    arr=list(map(int,sys.stdin.readline().rstrip().split()))
    v=[0]*n
    v[0]=arr[0]
    for i in range(n):
        v[i]=max(arr[i],v[i-1]+arr[i])
    print(max(v))