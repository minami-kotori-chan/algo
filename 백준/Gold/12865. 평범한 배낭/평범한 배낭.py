from collections import deque
import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
w=[0]*(n+1)
w[0]=[0,0]
for i in range(1,n+1):
    in_w,in_v=map(int,sys.stdin.readline().rstrip().split())
    w[i]=[in_w,in_v]
memo=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,k+1):
    for j in range(1,n+1):
        if i-w[j][0]>=0:
            memo[j][i]=max(memo[j-1][i],memo[j-1][i-w[j][0]]+w[j][1])
        else:
            memo[j][i]=memo[j-1][i]
print(memo[n][k])