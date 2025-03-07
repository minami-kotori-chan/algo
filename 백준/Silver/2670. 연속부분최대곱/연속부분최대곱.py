import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    arr.append(float(sys.stdin.readline().rstrip()))
v=[0]*n
v[0]=arr[0]
for i in range(1,n):
    v[i]=max(arr[i],v[i-1]*arr[i])
print(f"{max(v):.3f}")