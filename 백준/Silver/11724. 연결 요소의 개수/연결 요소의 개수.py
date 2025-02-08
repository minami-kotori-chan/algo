import sys

sys.setrecursionlimit(5000)
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    s,v=map(int,sys.stdin.readline().rstrip().split())
    arr[s][v]=1
    arr[v][s]=1

v=[0]*(n+1)
def dfs(start):
    if v[start]==1:
        return 0
    v[start]=1
    for i in range(1,n+1):
        if arr[start][i]==1 and v[i]==0:
            dfs(i)
    return 1
sum=0
for i in range(1,n+1):
    sum+=dfs(i)
print(sum)