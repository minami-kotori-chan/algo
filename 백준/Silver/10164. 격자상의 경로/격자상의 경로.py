import sys
n,m,k=map(int,sys.stdin.readline().rstrip().split())
v=[[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
graph=[[0]*(m+1) for _ in range(n+1)]
count=1
for i in range(1,n+1):
    for j in range(1,m+1):
        graph[i][j]=count
        count+=1

v[1][1][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 and j==1:
            continue
        v[i][j][0]=v[i-1][j][0]+v[i][j-1][0]
        v[i][j][1]=v[i-1][j][1]+v[i][j-1][1]
        if k!=0 and graph[i][j]==k:
            v[i][j][1]=v[i][j][0]
if k==0:
    print(v[n][m][0])
else:
    print(v[n][m][1])