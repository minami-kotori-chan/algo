import sys
n=int(sys.stdin.readline().rstrip())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
graph.sort(key=lambda x:(x[1],x[0]))
count=1
v=graph[0][1]
for i in range(1,n):
    if graph[i][0]>=v:
        count+=1
        v=graph[i][1]
print(count)