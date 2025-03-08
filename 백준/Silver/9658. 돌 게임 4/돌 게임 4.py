import sys
n=int(sys.stdin.readline().rstrip())
v=[0]*1001
v[1]=0
v[2]=1
v[3]=0
v[4]=1
for i in range(5,1001):
    v[i]=min(v[i-1],v[i-3],v[i-4])^1
if v[n]==0:
    print('CY')
else:
    print('SK')