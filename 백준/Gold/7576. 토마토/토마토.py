from collections import deque
import sys

m,n=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
visit_cost=[[0]*m for _ in range(n)]

def bfs():
    q=deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                q.append([i,j,1])
                visit_cost[i][j]=1
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    while q:
        cur_row,cur_col,cost=q.popleft()
        for i in range(4):
            if cur_row+dr[i]>=n or cur_row+dr[i]<0 or cur_col+dc[i]>=m or cur_col+dc[i]<0 or graph[cur_row+dr[i]][cur_col+dc[i]]==-1:
                continue
            if graph[cur_row+dr[i]][cur_col+dc[i]]==1:
                if visit_cost[cur_row+dr[i]][cur_col+dc[i]]==0 or visit_cost[cur_row+dr[i]][cur_col+dc[i]]>cost:
                    visit_cost[cur_row+dr[i]][cur_col+dc[i]]=cost
                    q.append([cur_row+dr[i],cur_col+dc[i],visit_cost[cur_row+dr[i]][cur_col+dc[i]]])
            else:
                if visit_cost[cur_row+dr[i]][cur_col+dc[i]]==0 or visit_cost[cur_row+dr[i]][cur_col+dc[i]]>cost+1:
                    visit_cost[cur_row+dr[i]][cur_col+dc[i]]=cost+1
                    q.append([cur_row+dr[i],cur_col+dc[i],visit_cost[cur_row+dr[i]][cur_col+dc[i]]])
                
bfs()

result=visit_cost[0][0]
is_valid=True
for i in range(n):
    for j in range(m):
        if visit_cost[i][j]==0 and graph[i][j]!=-1:
            is_valid=False
            break
        result=max(result,visit_cost[i][j])

if is_valid:
    print(result-1)
else:
    print(-1)