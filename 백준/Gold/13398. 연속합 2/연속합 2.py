import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))

v=[[0]*2 for _ in range(n)]
if arr[0]>=0:
    v[0][0]=arr[0]
    v[0][1]=0
else:
    v[0][0]=0
    v[0][1]=0
for i in range(1,n):
    sum=0
    if v[i-1][0]+arr[i]<=0:
        if arr[i]>=0:
            v[i][0]=arr[i]
        else:
            v[i][0]=0
            v[i][1]=v[i-1][0]
    else:
        if arr[i]>=0:
            v[i][0]=v[i-1][0]+arr[i]
        else:
            v[i][0]=v[i-1][0]+arr[i]
            v[i][1]=v[i-1][0]
    
    if v[i-1][1]!=0:
        v[i][1]=max(v[i][1],v[i-1][1]+arr[i])
zero_check=True
for i in range(n):
    if v[i][0]>0:
        zero_check=False
        break
if zero_check:
    result=arr[0]
    for i in range(n):
        result=max(arr[i],result)
    print(result)

else:
    result=v[0][0]
    for i in range(n):
        for j in range(2):
            result=max(result,v[i][j])
    print(result)