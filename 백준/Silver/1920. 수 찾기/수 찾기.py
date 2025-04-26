import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
arr.sort()
for i in map(int,sys.stdin.readline().rstrip().split()):
    pass
    result=0
    left=0
    right=n-1
    while left<=right:
        val=(left+right)//2
        if arr[val]==i:
            result=1
            break
        elif arr[val]<i:
            left=val+1
        else:
            right=val-1
    print(result)