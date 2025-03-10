import sys

n,d=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(d+1)]
v=[0]*(d+1)
for i in range(n):
    start,end,cost=map(int,sys.stdin.readline().rstrip().split())
    if end>d:
        continue
    graph[end].append([start,cost])
for i in range(1,d+1):
    v[i]=v[i-1]+1
    for j in graph[i]:
        v[i]=min(v[i],v[j[0]]+j[1])
print(v[d])