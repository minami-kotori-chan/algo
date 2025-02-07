import sys

l,c=map(int,sys.stdin.readline().rstrip().split())
string=[]

for i in sys.stdin.readline().rstrip().split():
    string.append(i)

string.sort()
stack=[]
stack_index=[]
v=[0]*c

def dfs(n=0):
    if len(stack)==l:
        if n==0 or n>l-2:
            return
        print(*stack,sep='')
        return
    for i in range(c):
        if v[i]==1 or (len(stack_index)!=0 and stack_index[-1]>i):
            continue
        v[i]=1
        stack.append(string[i])
        stack_index.append(i)
        if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
            dfs(n+1)
        else:
            dfs(n)
        stack.pop()
        stack_index.pop()
        v[i]=0
dfs()