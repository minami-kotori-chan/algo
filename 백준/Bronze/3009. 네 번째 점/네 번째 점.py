import sys
arr=[]
for i in range(3):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
if arr[0][0]==arr[1][0]:
    print(arr[2][0],end='')
if arr[0][0]==arr[2][0]:
    print(arr[1][0],end='')
if arr[1][0]==arr[2][0]:
    print(arr[0][0],end='')
print(' ',end='')
if arr[0][1]==arr[1][1]:
    print(arr[2][1],end='')
if arr[0][1]==arr[2][1]:
    print(arr[1][1],end='')
if arr[1][1]==arr[2][1]:
    print(arr[0][1],end='')