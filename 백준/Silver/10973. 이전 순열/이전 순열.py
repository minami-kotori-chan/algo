import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))

index=-1
for i in range(n-1,0,-1):
    if arr[i]<arr[i-1]:
        index=i-1
        break

if index==-1:
    print(-1)
else:
    for i in range(n-1,0,-1):
        if arr[i]<arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            break
    right_arr=[]
    for i in range(index+1,n):
        right_arr.append(arr[i])
    right_arr.sort()
    right_arr=right_arr[::-1]
    for i in range(n):
        if i<=index:
            print(arr[i],end=' ')
        else:
            print(right_arr[i-index-1],end=' ')