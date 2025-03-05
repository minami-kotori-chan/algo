import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*(n+1)

for i in range(1,n+1):
    if i==1:
        v[1]=1
        continue
    v[i]=v[i-1]+v[i-2]
print(v[n])