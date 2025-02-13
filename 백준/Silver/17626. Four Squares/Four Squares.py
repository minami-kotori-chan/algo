import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*(n+1)

for i in range(1,n+1):
    result=0
    for j in range(1,int(i**(0.5))+1):
        if result==0:
            result=v[i-pow(j,2)]+1
            continue
        result=min(result,v[i-pow(j,2)]+1)
    v[i]=result

print(v[n])