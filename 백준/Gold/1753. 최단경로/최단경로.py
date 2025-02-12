import heapq
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
start=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(n+1)]

for i in range(m):
    u,v,w=map(int,sys.stdin.readline().rstrip().split())
    graph[u].append([v,w])

q=[]
v=[-1]*(n+1)
heapq.heappush(q,[0,start])
v[start]=0
while q:
    cost,cur_v=heapq.heappop(q)
    if v[cur_v]<cost:
        continue
    for i in graph[cur_v]:
        if v[i[0]]==-1 or v[i[0]] > v[cur_v]+i[1]:
            heapq.heappush(q,[cost+i[1],i[0]])
            v[i[0]]=cost+i[1]
    
for i in range(1,n+1):
    if v[i]==-1:
        print("INF")
    else:
        print(v[i])