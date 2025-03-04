import sys
n=int(sys.stdin.readline().rstrip())
graph=[]
for _ in range(n):
	graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
v=[[0]*n for _ in range(n)]
v[0][0]=1
for i in range(n):
	for j in range(n):
		if v[i][j]==0 or graph[i][j]==0:
			continue
		if graph[i][j]+i<n:
			v[graph[i][j]+i][j]+=v[i][j]
		if graph[i][j]+j<n:
			v[i][graph[i][j]+j]+=v[i][j]
print(v[n-1][n-1])