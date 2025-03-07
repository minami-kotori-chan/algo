import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
v=[[0]*(m+1) for _ in range(n+1)]
v[1][1]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 and j==1:
            continue
        v[i][j]=(v[i][j-1]+v[i-1][j]+v[i-1][j-1])%1000000007
print(v[n][m])