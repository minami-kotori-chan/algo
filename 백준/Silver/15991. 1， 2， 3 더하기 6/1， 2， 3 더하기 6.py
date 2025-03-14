import sys
t=int(sys.stdin.readline().rstrip())

v=[0]*(100001)
v[1]=1
v[2]=2
v[3]=2
v[4]=3
v[5]=3
v[6]=6
for i in range(7,100001):
    v[i]=(v[i-2]+v[i-4]+v[i-6])%1000000009
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    print(v[n])