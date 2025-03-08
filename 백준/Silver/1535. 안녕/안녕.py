import sys

n=int(sys.stdin.readline().rstrip())
hp=[0]
value=[0]
for i in map(int,sys.stdin.readline().rstrip().split()):
    hp.append(i)
for i in map(int,sys.stdin.readline().rstrip().split()):
    value.append(i)
heal=99
v=[[0]*(heal+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,heal+1):
        if hp[i]>j:
            v[i][j]=v[i-1][j]
            continue
        v[i][j]=max(v[i-1][j],v[i-1][j-hp[i]]+value[i])
print(v[n][heal])