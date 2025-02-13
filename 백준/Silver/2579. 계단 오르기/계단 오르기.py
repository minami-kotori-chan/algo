import sys

n=int(sys.stdin.readline().rstrip())
arr=[0]
v=[0]*(n+1)
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
v[1]=arr[1]
for i in range(2,n+1):
    if i==2:
        v[2]=arr[1]+arr[2]
        continue
    v[i]=max(v[i-2]+arr[i],arr[i-1]+v[i-3]+arr[i])
print(v[n])