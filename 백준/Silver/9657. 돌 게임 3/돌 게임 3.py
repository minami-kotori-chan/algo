import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*1001
v[1]=1
v[2]=0
v[3]=1
v[4]=1
for i in range(5,1001):
    v[i]=min(v[i-1],v[i-3],v[i-4])^1
if v[n]==1:
    print('SK')
else:
    print('CY')