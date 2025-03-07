import sys

v=[0]*68
v[0]=1
v[1]=1
v[2]=2
v[3]=4
for i in range(4,68):
    v[i]=v[i-1]+v[i-2]+v[i-3]+v[i-4]

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    print(v[int(sys.stdin.readline().rstrip())])