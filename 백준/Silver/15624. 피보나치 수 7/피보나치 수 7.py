import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*1000001
v[0]=0
v[1]=1
for i in range(2,n+1):
    v[i]=(v[i-1]+v[i-2])%1000000007
print(v[n])