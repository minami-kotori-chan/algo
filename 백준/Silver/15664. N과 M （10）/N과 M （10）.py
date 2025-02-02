import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

numbers=list(map(int,sys.stdin.readline().rstrip().split()))
numbers.sort()
stack=[]
v=[0]*(n+1)

def dfs(index=0):
    check=0
    if len(stack)==m:
        print(*stack)
        return
    for i in range(index,n):
        if v[i]==1 or check==numbers[i]:
            continue
        v[i]=1
        stack.append(numbers[i])
        check=numbers[i]
        dfs(i)
        stack.pop()
        v[i]=0
dfs()