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
    if len(r)==0:
        for i in range(n):
            if v[i]==1:
                continue
            v[i]=1
            r.append(a[i])
            dfs()
            r.pop()
            v[i]=0
    else:
        l=a.index(r[-1])
        for i in range(l,n):
            if v[i]==1:
                continue
            v[i]=1
            r.append(a[i])
            dfs()
            r.pop()
            v[i]=0

dfs()