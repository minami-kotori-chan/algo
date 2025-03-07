import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*81
v[1]=1
v[2]=1
v[3]=2
for i in range(4,81):
    v[i]=v[i-1]+v[i-2]
print((v[n]+v[n-1]+v[n])*2)