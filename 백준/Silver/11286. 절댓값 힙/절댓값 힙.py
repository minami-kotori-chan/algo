import sys
import heapq

n=int(sys.stdin.readline().rstrip())
q=[]
heapq.heapify(q)
for i in range(n):
    x=int(sys.stdin.readline().rstrip())

    if x==0:
        if len(q)==0:
            print(0)
            continue
        num=heapq.heappop(q)
        print(num[1])
    else:
        ab_x=x
        if x<0:
            ab_x=-x
        heapq.heappush(q,(ab_x,x))