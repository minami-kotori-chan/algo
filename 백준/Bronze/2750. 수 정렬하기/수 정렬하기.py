import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp= arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(len(arr)):
    print(arr[i])