import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
least=arr[0]
result=0
for i in range(1,len(arr)):
    least=min(least,arr[i])
    result=max(arr[i]-least,result)
print(result)