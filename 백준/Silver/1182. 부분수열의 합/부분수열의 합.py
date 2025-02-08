import sys

n,s=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
stack=[]
stack_index=[]
v=[0]*n
result=[0]

def calc_sum():
    sum=0
    for i in stack:
        sum+=i
    return sum

def dfs(l=0):
    if l!=0 and len(stack)==l:
        if calc_sum()==s:
            result[0]+=1
        return
    if l==0:
        for i in range(1,n+1):
            for j in range(n):
                if v[j]==1 or (len(stack_index)!=0 and stack_index[-1]>j):
                    continue
                v[j]=1
                stack.append(arr[j])
                stack_index.append(j)
                dfs(i)
                v[j]=0
                stack.pop()
                stack_index.pop()
    else:
        for j in range(n):
                if v[j]==1 or (len(stack_index)!=0 and stack_index[-1]>j):
                    continue
                v[j]=1
                stack.append(arr[j])
                stack_index.append(j)
                dfs(l)
                v[j]=0
                stack.pop()
                stack_index.pop()

dfs()
print(result[0])