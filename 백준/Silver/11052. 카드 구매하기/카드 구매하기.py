import sys

n=int(sys.stdin.readline().rstrip())
p=[]
p.append(0)
value=[0]*(n+1)

for i in map(int,sys.stdin.readline().rstrip().split()):
    p.append(i)


def dp(n):
    if value[n]!=0:
        return value[n]
    if n==1:
        value[n]=p[n]
    for i in range(1,int(n/2)+1):
        value[n]=max(dp(i)+dp(n-i),value[n])
    value[n] = max(value[n],p[n])
    return value[n]

print(dp(n))