import sys

n,i,q=map(int,sys.stdin.readline().rstrip().split())
dic={}
def dfs(num):
    if num==0:
        return 1
    if num in dic:
        return dic[num]
    dic[num]=dfs(num//i)+dfs(num//q)
    return dic[num]
print(dfs(n))