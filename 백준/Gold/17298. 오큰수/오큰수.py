import sys

n=int(sys.stdin.readline().rstrip())
a=[]
stack=[]
result=[]
for i in sys.stdin.readline().rstrip().split():
    a.append(int(i))
for i in range(n):
    result.append(-1)
for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        index = stack.pop()
        result[index]=a[i]
    stack.append(i)

print(*result)