from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for i in range(n):
    graph.append(sys.stdin.readline().rstrip())
v=[[0]*m for _ in range(n)]
v_j=[[0]*m for _ in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]=='J':
            q.append([i,j,0,0])
            v_j[i][j]=1
        if graph[i][j]=='F':
            q.appendleft([i,j,1,0])
            v[i][j]=1
dr=[-1,0,1,0]
dc=[0,1,0,-1]
escape=False
while q:
    r,c,type,cost=q.popleft()
    for i in range(4):
        row=r+dr[i]
        col=c+dc[i]
        if row>=n or row<0 or col>=m or col<0:
            if type==0:
                print(cost+1)
                escape=True
                break
            else:
                continue
        if graph[row][col]=='#':
            continue
        if v[row][col]==1:
            continue
        if type==0:
            if v_j[row][col]==1:
                continue
            q.append([row,col,0,cost+1])
            v_j[row][col]=1
        else:
            q.append([row,col,1,cost+1])
            v[row][col]=1
    if escape==True:
        break
if escape==False:
    print("IMPOSSIBLE")