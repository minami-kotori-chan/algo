from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

q=deque()
visited=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            q.append([i,j])
            visited[i][j]=0
        elif graph[i][j]==0:
            visited[i][j]=0
dr=[-1,0,1,0]
dc=[0,1,0,-1]
while q:
    cur_row,cur_col=q.popleft()
    for i in range(4):
        row=cur_row+dr[i]
        col=cur_col+dc[i]
        if row>=n or row<0 or col>=m or col<0:
            continue
        if visited[row][col]!=-1:
            continue
        visited[row][col]=visited[cur_row][cur_col]+1
        q.append([row,col])
for i in visited:
    print(*i)