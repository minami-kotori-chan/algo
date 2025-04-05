from collections import deque
import sys

graph=[]
for i in range(5):
    graph.append(sys.stdin.readline().rstrip())
stack=[]
v=[0]*25
dr=[-1,0,1,0]
dc=[0,1,0,-1]
output=[0]
def bfs():
    q=deque()
    q.append(stack[0])
    visited=[0]*25
    result=1
    while q:
        cur = q.popleft()
        row=cur//5
        col=cur%5
        visited[row*5+col]=1
        for i in range(4):
            r=row+dr[i]
            c=col+dc[i]
            if r<0 or r>=5 or c<0 or c>=5:
                continue
            if v[r*5+c]==0 or visited[r*5+c]==1:
                continue
            q.append(r*5+c)
            visited[r*5+c]=1
            result+=1
    if result==7:
        return True
    else:
        return False

def dfs(n=0):
    if n>=4:
        return
    if len(stack)==7:
        if bfs():
            output[0]+=1
        return
    for i in range(25):
        if v[i]==1:
            continue
        if stack and stack[-1]<i:
            continue
        stack.append(i)
        v[i]=1
        value=n
        if graph[i//5][i%5]=='Y':
            value+=1
        dfs(value)
        stack.pop()
        v[i]=0
dfs()
print(output[0])