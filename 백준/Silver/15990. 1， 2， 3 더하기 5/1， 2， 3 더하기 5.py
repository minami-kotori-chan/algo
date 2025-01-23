import sys

t=int(sys.stdin.readline().rstrip())

n=100000
v = [[0] * 4 for _ in range(n+1)]
v[1][1]=1
v[2][2]=1
v[3][1]=1
v[3][2]=1
v[3][3]=1

for i in range(1,n+1):
    for j in range(1,3+1):
        if i>3:
            v[i][j]+=((v[i-j][1]+v[i-j][2]+v[i-j][3]-v[i-j][j])%1000000009)
    v[i][0]=(v[i][1]+v[i][2]+v[i][3])%1000000009

for _ in range(t):
    in_n=int(sys.stdin.readline().rstrip())
    print(v[in_n][0])