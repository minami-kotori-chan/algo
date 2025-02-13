import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
sum=0
result=0
for i in range(n):
    sum+=arr[i]
    result+=sum
print(result)