import sys
sys.setrecursionlimit(3000)
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n,k=map(int,sys.stdin.readline().rstrip().split())
    board=[[0]*m for _ in range(n)]
    for i in range(k):
        x,y=map(int,sys.stdin.readline().rstrip().split())
        board[y][x]=1
    visited=[[0]*m for _ in range(n)]

    def dfs(row,col):
        if visited[row][col]==1:
            return 0
        if board[row][col]==0:
            return 0
        visited[row][col]=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            if row+dr[i]>=n or row+dr[i]<0 or col+dc[i]>=m or col+dc[i]<0:
                continue
            dfs(row+dr[i],col+dc[i])
        return 1
    result=0

    for i in range(n):
        for j in range(m):
            result+=dfs(i,j)
    print(result)