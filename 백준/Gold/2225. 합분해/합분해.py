import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

v=[[0]*(m+1) for _ in range(n+1)]

for i in range(m+1):
    v[0][i]=1
    v[1][i]=i

for i in range(2,n+1):
    v[i][1]=1
    for j in range(2,m+1):
        for k in range(0,i+1):
            v[i][j]+=(v[i-k][j-1])%1000000000
            v[i][j]%=1000000000

print(v[n][m])