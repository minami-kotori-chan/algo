import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

v=[[0]*(n+1) for _ in range(n+1)]

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        v[i][j]=max(v[i+1][j+1],v[i+1][j])
        if arr[0][i]>arr[1][j]:
            v[i][j]=max(v[i][j],v[i][j+1]+arr[1][j])
print(v[0][0])