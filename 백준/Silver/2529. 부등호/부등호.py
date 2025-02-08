import sys

n=int(sys.stdin.readline().rstrip())
str_com=list(sys.stdin.readline().rstrip().split())

def inspect():
    result=True
    for i in range(n):
        if str_com[i]=='>':
            if stack[i]>stack[i+1]:
                continue
            else:
                result=False
                break
        else:
            if stack[i]<stack[i+1]:
                continue
            else:
                result=False
                break
    
    return result

check=[0]
stack=[]
v=[0]*10

def dfs():
    if len(stack)==n+1:
        if inspect()==True:
            print(*stack,sep='')
            check[0]=1
        return
    
    for i in range(9,-1,-1):
        if v[i]==1:
            continue
        v[i]=1
        stack.append(i)
        if check[0]==1:
            return
        dfs()
        stack.pop()
        v[i]=0

def dfs2():
    if len(stack)==n+1:
        if inspect()==True:
            print(*stack,sep='')
            check[0]=1
        return
    for i in range(10):
        if v[i]==1:
            continue
        v[i]=1
        stack.append(i)
        if check[0]==1:
            return
        dfs2()
        stack.pop()
        v[i]=0
dfs()
stack=[]
v=[0]*10
check[0]=0
dfs2()