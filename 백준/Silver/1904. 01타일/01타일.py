import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*n

v[0]=1
if n>1:
    v[1]=2

for i in range(2,n):
    v[i]=(v[i-1]+v[i-2])%15746
print(v[n-1])