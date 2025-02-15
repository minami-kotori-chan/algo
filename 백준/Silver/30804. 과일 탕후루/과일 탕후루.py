import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
left=0
right=0
result=0
numbers=[0]*10
numbers[arr[0]]=1
while right<n:
    count=0
    for i in range(10):
        if numbers[i]!=0:
            count+=1
    if count>2:
        numbers[arr[left]]-=1
        left+=1
    else:
        result=max(result,right-left+1)
        right+=1
        if right<n:
            numbers[arr[right]]+=1
print(result)