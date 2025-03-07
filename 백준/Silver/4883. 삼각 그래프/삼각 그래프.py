import sys
t=1
while True:
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    graph=[]
    for i in range(n):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    v=[[0]*3 for _ in range(n)]
    v[0][0]=graph[0][1]
    v[0][1]=graph[0][1]
    v[0][2]=graph[0][1]+graph[0][2]
    for i in range(1,n):
        v[i][0]=min(v[i-1][0],v[i-1][1])+graph[i][0]
        v[i][1]=min(v[i][0],v[i-1][0],v[i-1][1],v[i-1][2])+graph[i][1]
        v[i][2]=min(v[i][1],v[i-1][1],v[i-1][2])+graph[i][2]

    print(f"{t}. {v[n-1][1]}")
    t+=1