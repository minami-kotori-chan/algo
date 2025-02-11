from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

q=deque()
q.append([n,1])
result=-1
while q:
    cur_v,cost=q.popleft()
    if cur_v==m:
        result=cost
        is_end=True
        break
    if cur_v>m:
        continue
    q.append([cur_v*2,cost+1])
    q.append([cur_v*10+1,cost+1])
print(result)