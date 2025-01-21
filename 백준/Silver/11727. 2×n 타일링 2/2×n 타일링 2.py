import sys

n=int(sys.stdin.readline().rstrip())

data=[0]*(n+1)

def dp(n):
    if data[n]!=0:
        return data[n]
    if n==1:
        data[n]=1
        return 1
    elif n==2:
        data[n]=3
        return 3
    data[n]=(dp(n-1)+dp(n-2)+dp(n-2))%10007
    return data[n]

print(dp(n))