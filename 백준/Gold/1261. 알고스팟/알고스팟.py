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
is_end=False
if n==1 and m==1:
    print(0)
else:
    while q:
        cur_row,cur_col=q.popleft()
        cost=visited[cur_row][cur_col]
        for i in range(4):
            if cur_row+dr[i]>=n or cur_row+dr[i]<0 or cur_col+dc[i]>=m or cur_col+dc[i]<0:
                continue
            if visited[cur_row+dr[i]][cur_col+dc[i]]==-1 or visited[cur_row+dr[i]][cur_col+dc[i]]>cost+graph[cur_row+dr[i]][cur_col+dc[i]]:
                if graph[cur_row+dr[i]][cur_col+dc[i]]==0:
                    q.appendleft([cur_row+dr[i],cur_col+dc[i]])
                else:
                    q.append([cur_row+dr[i],cur_col+dc[i]])
                visited[cur_row+dr[i]][cur_col+dc[i]]=cost+graph[cur_row+dr[i]][cur_col+dc[i]]
            if cur_row+dr[i]==n-1 and cur_col+dc[i]==m-1:
                print(cost+graph[cur_row+dr[i]][cur_col+dc[i]])
                is_end=True
                break
        if is_end:
            break