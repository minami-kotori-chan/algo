import sys

n = int(sys.stdin.readline().rstrip())

number=[[0]*10 for _ in range(n+1)]

for i in range(10):
    number[1][i]=1

for i in range(2,n+1):
    for j in range(1,10):
        if j==1:
            number[i][0]=number[i-1][1]
        if j+1<10:
            number[i][j]=(number[i-1][j-1]+number[i-1][j+1])%1000000000
        else:
            number[i][j]=(number[i-1][j-1]%1000000000)
        
result=0
for i in range(1,10):
    result=(result+number[n][i])%1000000000
print(result)