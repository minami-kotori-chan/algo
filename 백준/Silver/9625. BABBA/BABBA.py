import sys

n=int(sys.stdin.readline().rstrip())
v=[[0]*2 for _ in range(n+1)]
v[0][0]=1
for i in range(1,n+1):
    v[i][0]=v[i-1][1]
    v[i][1]=v[i-1][0]+v[i-1][1]
print(*v[n])