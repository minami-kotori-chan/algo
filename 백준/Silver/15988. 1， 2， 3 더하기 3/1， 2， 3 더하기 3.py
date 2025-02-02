import sys

t=int(sys.stdin.readline().rstrip())

max_num=1000000

v=[0]*(max_num+1)
v[1]=1
v[2]=2
v[3]=4

for i in range(4,max_num+1):
    for j in range(1,3+1):
        v[i]+=v[i-j]
    v[i]%=1000000009

for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    print(v[n])