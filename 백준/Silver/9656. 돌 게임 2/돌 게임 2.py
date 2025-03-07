import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*1001

v[1]=1
v[2]=0
v[3]=1
for i in range(4,1001):
    v[i]=v[i-1]^1
if v[n]==0:
    print('SK')
else:
    print('CY')