from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
graph=[set() for _ in range(n+1)]

for i in range(n-1):
    v1,v2=map(int,sys.stdin.readline().rstrip().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
visited=[0]*(n+1)

def bfs():
    q=[]
    q.append(0)
    graph[0].add(1)
    index=0
    for i in in_que:
        while i not in graph[q[index]]:
            index+=1
            if index==len(q):
                print(0)
                return
        q.append(i)
    print(1)

in_que = list(map(int,sys.stdin.readline().rstrip().split()))

bfs()