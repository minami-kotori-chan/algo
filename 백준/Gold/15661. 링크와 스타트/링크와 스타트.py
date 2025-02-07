import sys

n=int(sys.stdin.readline().rstrip())
s=[]
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().rstrip().split())))

v=[0]*n
stack_index=[]
result=[]

def calc():
    sum1=0
    sum2=0
    sum1_set=[]
    sum2_set=[]

    for i in range(n):
        if v[i]==1:
            sum1_set.append(i)
        else:
            sum2_set.append(i)

    for i in range(len(sum1_set)):
        for j in range(len(sum1_set)):
            sum1+=s[sum1_set[i]][sum1_set[j]]
    for i in range(len(sum2_set)):
        for j in range(len(sum2_set)):
            sum2+=s[sum2_set[i]][sum2_set[j]]
    
    return abs(sum1-sum2)

def dfs(c=-1):
    if len(stack_index)==c:
        if len(result)==0:
            result.append(calc())
            return
        result[0]=min(result[0],calc())
        return
    if c==-1:
        for i in range(1,n//2+1):
            for j in range(n):
                if v[j]==1 or (len(stack_index)!=0 and stack_index[-1]>j):
                    continue
                v[j]=1
                stack_index.append(j)
                dfs(i)
                stack_index.pop()
                v[j]=0
                if len(result)!=0 and result[0]==0:
                    return
    else:
        for j in range(n):
            if v[j]==1 or (len(stack_index)!=0 and stack_index[-1]>j):
                continue
            v[j]=1
            stack_index.append(j)
            dfs(c)
            stack_index.pop()
            v[j]=0
            if len(result)!=0 and result[0]==0:
                return
            
dfs()
print(result[0])