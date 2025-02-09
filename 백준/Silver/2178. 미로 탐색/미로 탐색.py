from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
    graph.append(sys.stdin.readline().rstrip())
visit=[[0]*m for _ in range(n)]

def bfs(row=0,col=0):
    q=deque()
    q.append([row,col,1])
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    while q:
        cur_row,cur_col,cost=q.popleft()
        if cur_row==n-1 and cur_col==m-1:
            print(cost)
            break
        for i in range(4):
            if cur_row+dr[i]>=n or cur_row+dr[i]<0 or cur_col+dc[i]>=m or cur_col+dc[i]<0:
                continue
            if visit[cur_row+dr[i]][cur_col+dc[i]]==1 or graph[cur_row+dr[i]][cur_col+dc[i]]=='0':
                continue
            q.append([cur_row+dr[i],cur_col+dc[i],cost+1])
            visit[cur_row+dr[i]][cur_col+dc[i]]=1
bfs()