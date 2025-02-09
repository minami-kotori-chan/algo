import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
    graph.append(sys.stdin.readline().rstrip())
visited=[[0]*m for _ in range(n)]
max_count=[0]
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def dfs(row,col,start_row,start_col,type,count=1):
    visited[row][col]=1
    for i in range(4):
        if row+dr[i]>=n or row+dr[i]<0 or col+dc[i]>=m or col+dc[i]<0:
            continue
        if row+dr[i]==start_row and col+dc[i]==start_col:
            max_count[0]=max(max_count[0],count)
        if visited[row+dr[i]][col+dc[i]]==0 and graph[row+dr[i]][col+dc[i]]==type:
            dfs(row+dr[i],col+dc[i],start_row,start_col,type,count+1)
        if max_count[0]>=4:
            break
    visited[row][col]=0

for i in range(n):
    for j in range(m):
        dfs(i,j,i,j,graph[i][j])
        if max_count[0]>=4:
            break
if max_count[0]>=4:
    print("Yes")
else:
    print("No")