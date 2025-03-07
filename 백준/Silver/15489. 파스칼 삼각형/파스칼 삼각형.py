import sys

r,c,w=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(r+w)]
graph[0].append(1)
for i in range(1,r+w):
    for j in range(i+1):
        graph[i].append(1)
for i in range(2,r+w):
    for j in range(1,i):
        graph[i][j]=graph[i-1][j-1]+graph[i-1][j]
result=0
for i in range(w):
    for j in range(i+1):
        result+=graph[i+r-1][j+c-1]
print(result)