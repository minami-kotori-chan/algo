import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))

def calc_sum():
    sum=0
    for i in range(n-1):
        sum+=abs(stack[i]-stack[i+1])
    return sum

stack=[]
result=[0]
v=[0]*n
def dfs():
    if len(stack)==n:
        result[0]=max(calc_sum(),result[0])
        return
    for i in range(n):
        if v[i]==1:
            continue
        v[i]=1
        stack.append(arr[i])
        dfs()
        stack.pop()
        v[i]=0
dfs()
print(result[0])