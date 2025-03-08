import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*(100000+1)
v[1]=1
v[2]=1
v[3]=2
v[4]=2
v[5]=1
v[6]=2
v[7]=1
for i in range(8,n+1):
    v[i]=min(v[i-7],v[i-5],v[i-2],v[i-1])+1
print(v[n])