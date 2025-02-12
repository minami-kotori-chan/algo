from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
board=[]
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
chik=[]
house=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            chik.append([i,j])
        elif board[i][j]==1:
            house.append([i,j])

stack=[]
stack_index=[]
v=[0]*(len(chik))
result=[]
def calc_distance():
    total=0
    for i in house:
        sub_total=-1
        for j in stack:
            if sub_total==-1:
                sub_total=abs(i[0]-chik[j][0])+abs(i[1]-chik[j][1])
            else:
                sub_total=min(abs(i[0]-chik[j][0])+abs(i[1]-chik[j][1]),sub_total)
        total+=sub_total
    return total

def dfs():
    if len(stack)==m:
        if len(result)==0:
            result.append(calc_distance())
            return
        result[0]=min(result[0],calc_distance())
        return
    for i in range(len(chik)):
        if v[i]!=0 or(len(stack)>0 and stack[-1]>i):
            continue
        stack.append(i)
        v[i]=1
        dfs()
        v[i]=0
        stack.pop()
dfs()
print(result[0])