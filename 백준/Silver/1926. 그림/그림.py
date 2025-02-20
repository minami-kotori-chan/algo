import sys
sys.setrecursionlimit(250001)
n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
dr=[-1,0,1,0]
dc=[0,1,0,-1]
v=[[0]*m for _ in range(n)]
def dfs(row,col):
    count=0
    if v[row][col]==1:
        return count
    count=1
    v[row][col]=1
    for i in range(4):
        r=row+dr[i]
        c=col+dc[i]
        if r>=n or r<0 or c>=m or c<0:
            continue
        if graph[r][c]==0:
            continue
        if v[r][c]==1:
            continue
        
        count+=dfs(r,c)
    return count
result=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and v[i][j]==0:
            result.append(dfs(i,j))
if len(result)==0:
    print(0)
    print(0)
else:
    print(len(result))
    result.sort()
    print(max(result))