import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

visited=[0]*(n+1)
arr=[]

def dfs():
    if len(arr)==m:
        print(*arr)
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        arr.append(i)
        visited[i]=1
        dfs()
        arr.pop()
        visited[i]=0
dfs()