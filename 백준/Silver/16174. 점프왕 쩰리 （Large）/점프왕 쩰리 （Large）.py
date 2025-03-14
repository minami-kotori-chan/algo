import sys
n=int(sys.stdin.readline().rstrip())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
v=[[0]*n for _ in range(n)]
v[0][0]=1

for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            continue
        if graph[i][j]==-1:
            continue
        r=i+graph[i][j]
        c=j+graph[i][j]
        if r<n and r>=0:
            v[r][j]+=v[i][j]
        if c<n and c>=0:
            v[i][c]+=v[i][j]
if v[n-1][n-1]!=0:
    print("HaruHaru")
else:
    print("Hing")