import sys

sys.setrecursionlimit(3000)

while True:
    w,h=map(int,sys.stdin.readline().rstrip().split())
    if w==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    visit=[[0]*w for _ in range(h)]

    def dfs(row,col):
        if graph[row][col]==0 or visit[row][col]!=0:
            return
        dy=[-1,-1,0,1,1,1,0,-1]
        dx=[0,1,1,1,0,-1,-1,-1]
        visit[row][col]=1
        for i in range(8):
            if row+dy[i]>=h or row+dy[i]<0 or col+dx[i]>=w or col+dx[i]<0:
                continue
            dfs(row+dy[i],col+dx[i])

    result=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visit[i][j]==0:
                dfs(i,j)
                result+=1
    
    print(result)