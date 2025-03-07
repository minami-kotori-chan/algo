import sys

t=int(sys.stdin.readline().rstrip())
v=[0]*(t+1)
v[0]=1
for i in range(1,t+1):
    total=0
    for j in range(i):
        total+=(v[j]*v[i-j-1])
    v[i]=total
print(v[t])