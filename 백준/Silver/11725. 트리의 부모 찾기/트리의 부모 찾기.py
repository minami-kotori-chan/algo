from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(n+1)]
v=[-1]*(n+1)
for i in range(n-1):
    left,right=map(int,sys.stdin.readline().rstrip().split())
    graph[left].append(right)
    graph[right].append(left)
q=deque()
q.append(1)
v[1]=1
while q:
    cur_v=q.popleft()
    for i in graph[cur_v]:
        if v[i]==-1:
            q.append(i)
            v[i]=cur_v
for i in range(2,n+1):
    print(v[i])