from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(n)]
for i in range(m):
    s,e=map(int,sys.stdin.readline().rstrip().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

def bfs(start):
    q=deque()
    visited=[0]*n
    q.append(start)
    visited[start]=1
    while q:
        cur_v=q.popleft()
        for i in graph[cur_v]:
            if visited[i]!=0:
                continue
            q.append(i)
            visited[i]=visited[cur_v]+1
    sum=0
    for i in visited:
        sum+=i
    return sum
result=bfs(0)
index=0
for i in range(n):
    sum=bfs(i)
    if result>sum:
        result=sum
        index=i
print(index+1)