import sys

n=int(sys.stdin.readline().rstrip())
t=[]
p=[]
for _ in range(n):
    ti,pi=map(int,sys.stdin.readline().rstrip().split())
    t.append(ti)
    p.append(pi)

stack_index=[]
stack_value=[]
result=[0]

def dfs(d=0):
    if d>n:
        sum=0
        for i in stack_value:
            sum+=i
        sum-=stack_value[-1]
        result[0]=max(result[0],sum)
        return
    if d==n:
        sum=0
        for i in stack_value:
            sum+=i
        result[0]=max(result[0],sum)
        return
    for i in range(d,n):
        stack_index.append(i)
        stack_value.append(p[i])
        dfs(i+t[i])
        stack_index.pop()
        stack_value.pop()
dfs()
print(result[0])