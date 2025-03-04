import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(n):
	arr.append(int(sys.stdin.readline().rstrip()))	

v=[[0]*(m+1) for _ in range(n)]
v[0][0]=arr[0]%2
v[0][1]=arr[0]//2

for i in range(1,n):
	for j in range(m+1):
		if j%2==1:
			k=arr[i]//2
		else:
			k=arr[i]%2
		if j==0:
			v[i][j]=arr[i]%2+v[i-1][j]
			continue
		v[i][j]=max(v[i-1][j],v[i-1][j-1])+k
print(max(v[n-1]))