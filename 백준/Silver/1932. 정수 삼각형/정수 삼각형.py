import sys

n=int(sys.stdin.readline().rstrip())
numbers=[]
numbers.append([0])
v=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    numbers.append(list(map(int,sys.stdin.readline().rstrip().split())))

v[1][1]=numbers[1][0]

for i in range(1,n):
    for j in range(1,i+2):
        v[i+1][j]=max(v[i][j]+numbers[i+1][j-1],v[i][j-1]+numbers[i+1][j-1])

result=0

for i in range(1,n+1):
    result=max(result,v[n][i])

print(result)