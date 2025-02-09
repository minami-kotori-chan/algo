from collections import deque
import sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    start_row,start_col=map(int,sys.stdin.readline().rstrip().split())
    end_row,end_col=map(int,sys.stdin.readline().rstrip().split())
    visited=[[0]*n for _ in range(n)]

    def bfs(row,col):
        q=deque()
        q.append([row,col,0])
        visited[row][col]=1
        dr=[-2,-1,1,2,2,1,-1,-2]
        dc=[1,2,2,1,-1,-2,-2,-1]
        while q:
            cur_row,cur_col,cost=q.popleft()
            if cur_row==end_row and cur_col==end_col:
                print(cost)
                return
            for i in range(8):
                if cur_row+dr[i]>=n or cur_row+dr[i]<0 or cur_col+dc[i]>=n or cur_col+dc[i]<0:
                    continue
                if visited[cur_row+dr[i]][cur_col+dc[i]]==0:
                    q.append([cur_row+dr[i],cur_col+dc[i],cost+1])
                    visited[cur_row+dr[i]][cur_col+dc[i]]=1
    
    bfs(start_row,start_col)