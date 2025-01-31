import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

numbers=[]

def dfs():
    if len(numbers)==m:
        print(*numbers)
        return
    for i in range(1,n+1):
        numbers.append(i)
        dfs()
        numbers.pop()
    
dfs()