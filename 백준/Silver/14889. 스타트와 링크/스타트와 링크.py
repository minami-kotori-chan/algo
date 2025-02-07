import sys

n=int(sys.stdin.readline().rstrip())
s=[]
team=n//2
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().rstrip().split())))
stack=[]
v=[0]*n
result=[]
stack_index=[]

def calc():
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(n):
            if v[i]==v[j]:
                if v[i]==1:
                    sum1+=s[i][j]
                else:
                    sum2+=s[i][j]
    return abs(sum1-sum2)

def dfs():
    if len(stack)==team:
        if len(result)==0:
            result.append(calc())
            return
        result[0]=min(result[0],calc())
        return
    for i in range(n):
        if v[i]==1 or (len(stack)!=0 and stack_index[-1]>i):
            continue
        v[i]=1
        stack.append(i)
        stack_index.append(i)
        dfs()
        stack.pop()
        stack_index.pop()
        v[i]=0
dfs()
print(result[0])