import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

a=list(map(int,sys.stdin.readline().rstrip().split()))
a.sort()
r=[]
v=[0]*n

def dfs():
    if len(r)==m:
        print(*r)
        return
    if True:
        for i in range(n):
            v[i]=1
            r.append(a[i])
            dfs()
            r.pop()
            v[i]=0

dfs()