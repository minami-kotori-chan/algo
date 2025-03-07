import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*11
v[1]=0
v[2]=1
v[3]=3
for i in range(4,11):
    result=0
    for j in range(i//2+1):
        result=max(result,v[j]+v[i-j]+(j*(i-j)))
    v[i]=result
print(v[n])