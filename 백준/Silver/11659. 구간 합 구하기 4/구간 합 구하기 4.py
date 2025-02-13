import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
v=[0]*n
sum=0
for i in range(n):
    sum+=arr[i]
    v[i]=sum
for i in range(m):
    start,end=map(int,sys.stdin.readline().rstrip().split())
    if start==1:
        print(v[end-1])
        continue
    print(v[end-1]-v[start-2])