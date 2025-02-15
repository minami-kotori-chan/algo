import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
right=0
left=0
for i in arr:
    right=max(right,i)
def calc_w(h):
    result=0
    for i in range(n):
        if arr[i]-h<=0:
            continue
        result+=(arr[i]-h)
    return result

while right>=left:
    mid=(right+left)//2
    w=calc_w(mid)
    if w>=m:
        left=mid+1
    else:
        right=mid-1
print(right)