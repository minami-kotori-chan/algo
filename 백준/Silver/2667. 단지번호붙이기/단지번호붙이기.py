import sys

n=int(sys.stdin.readline().rstrip())
graph=[]
for _ in range(n):
    graph.append(sys.stdin.readline().rstrip())

visited=[[0]*n for _ in range(n)]
count=0

def dfs(row,col):
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    if graph[row][col]==0:
        return
    visited[row][col]=1
    count[0]+=1
    for i in range(4):
        if row+dy[i]>=n or row+dy[i]<0 or col+dx[i]>=n or col+dx[i]<0:
            continue
        if visited[row+dy[i]][col+dx[i]]==0 and graph[row+dy[i]][col+dx[i]]=='1':
            dfs(row+dy[i],col+dx[i])

result_count=0
result=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1' and visited[i][j]==0:
            count=[0]
            dfs(i,j)
            result_count+=1
            result.append(count)
print(result_count)
result.sort()
for i in result:
    print(*i)