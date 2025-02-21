import sys
n=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().rstrip().split()))
stack=[]
result=[0]*n
for i in range(n-1,-1,-1):
    while stack and numbers[i]>stack[-1][0]:
        value,index=stack.pop()
        result[index]=i+1

    stack.append([numbers[i],i])
print(*result)