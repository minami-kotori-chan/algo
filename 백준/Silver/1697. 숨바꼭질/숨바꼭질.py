from collections import deque
import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
visited=[0]*100001

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
                return cost+1
            if visited[move_v]==0:
                q.append([move_v,cost+1])
                visited[move_v]=1
print(bfs())