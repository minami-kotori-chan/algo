from collections import deque
import sys

sys.setrecursionlimit(5000)

n=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(n)]
for _ in range(n):
    v1,v2=map(int,sys.stdin.readline().rstrip().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

check_circle=[0]*n

def dfs(start,p):
    if visited[start]==1:
        check_circle[start]=1
        return
    visited[start]=1
    for i in graph[start]:
        if i!=p:
            dfs(i,start)

def bfs(start):
    q=deque()
    visited=[0]*n
    q.append([start,0])
    visited[start]=1
    while q:
        cur_v,deep=q.popleft()
        if check_circle[cur_v]==1:
            print(deep,end=' ')
            return
        for i in graph[cur_v]:
            if visited[i]==0:
                q.append([i,deep+1])
                visited[i]=1

for i in range(n):
    visited=[0]*n
    dfs(i,i)

for i in range(n):
    bfs(i)