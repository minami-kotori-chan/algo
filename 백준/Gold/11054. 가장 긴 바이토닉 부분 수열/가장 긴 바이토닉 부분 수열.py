import sys

n=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().rstrip().split()))
lis=[0]*n
lds=[0]*n

lis[0]=1
lds[n-1]=1
result=0
for i in range(1,n):
    lis_max=0
    for j in range(i):
        if numbers[i]>numbers[j]:
            lis_max=max(lis_max,lis[j])
    lis[i]=lis_max+1
for i in range(n-1,-1,-1):
    lds_max=0
    for j in range(n-1,i,-1):
        if numbers[i]>numbers[j]:
            lds_max=max(lds_max,lds[j])
    lds[i]=lds_max+1

result=0
for i in range(n):
    result=max(lis[i]+lds[i],result)
print(result-1)