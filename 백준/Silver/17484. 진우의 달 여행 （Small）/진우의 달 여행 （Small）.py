import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
v=[[[float('inf')]*3 for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(m):
    for j in range(3):
        v[0][i][j]=graph[0][i]
for i in range(1,n):
    for j in range(m):
        if j>0:
            v[i][j][0]=min(v[i-1][j-1][1],v[i-1][j-1][2])+graph[i][j]
        if j<m-1:
            v[i][j][2]=min(v[i-1][j+1][0],v[i-1][j+1][1])+graph[i][j]
        v[i][j][1]=min(v[i-1][j][0],v[i-1][j][2])+graph[i][j]
result=v[n-1][0][0]
for i in range(m):
    for j in range(3):
        result=min(result,v[n-1][i][j])
print(result)