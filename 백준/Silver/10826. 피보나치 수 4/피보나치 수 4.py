import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*(n+1)
if n>=1:
    v[1]=1
for i in range(2,n+1):
    v[i]=v[i-1]+v[i-2]
print(v[n])