from collections import deque
import sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    opcode=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline().rstrip())
    q=deque()
    count=0
    prev_str=''
    for i in sys.stdin.readline().rstrip():
        if i=='[':
            continue
        if (i==',' or i==']') and prev_str!='':
            q.append(prev_str)
            prev_str=''
            continue
        prev_str=prev_str+i
    for i in opcode:
        if i=='R':
            count=count^1
        else:
            if len(q)==0:
                count=-1
                break
            if count==0:
                q.popleft()
            else:
                q.pop()
    if count==-1:
        print('error')
        continue
    print('[',end='')
    if count==0:
        for i in range(len(q)):
            print(q[i],end='')
            if i!=len(q)-1:
                print(',',end='')
    else:
        for i in range(len(q)-1,-1,-1):
            print(q[i],end='')
            if i!=0:
                print(',',end='')
    print(']')