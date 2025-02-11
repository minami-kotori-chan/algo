from collections import deque
import sys

m,n=map(int,sys.stdin.readline().rstrip().split())
str_graph=[]
for i in range(n):
    str_graph.append(sys.stdin.readline().rstrip())
graph=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        graph[i][j]=ord(str_graph[i][j])-ord('0')

q=deque()
q.append([0,0])
visited=[[-1]*m for _ in range(n)]
visited[0][0]=0
dr=[-1,0,1,0]
dc=[0,1,0,-1]
while q:
    cur_row,cur_col=q.popleft()
    cost=visited[cur_row][cur_col]
    for i in range(4):
        if cur_row+dr[i]>=n or cur_row+dr[i]<0 or cur_col+dc[i]>=m or cur_col+dc[i]<0:
            continue
        if visited[cur_row+dr[i]][cur_col+dc[i]]==-1 or visited[cur_row+dr[i]][cur_col+dc[i]]>cost+graph[cur_row+dr[i]][cur_col+dc[i]]:
            q.append([cur_row+dr[i],cur_col+dc[i]])
            visited[cur_row+dr[i]][cur_col+dc[i]]=cost+graph[cur_row+dr[i]][cur_col+dc[i]]
print(visited[n-1][m-1])