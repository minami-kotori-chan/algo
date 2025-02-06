import sys

n=int(sys.stdin.readline().rstrip())
w=[]
v=[0]*n
stack=[]
result=[-1]

for _ in range(n):
    w.append(list(map(int,sys.stdin.readline().rstrip().split())))

def calc_value():
    sum=0
    for i in range(-1,len(stack)-1):
        if w[stack[i]][stack[i+1]]!=0:
            sum+=w[stack[i]][stack[i+1]]
        else:
            return result[0]
    return sum

def dfs():
    if len(stack)==n:
        if result[0]==-1:
            result[0]=calc_value()
        else:
            result[0]=min(result[0],calc_value())
        return
    for i in range(n):
        if v[i]==1:
            continue
        v[i]=1
        stack.append(i)
        dfs()
        stack.pop()
        v[i]=0
dfs()
print(result[0])