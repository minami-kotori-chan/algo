import sys

sys.setrecursionlimit(2500)

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for _ in range(n)]
for i in range(m):
    s,e=map(int,sys.stdin.readline().rstrip().split())
    arr[s].append(e)
    arr[e].append(s)


max_deep=[0]
def dfs(node,deep=1):
    if v[node]==1:
        return
    max_deep[0]=max(max_deep[0],deep)
    v[node]=1
    if max_deep[0]>=5:
        return
    for i in arr[node]:
        if v[i]==0:
            dfs(i,deep+1)
            if deep>=5:
                break
            v[i]=0

for i in range(n):
    v=[0]*n
    dfs(i)
    if max_deep[0]>=5:
        break
if max_deep[0]>=5:
    print(1)
else:
    print(0)