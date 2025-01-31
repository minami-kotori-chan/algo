import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

numbers=[]
v=[0]*(n+1)

def dfs():
    if len(numbers)==m:
        print(*numbers)
        return
    if len(numbers)!=0:
        for i in range(numbers[-1],n+1):
            numbers.append(i)
            dfs()
            numbers.pop()
    else:
        for i in range(1,n+1):
            numbers.append(i)
            dfs()
            numbers.pop()
dfs()