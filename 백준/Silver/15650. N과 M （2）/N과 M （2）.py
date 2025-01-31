import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

numbers=[]
v=[0]*(n+1)

def dfs():
    if len(numbers)==m:
        print(*numbers)
        return
    if len(numbers)>0:
        for i in range(numbers[-1],n+1):
            if v[i]==1:
                continue
            numbers.append(i)
            v[i]=1
            dfs()
            numbers.pop()
            v[i]=0
    else:
        for i in range(1,n+1):
            if v[i]==1:
                continue
            numbers.append(i)
            v[i]=1
            dfs()
            numbers.pop()
            v[i]=0

dfs()
