import sys

arr1=sys.stdin.readline().rstrip()
arr2=sys.stdin.readline().rstrip()

v=[[0]*(len(arr2)+1) for _ in range(len(arr1)+1)]

for i in range(1,len(arr1)+1):
    for j in range(1,len(arr2)+1):
        if arr1[i-1]==arr2[j-1]:
            v[i][j]=v[i-1][j-1]+1
        else:
            v[i][j]=max(v[i-1][j],v[i][j-1])
print(v[len(arr1)][len(arr2)])