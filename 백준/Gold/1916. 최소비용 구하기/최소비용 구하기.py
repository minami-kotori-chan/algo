import heapq
import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
v=[-1]*(n+1)
for i in range(m):
    s1,s2,in_cost=map(int,sys.stdin.readline().split())
    graph[s1].append([s2,in_cost])
start,end=map(int,sys.stdin.readline().split())

q=[]
heapq.heappush(q,[0,start])
while q:
    cost,cur_v=heapq.heappop(q)
    if v[cur_v]!=-1:
        continue
    if cur_v==end:
        print(cost)
        break
    v[cur_v]=cost
    for i in graph[cur_v]:
        heapq.heappush(q,[cost+i[1],i[0]])