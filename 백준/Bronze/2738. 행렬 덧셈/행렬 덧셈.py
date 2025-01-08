import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n*2):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(n):
    for j in range(m):
        print(arr[i][j]+arr[i+n][j],end=' ')
    print()