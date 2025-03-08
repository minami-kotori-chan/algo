import sys
while True:
    n=sys.stdin.readline()
    if n=="":
        break
    n=int(n.rstrip())
    v=[0]*(n+1)
    v[0]=1
    if n>=1:
        v[1]=1
    if n>=2:
        v[2]=3
    for i in range(3,n+1):
        v[i]=v[i-2]*2+v[i-1]
    print(v[n])