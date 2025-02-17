import sys
sys.setrecursionlimit(10001)
n=int(sys.stdin.readline().rstrip())
graph1=[]
graph2=[[] for _ in range(n)]
for i in range(n):
    graph1.append(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(n):
        if graph1[i][j]=='G':
            graph2[i].append('R')
            continue
        graph2[i].append(graph1[i][j])

dr=[-1,0,1,0]
dc=[0,1,0,-1]
def dfs(r,c,type):
    if v[r][c]!=0:
        return 0
    v[r][c]=1
    for i in range(4):
        row=r+dr[i]
        col=c+dc[i]
        if row>=n or row<0 or col>=n or col<0:
            continue
        if v[row][col]!=0:
            continue
        if type==0:
            graph=graph1
        else:
            graph=graph2
        if graph[row][col]!=graph[r][c]:
            continue
        dfs(row,col,type)
    return 1
count=0
v=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        count+=dfs(i,j,0)
print(count,end=' ')
count=0
v=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        count+=dfs(i,j,1)
print(count)