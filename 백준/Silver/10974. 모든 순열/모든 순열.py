import sys

n=int(sys.stdin.readline().rstrip())
stack=[]
v=[0]*(n+1)
def dfs():
    if len(stack)==n:
        print(*stack)
        return
    for i in range(1,n+1):
        if v[i]==1:
            continue
        v[i]=1
        stack.append(i)
        dfs()
        stack.pop()
        v[i]=0
dfs()