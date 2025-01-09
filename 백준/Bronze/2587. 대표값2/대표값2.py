import sys

arr=[]
sum=0
for i in range(5):
    arr.append(int(sys.stdin.readline().rstrip()))
    sum+=arr[i]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp= arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print(f"{int(sum/5)}\n{arr[2]}")