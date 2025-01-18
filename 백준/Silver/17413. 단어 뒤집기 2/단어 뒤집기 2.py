from collections import deque
import sys

in_str=sys.stdin.readline().rstrip()
q=deque()
cnt=0
result=''
for i in in_str:
    if i=='<':
        while q:
            result+=q.pop()
        cnt=1
    if i==' ' and cnt!=1:
        while q:
            result+=q.pop()
        result+=' '
        continue
    
    q.append(i)
    if i=='>':
        while q:
            result+=q.popleft()
        cnt=0
while q:
    result+=q.pop()

print(result)