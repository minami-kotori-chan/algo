import sys

t=int(sys.stdin.readline().rstrip())
v=[[0]*10 for _ in range(65)]
result=[0]*65
for i in range(10):
    v[1][i]=1
result[1]=10
for i in range(2,65):
    for j in range(10):
        for k in range(j,10):
            v[i][j]+=v[i-1][k]
        result[i]+=v[i][j]

for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    print(result[n])