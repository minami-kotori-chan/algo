from collections import deque
import sys
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n=map(int,sys.stdin.readline().rstrip().split())
    graph=[]

    for i in range(n):
        graph.append(list(sys.stdin.readline().rstrip()))
    
    q=deque()
    visited_fire=[[0]*m for _ in range(n)]
    visited_s=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j]=='*':
                q.appendleft([i,j,1,0])
                visited_fire[i][j]=1
            elif graph[i][j]=='@':
                q.append([i,j,0,0])
                visited_s[i][j]=1
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    is_valid=True
    while q:
        cur_row,cur_col,type,cost=q.popleft()
        for i in range(4):
            row=cur_row+dr[i]
            col=cur_col+dc[i]
            if row>=n or row<0 or col>=m or col<0:
                if type==0:
                    print(cost+1)
                    is_valid=False
                    break
                continue
            if graph[row][col]=='#':
                continue
            if visited_fire[row][col]==1:
                continue
            
            if type==0:
                if visited_s[row][col]==1:
                    continue
                else:
                    q.append([row,col,type,cost+1])
                    visited_s[row][col]=1
            else:
                q.append([row,col,type,cost+1])
                visited_fire[row][col]=1
        if is_valid==False:
            break
    if is_valid:
        print("IMPOSSIBLE")