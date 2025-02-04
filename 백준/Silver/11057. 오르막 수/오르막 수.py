import sys

n=int(sys.stdin.readline().rstrip())

v=[[0]*10 for _ in range(n+1)]

for i in range(10):
    v[1][i]=1
for i in range(1,n+1):
    for j in range(10):
        for k in range(j,10):
            v[i][j]+=(v[i-1][k])%10007
        v[i][j]%=10007
result=0
for i in range(10):
    result+=v[n][i]
result%=10007
print(result)