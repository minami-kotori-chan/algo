import sys

n=int(sys.stdin.readline().rstrip())

v=[[0]*4 for _ in range(n+1)]
v[1][0]=3
v[1][1]=1
v[1][2]=1
v[1][3]=1

for i in range(2,n+1):
    v[i][1]=v[i-1][0]
    v[i][2]=v[i-1][0]-v[i-1][2]
    v[i][3]=v[i-1][0]-v[i-1][3]
    v[i][0]=(v[i][1]+v[i][2]+v[i][3])%9901

print(v[n][0])