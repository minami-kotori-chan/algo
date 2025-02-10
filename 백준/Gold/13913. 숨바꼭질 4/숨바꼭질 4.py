from collections import deque
import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
visited=[-1]*100001

def move(x,num):
    if num==0:
        return x-1
    elif num==1:
        return x+1
    else:
        return x*2

def bfs():
    q=deque()
    q.append([n,0])
    visited[n]=1
    if n==k:
        return 0
    while q:
        cur_v,cost=q.popleft()
        for i in range(3):
            move_v=move(cur_v,i)
            if move_v<0 or move_v>100000:
                continue
            if move_v==k:
                visited[move_v]=cur_v
                return cost+1
            if visited[move_v]==-1:
                q.append([move_v,cost+1])
                visited[move_v]=cur_v
print(bfs())
stack=[]
stack.append(k)
if k!=n:
    prev_v=visited[k]
    stack.append(prev_v)
    while prev_v!=n:
        prev_v=visited[prev_v]
        stack.append(prev_v)
print(*stack[::-1])