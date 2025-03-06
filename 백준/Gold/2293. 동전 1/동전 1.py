import sys

m,n=map(int,sys.stdin.readline().rstrip().split())
arr=[]
v=[0]*(n+1)
for _ in range(m):
    arr.append(int(sys.stdin.readline().rstrip()))
v[0]=1
for i in range(m):
    for j in range(arr[i],n+1):
        v[j]+=v[j-arr[i]]
print(v[n])