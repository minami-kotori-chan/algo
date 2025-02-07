import sys

while True:
    k=-1
    arr=[]
    for i in list(map(int,sys.stdin.readline().rstrip().split())):
        if k==-1:
            k=i
        else:
            arr.append(i)
    if k==0:
        break
    
    stack=[]
    stack_index=[]
    v=[0]*k

    def dfs():
        if len(stack)==6:
            print(*stack)
            return
        for i in range(k):
            if v[i]==1 or (len(stack)!=0 and i<stack_index[-1]):
                continue
            v[i]=1
            stack.append(arr[i])
            stack_index.append(i)
            dfs()
            stack.pop()
            stack_index.pop()
            v[i]=0
    dfs()
    print()