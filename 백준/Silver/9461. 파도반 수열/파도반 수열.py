import sys

v=[0]*(101)
v[1]=1
v[2]=1
v[3]=1
v[4]=2
for i in range(5,101):
    v[i]=v[i-1]+v[i-5]

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    print(v[n])