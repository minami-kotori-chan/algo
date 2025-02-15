import sys

n=int(sys.stdin.readline().rstrip())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

def dfs(start):
    for i in range(n):
        if graph[start][i]==0 or v[i]!=0:
            continue
        v[i]=1
        dfs(i)

for i in range(n):
    v=[0]*n
    dfs(i)
    print(*v)