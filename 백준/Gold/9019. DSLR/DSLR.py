from collections import deque
import sys
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    q=deque()
    q.append([a,''])
    v=set()

    while q:
        cur_num,op=q.popleft()
        if cur_num==b:
            print(op)
            break
        if (cur_num*2)%10000 not in v:
            v.add((cur_num*2)%10000)
            q.append([(cur_num*2)%10000,op+'D'])
        num=cur_num
        if num==0:
            num=9999
        else:
            num-=1
        if num not in v:
            v.add(num)
            q.append([num,op+'S'])

        l=(cur_num%1000)*10+cur_num//1000
        r=(cur_num%10)*1000+cur_num//10
        
        if l not in v:
            v.add(l)
            q.append([l,op+'L'])
        if r not in v:
            v.add(r)
            q.append([r,op+'R'])