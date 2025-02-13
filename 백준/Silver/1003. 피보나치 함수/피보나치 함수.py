import sys


fibo=[[0]*2 for _ in range(41)]

fibo[0][0]=1
fibo[0][1]=0
fibo[1][0]=0
fibo[1][1]=1

for i in range(2,41):
    fibo[i][0]=fibo[i-1][0]+fibo[i-2][0]
    fibo[i][1]=fibo[i-1][1]+fibo[i-2][1]

n=int(sys.stdin.readline().rstrip())
for i in range(n):
    m=int(sys.stdin.readline().rstrip())
    print(f"{fibo[m][0]} {fibo[m][1]}")