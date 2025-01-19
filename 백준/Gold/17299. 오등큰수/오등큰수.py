import sys

n=int(sys.stdin.readline().rstrip())
a=[]
stack=[]
stack_count={}
result=[]
for i in sys.stdin.readline().rstrip().split():
    a.append(int(i))
for i in range(n):
    result.append(-1)
for i in a:
    if i not in stack_count:
        stack_count[i]=1
    else:
        stack_count[i]+=1
for i in range(n):
    while stack and stack_count[a[stack[-1]]]<stack_count[a[i]]:
        index=stack.pop()
        result[index]=a[i]
    stack.append(i)

print(*result)