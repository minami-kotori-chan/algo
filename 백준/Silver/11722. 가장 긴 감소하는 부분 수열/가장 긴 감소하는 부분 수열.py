import sys

n=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().rstrip().split()))
v=[0]*n

v[0]=1

for i in range(1,n):
    max_num=0
    for j in range(i):
        if numbers[i]<numbers[j]:
            max_num=max(max_num,v[j])
    v[i]=max_num+1
result=0
for i in range(n):
    result=max(result,v[i])
print(result)