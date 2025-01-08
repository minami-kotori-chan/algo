import sys
max,row,col=0,0,0
for i in range(9):
    arr=list(map(int,sys.stdin.readline().rstrip().split()))
    if i==0:
        max=arr[0]
    for j in range(len(arr)):
        if max<arr[j]:
            max=arr[j]
            row=i
            col=j
print(f"{max}\n{row+1} {col+1}")