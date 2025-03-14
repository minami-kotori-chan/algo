import sys
n=int(sys.stdin.readline().rstrip())
arr=[0]
for i in range(n-1):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
k=int(sys.stdin.readline().rstrip())
v=[[0]*2 for _ in range(n+1)]
if n>=2:
    v[2][0]=arr[1][0]
    v[2][1]=float('inf')
if n>=3:
    v[3][0]=min(v[2][0]+arr[2][0],arr[1][1])
    v[3][1]=float('inf')

for i in range(4,n+1):
    v[i][0]=min(v[i-1][0]+arr[i-1][0],v[i-2][0]+arr[i-2][1])
    v[i][1]=min(v[i-1][1]+arr[i-1][0],v[i-2][1]+arr[i-2][1],v[i-3][0]+k)
print(min(v[n]))