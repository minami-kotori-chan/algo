import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[0]*(m+1)]
v=[[0]*(m+1) for _ in range(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        v[i][j]=max(v[i-1][j],v[i][j-1])+arr[i][j]
print(v[i][j])