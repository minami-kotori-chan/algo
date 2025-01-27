import sys

n = int(sys.stdin.readline().rstrip())
a=[]
a=list(map(int,sys.stdin.readline().rstrip().split()))
v=[0]*n
v[0]=1

for i in range(1,n):
    max_numbers=0
    for j in range(i):
        if a[i]>a[j]:
            max_numbers=max(max_numbers,v[j])
    v[i]=max_numbers+1
result=0
for i in range(n):
    result=max(result,v[i])
print(result)