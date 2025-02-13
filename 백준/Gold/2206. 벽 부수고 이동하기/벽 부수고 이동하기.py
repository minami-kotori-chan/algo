from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
in_board=[]
for i in range(n):
    in_board.append(sys.stdin.readline().rstrip())

v=[[[-1]*2 for _ in range(m)]for _ in range(n)]
q=deque()
q.append([0,0])
v[0][0][0]=1
v[0][0][1]=1
dr=[-1,0,1,0]
dc=[0,1,0,-1]
while q:
    cur_row,cur_col=q.popleft()
    for i in range(4):
        row=cur_row+dr[i]
        col=cur_col+dc[i]
        if row>=n or row<0 or col>=m or col<0:
            continue

        if v[cur_row][cur_col][0]==-1:
            if in_board[row][col]=='1':
                continue
            if v[row][col][1]==-1 or v[row][col][1]>v[cur_row][cur_col][1]+1:
                v[row][col][1]=v[cur_row][cur_col][1]+1
                q.append([row,col])
            continue
        
        if in_board[row][col]=='1':
            if v[row][col][1]==-1 or v[row][col][1]>v[cur_row][cur_col][0]+1:
                v[row][col][1]=v[cur_row][cur_col][0]+1
                q.append([row,col])
        else:
            if v[row][col][0]==-1 or v[row][col][0]>v[cur_row][cur_col][0]+1:
                v[row][col][0]=v[cur_row][cur_col][0]+1
                q.append([row,col])

if min(v[n-1][m-1][0],v[n-1][m-1][1])==-1:
    print(max(v[n-1][m-1][0],v[n-1][m-1][1]))
else:
    print(min(v[n-1][m-1][0],v[n-1][m-1][1]))