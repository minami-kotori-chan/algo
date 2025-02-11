from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
q=deque()

visited=[[-1]*2001 for _ in range(2001)]
q.append([1,0])
visited[1][0]=0
is_end=False
while q:
    cur_v,clip=q.popleft()
    
    for i in range(3):
        move_v=cur_v
        move_clip=clip
        if i==0:
            move_clip=move_v
        elif i==1:
            move_v+=move_clip
        elif i==2:
            move_v-=1
        if move_v<0 or move_v>2000:
            continue
        if move_v==n:
            print(visited[cur_v][clip]+1)
            is_end=True
            break
        if visited[move_v][move_clip]==-1:
            q.append([move_v,move_clip])
            visited[move_v][move_clip]=visited[cur_v][clip]+1
    if is_end:
        break
