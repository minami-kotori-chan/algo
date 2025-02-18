from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
r1,c1,r2,c2=map(int,sys.stdin.readline().rstrip().split())

q=deque()
v=[[-1]*n for _ in range(n)]
q.append([r1,c1])
v[r1][c1]=0
dr=[-2,-2,0,0,2,2]
dc=[-1,1,-2,2,-1,1]
while q:
    cur_row,cur_col=q.popleft()
    for i in range(6):
        row=cur_row+dr[i]
        col=cur_col+dc[i]
        if row>=n or row<0 or col>=n or col<0:
            continue
        if v[row][col]!=-1:
            continue
        q.append([row,col])
        v[row][col]=v[cur_row][cur_col]+1
print(v[r2][c2])