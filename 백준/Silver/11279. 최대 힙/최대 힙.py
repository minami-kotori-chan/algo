import sys
import heapq
n=int(sys.stdin.readline().rstrip())
heap=[]
heapq.heapify(heap)
for i in range(n):
    x=int(sys.stdin.readline().rstrip())
    if x==0:
        if len(heap)==0:
            print(0)
            continue
        print((heapq.heappop(heap))*-1)
        continue
    heapq.heappush(heap,-x)