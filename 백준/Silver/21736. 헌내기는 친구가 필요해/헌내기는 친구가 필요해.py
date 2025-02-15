from collections import deque
import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
q=deque()
visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='I':
            q.append([i,j])
            visited[i][j]=1

dr=[-1,0,1,0]
dc=[0,1,0,-1]
result=0
while q:
    cur_row,cur_col=q.popleft()
    if arr[cur_row][cur_col]=='P':
        result+=1
    for i in range(4):
        row=cur_row+dr[i]
        col=cur_col+dc[i]
        if row>=n or row<0 or col>=m or col<0:
            continue
        if visited[row][col]==0 and arr[row][col]!='X':
            q.append([row,col])
            visited[row][col]=1
if result==0:
    print("TT")
else:
    print(result)