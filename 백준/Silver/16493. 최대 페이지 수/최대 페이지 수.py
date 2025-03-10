import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for _ in range(m)]
v=[[0]*(m+1) for _ in range(n+1)]
for i in range(m):
    arr[i]=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(1,n+1):
    for j in range(1,m+1):
        if i-arr[j-1][0]<0:
            v[i][j]=v[i][j-1]
            continue
        v[i][j]=max(v[i][j-1],v[i-arr[j-1][0]][j-1]+arr[j-1][1])
print(v[n][m])