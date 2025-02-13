import sys

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(n+1)]
for i in range(m):
    v1,v2=map(int,sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited=[0]*(n+1)
result=[0]
def dfs(start):
    if visited[start]==1:
        return
    visited[start]=1
    result[0]+=1
    for i in graph[start]:
        dfs(i)
dfs(1)
print(result[0]-1)