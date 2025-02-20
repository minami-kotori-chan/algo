import sys
sys.setrecursionlimit(10001)
n,m,k=map(int,sys.stdin.readline().rstrip().split())
graph=[[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().rstrip().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
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
        if graph[r][c]==1:
            continue
        if v[r][c]==1:
            continue
        
        count+=dfs(r,c)
    return count
result=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0 and v[i][j]==0:
            result.append(dfs(i,j))
print(len(result))
result.sort()
print(*result)