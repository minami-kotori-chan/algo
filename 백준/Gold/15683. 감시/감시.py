from itertools import combinations
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
c_num=0
ct=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]>0 and graph[i][j]<6:
            c_num+=1
            ct.append([i,j])
stack=[]
result=n*m

def straight(type,row,col,v):
    if type==0:
        t=row
        while t>0:
            t-=1
            if graph[t][col]==6:
                break
            v[t][col]=1
    elif type==1:
        t=col
        while t<m-1:
            t+=1
            if graph[row][t]==6:
                break
            v[row][t]=1
    elif type==2:
        t=row
        while t<n-1:
            t+=1
            if graph[t][col]==6:
                break
            v[t][col]=1
    else:
        t=col
        while t>0:
            t-=1
            if graph[row][t]==6:
                break
            v[row][t]=1


def calc():
    global result
    v=[[0]*m for _ in range(n)]
    for i in range(len(stack)):
        row=ct[i][0]
        col=ct[i][1]
        cv=graph[row][col]

        if cv==1:
            straight(stack[i],row,col,v)
        
        elif cv==2:
            if stack[i]%2==0:
                straight(0,row,col,v)
                straight(2,row,col,v)
            else:
                straight(1,row,col,v)
                straight(3,row,col,v)
        elif cv==3:
            if stack[i]==0:
                straight(0,row,col,v)
                straight(1,row,col,v)
            elif stack[i]==1:
                straight(1,row,col,v)
                straight(2,row,col,v)
            elif stack[i]==2:
                straight(2,row,col,v)
                straight(3,row,col,v)
            else:
                straight(3,row,col,v)
                straight(0,row,col,v)

        elif cv==4:
            if stack[i]==0:
                straight(0,row,col,v)
                straight(1,row,col,v)
                straight(2,row,col,v)
            elif stack[i]==1:
                straight(1,row,col,v)
                straight(2,row,col,v)
                straight(3,row,col,v)
            elif stack[i]==2:
                straight(2,row,col,v)
                straight(3,row,col,v)
                straight(0,row,col,v)
            else:
                straight(3,row,col,v)
                straight(0,row,col,v)
                straight(1,row,col,v)
        
        else:
            straight(0,row,col,v)
            straight(1,row,col,v)
            straight(2,row,col,v)
            straight(3,row,col,v)
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0 and v[i][j]==0:
                count+=1
    result=min(result,count)
            

def dfs():
    if len(stack)==c_num:
        calc()
        return
    for i in range(4):
        stack.append(i)
        dfs()
        stack.pop()
dfs()
print(result)