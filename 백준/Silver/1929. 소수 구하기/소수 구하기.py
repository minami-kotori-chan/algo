import sys

m,n=map(int,sys.stdin.readline().rstrip().split())
result={}
for i in range(m,n+1):
    result[i]=0
for i in range(2,n+1):
    j=2
    while i*j<=n:
        if i*j in result:
            result[i*j]=1
        j+=1
for i in range(m,n+1):
    if result[i]==0 and i!=1:
        print(i)
