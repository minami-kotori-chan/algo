import sys
from collections import deque

n=int(sys.stdin.readline().rstrip())

q=deque()
dic={}
q.append([n,0])
dic[n]=0

while q:
    value,cost=q.popleft()
    if value==1:
        print(cost)
        break
    if value%3==0:
        if value//3 not in dic:
            q.append([value//3,cost+1])
            dic[value//3]=value
    if value%2==0:
        if value//2 not in dic:
            q.append([value//2,cost+1])
            dic[value//2]=value
    if value-1 not in dic:
        q.append([value-1,cost+1])
        dic[value-1]=value
    
stack=[1]
index=1
while True:
    index=dic[index]
    if index==0:
        break
    stack.append(index)

print(*stack[::-1])