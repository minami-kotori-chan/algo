from collections import deque
import sys

n,m,start=map(int,sys.stdin.readline().rstrip().split())
arr=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    n_num,v_num = map(int,sys.stdin.readline().rstrip().split())
    arr[n_num][v_num]=1

def dfs(num):
    v[num]=1
    print(num,end=' ')
    for i in range(1,n+1):
        if arr[num][i]==1 or arr[i][num]==1:
            if v[i]==0:
                dfs(i)

def bfs(start_node):
    q.append(start_node)
    v[start_node]=1
    while q:
        cur = q.popleft()
        print(cur,end=' ')
        for i in range(1,n+1):
            if arr[cur][i]==1 or arr[i][cur]==1:
                if v[i]==0:
                    q.append(i)
                    v[i]=1

v=[0]*(n+1)
dfs(start)
print()
v=[0]*(n+1)
q=deque()
bfs(start)