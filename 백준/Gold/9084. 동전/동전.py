import sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    arr=list(map(int,sys.stdin.readline().rstrip().split()))
    m=int(sys.stdin.readline().rstrip())
    v=[0]*(m+1)
    v[0]=1
    for i in range(n):
        for j in range(arr[i],m+1):
            v[j]+=v[j-arr[i]]
    print(v[m])