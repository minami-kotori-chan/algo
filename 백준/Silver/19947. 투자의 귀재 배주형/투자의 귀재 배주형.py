import sys

h,y=map(int,sys.stdin.readline().rstrip().split())
v=[0]*(y+1)
v[0]=h
for i in range(1,y+1):
    v[i]=v[i-1]+v[i-1]//20
    if i>=3:
        v[i]=max(v[i],v[i-3]+v[i-3]//5)
    if i>=5:
        v[i]=max(v[i],v[i-5]+(v[i-5]*35)//100)
print(v[y])