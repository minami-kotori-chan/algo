import sys

n,p,q,x,y=map(int,sys.stdin.readline().rstrip().split())
dic={}
dic[0]=1

def dfs(num):
    if num<=0:
        return 1
    if num in dic:
        return dic[num]
    dic[num]=dfs(num//p-x)+dfs(num//q-y)
    return dic[num]
print(dfs(n))