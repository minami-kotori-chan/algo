import sys

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())

v=[0]*(n+1)
arr=[0]*(n+1)

for _ in range(m):
	arr[int(sys.stdin.readline().rstrip())]=1
v[0]=1
v[1]=1
for i in range(2,n+1):
	if arr[i]==1 or arr[i-1]==1:
		v[i]=v[i-1]
		continue
	if v[i-1]==v[i-2]:
		v[i]=v[i-1]*2
		continue
	v[i]=v[i-1]+v[i-2]

print(v[n])