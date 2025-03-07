import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*117
v[1]=1
v[2]=1
v[3]=1
for i in range(4,117):
    v[i]=v[i-1]+v[i-3]
print(v[n])