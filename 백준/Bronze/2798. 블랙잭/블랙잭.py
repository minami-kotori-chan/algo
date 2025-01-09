import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))


top = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]<=m and arr[i]+arr[j]+arr[k]>top:
                top=arr[i]+arr[j]+arr[k]
print(top)