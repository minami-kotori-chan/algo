import sys

t=int(sys.stdin.readline().rstrip())

for x in range(t):
    m,p=map(int,sys.stdin.readline().rstrip().split())
    v=[0]*(m+1)
    v[1]=1
    if m>=2:
        v[2]=1
    for i in range(3,m+1):
        v[i]=(v[i-1]+v[i-2])%p
    print(f"Case #{x+1}: {v[m]%p}")