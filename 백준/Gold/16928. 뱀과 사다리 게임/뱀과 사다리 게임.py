from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(101)]

for i in range(n+m):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)

q=deque()
visited=[-1]*101
q.append(1)
visited[1]=0
while q:
    cur_v=q.popleft()
    if len(graph[cur_v])!=0:
        if visited[graph[cur_v][0]]==-1 or visited[graph[cur_v][0]]>visited[cur_v]:
            q.appendleft(graph[cur_v][0])
            visited[graph[cur_v][0]]=visited[cur_v]
        continue
    for i in range(1,7):
        if cur_v+i>100:
            continue
        if visited[cur_v+i]!=-1 and visited[cur_v+i]<visited[cur_v]+1:
            continue
        q.append(cur_v+i)
        visited[cur_v+i]=visited[cur_v]+1
print(visited[100])