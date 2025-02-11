from collections import deque
import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
q=deque()
visited=[-1]*100001
q.append(n)
visited[n]=0
while q:
    cur_v=q.popleft()
    
    if cur_v+1<=100000 and (visited[cur_v+1]==-1 or visited[cur_v+1]>visited[cur_v]+1):
        q.append(cur_v+1)
        visited[cur_v+1]=visited[cur_v]+1
    if cur_v-1>=0 and (visited[cur_v-1]==-1 or visited[cur_v-1]>visited[cur_v]+1):
        q.append(cur_v-1)
        visited[cur_v-1]=visited[cur_v]+1
    if cur_v*2<=100000 and (visited[cur_v*2]==-1 or visited[cur_v*2]>visited[cur_v]):
        q.append(cur_v*2)
        visited[cur_v*2]=visited[cur_v]
print(visited[k])