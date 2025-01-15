from collections import deque
import sys

stack=[]
current=1
result=[]
answer=[]
enable=True

for i in range(int(sys.stdin.readline().rstrip())):
    answer.append(int(sys.stdin.readline().rstrip()))

for i in answer:
    while current<=i:
        stack.append(current)
        result.append("+")
        current+=1
    if stack[-1]==i:
        stack.pop()
        result.append("-")
    else:
        enable=False
        break
if enable:
    for i in result:
        print(i)
else:
    print("NO")