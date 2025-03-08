import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
v=[1]*n

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            v[i]=max(v[i],v[j]+1)
print(max(v))