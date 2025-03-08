import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
v=[-1]*(m+1)
v[n]=0
for i in range(n,m+1):
    if v[i-1]!=-1:
        v[i]=v[i-1]+1
    if i%2==0 and v[i//2]!=-1:
        if v[i]!=-1:
            v[i]=min(v[i],v[i//2]+1)
        else:
            v[i]=v[i//2]+1
print(v[m])