import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

arr=[]
for i in map(int,sys.stdin.readline().rstrip().split()):
    arr.append(i)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            temp= arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print(arr[m-1])