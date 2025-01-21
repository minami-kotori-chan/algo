import sys

n=int(sys.stdin.readline().rstrip())

data=[0]*1001
data[1]=1
data[2]=2
def dp(n):
    if data[n]!=0:
        return data[n]
    data[n]=(dp(n-1)+dp(n-2))%10007
    return data[n]

print(dp(n))