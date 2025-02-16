from collections import deque
import sys

m,n,h=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,sys.stdin.readline().rstrip().split())))

q=deque()
visited=[[[-1]*m for _ in range(n)]for _ in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                q.append([i,j,k])
                visited[i][j][k]=0
dh=[0,0,0,0,1,-1]
dr=[-1,0,1,0,0,0]
dc=[0,1,0,-1,0,0]
while q:
    cur_h,cur_row,cur_col=q.popleft()
    for i in range(6):
        height=cur_h+dh[i]
        row=cur_row+dr[i]
        col=cur_col+dc[i]
        if height>=h or height<0 or row>=n or row<0 or col>=m or col<0:
            continue
        if visited[height][row][col]!=-1 or graph[height][row][col]==-1:
            continue
        q.append([height,row,col])
        visited[height][row][col]=visited[cur_h][cur_row][cur_col]+1
is_valid=True
result=visited[0][0][0]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k]==-1 and graph[i][j][k]!=-1:
                is_valid=False
            result=max(result,visited[i][j][k])
if is_valid:
    print(result)
else:
    print(-1)