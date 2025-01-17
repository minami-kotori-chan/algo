from collections import deque
import sys

q=deque()

for i in range(int(sys.stdin.readline().rstrip())):
    word = sys.stdin.readline().rstrip().split()

    if word[0]=="push_front":
        q.appendleft(word[1])
    elif word[0]=="push_back":
        q.append(word[1])
    elif word[0]=="pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif word[0]=="pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif word[0]=="size":
        print(len(q))
    elif word[0]=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif word[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif word[0]=="back":
        if q:
            print(q[-1])
        else:
            print(-1)