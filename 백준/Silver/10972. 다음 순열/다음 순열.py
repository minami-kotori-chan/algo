import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
index=-1

for i in range(n-1,0,-1):
    if arr[i]>arr[i-1]:
        index=i
        break

if index==-1:
    print(-1)
else:
    for i in range(n-1,-1,-1):
        if arr[i]>arr[index-1]:
            arr[i],arr[index-1]=arr[index-1],arr[i]
            stack_left=[]
            stack_right=[]
            for j in range(n):
                if j>=index:
                    stack_right.append(arr[j])
                else:
                    stack_left.append(arr[j])
            stack_right.sort()
            print(*stack_left,end=' ')
            print(*stack_right)
            break