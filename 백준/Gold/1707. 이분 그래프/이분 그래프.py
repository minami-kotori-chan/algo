from collections import deque
import sys

k=int(sys.stdin.readline().rstrip())
for _ in range(k):
    v,e=map(int,sys.stdin.readline().rstrip().split())

    arr=[[] for _ in range(v+1)]

    for i in range(e):
        v_in,e_in=map(int,sys.stdin.readline().rstrip().split())
        arr[v_in].append(e_in)
        arr[e_in].append(v_in)

    def bfs(start):
        q=deque()
        q.append(start)
        if visited[start]==-1:
            visited[start]=0
        while q:
            cur_v=q.popleft()
            for i in arr[cur_v]:
                if visited[i]==-1:
                    visited[i]=visited[cur_v] ^ 1
                    q.append(i)
                elif visited[i]==visited[cur_v]:
                    return False
        return True
    
    visited=[-1]*(v+1)
    result=True
    for i in range(1,v+1):
        if bfs(i)==False:
            result=False
            break
    if result:
        print("YES")
    else:
        print("NO")
            