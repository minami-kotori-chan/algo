import sys

n=int(sys.stdin.readline().rstrip())

a=[]
a=list(map(int,sys.stdin.readline().rstrip().split()))

result=a[0]
prev_sum=a[0]

for i in range(1,n):
    prev_sum=max(prev_sum+a[i],a[i])
    result=max(prev_sum,result)

print(result)