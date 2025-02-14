import sys
import heapq
t=int(sys.stdin.readline().rstrip())
q=[]
heapq.heapify(q)
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        if len(q)>=1:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,n)