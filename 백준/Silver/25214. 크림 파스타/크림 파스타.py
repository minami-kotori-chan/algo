import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
v=[0]*n
v[0]=arr[0]
result=0
print(0,end=' ')
for i in range(1,n):
    v[i]=min(arr[i],v[i-1])
    result=max(result,arr[i]-v[i])
    print(result,end=' ')