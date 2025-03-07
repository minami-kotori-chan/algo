import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
v=[[1]*n for _ in range(n)]
for i in range(1,n):
    for j in range(1,i+1-1):
        v[i][j]=v[i-1][j-1]+v[i-1][j]
print(v[n-1][k-1])