from collections import deque
import sys

q1=deque()

for i in sys.stdin.readline().rstrip():
    q1.append(i)
q2=deque()

for i in range(int(sys.stdin.readline().rstrip())):
    word = sys.stdin.readline().rstrip().split()

    if word[0]=="L":
        if q1:
            q2.appendleft((q1.pop()))
    elif word[0]=="D":
        if q2:
            q1.append((q2.popleft()))
    elif word[0]=="B":
        if q1:
            q1.pop()
    elif word[0]=="P":
        q1.append(word[1])
print(''.join(q1)+''.join(q2))