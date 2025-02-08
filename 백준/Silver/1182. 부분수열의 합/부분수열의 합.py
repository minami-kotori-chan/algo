from itertools import combinations
import sys

n,s=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
result=0
for i in range(1,n+1):
    c=combinations(arr,i)
    for i in c:
        sum=0
        for j in i:
            sum+=j
        if sum==s:
            result+=1
print(result)