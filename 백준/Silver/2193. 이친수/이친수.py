import sys

n = int(sys.stdin.readline().rstrip())

number=[[0]*2 for _ in range(n+1)]

number[1][0]=1
number[1][1]=1

for i in range(2,n+1):
    for j in range(2):
        if j==0:
            number[i][j]=number[i-1][0]+number[i-1][1]
        else:
            number[i][j]=number[i-1][0]
print(number[n][1])