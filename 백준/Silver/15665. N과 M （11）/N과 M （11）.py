import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

numbers=list(map(int,sys.stdin.readline().rstrip().split()))
numbers.sort()
stack=[]
v=[0]*(n+1)

def dfs():
    check=0
    if len(stack)==m:
        print(*stack)
        return
    for i in range(n):
        if check==numbers[i]:
            continue
        v[i]=1
        stack.append(numbers[i])
        check=numbers[i]
        dfs()
        stack.pop()
        v[i]=0
dfs()