import sys
n=int(sys.stdin.readline().rstrip())
if n==0:
    print(0)
else:
    stack=[]
    count=0
    def dfs(l=0):
        global count
        if len(stack)==l:
            if stack[0]==0:
                return
            count+=1
            if count==n:
                print(*stack,sep='')
            return
        for i in range(10):
            if stack and i>=stack[-1]:
                continue
            stack.append(i)
            dfs(l)
            stack.pop()
            if count==n:
                break
    for i in range(1,11):
        dfs(i)
        if count==n:
            break
    if count!=n:
        print(-1)