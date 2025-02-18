import sys

n=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().rstrip().split()))
opcode=list(map(int,sys.stdin.readline().rstrip().split()))
result_max=[]
result_min=[]
stack=[]

def calc():
    result=numbers[0]
    for i,v in enumerate(stack):
        if v==0:
            result+=numbers[i+1]
        elif v==1:
            result-=numbers[i+1]
        elif v==2:
            result*=numbers[i+1]
        else:
            result/=numbers[i+1]
        result=int(result)
    if len(result_max)==0:
        result_max.append(result)
    if len(result_min)==0:
        result_min.append(result)
    result_max[0]=max(result_max[0],result)
    result_min[0]=min(result_min[0],result)


def dfs():
    k=-1
    if len(stack)==n-1:
        calc()
        return
    for i in range(4):
        if opcode[i]==0:
            continue
        if i==k:
            continue
        stack.append(i)
        opcode[i]-=1
        k=i
        dfs()
        opcode[i]+=1
        stack.pop()
dfs()
print(result_max[0])
print(result_min[0])