import sys

for i in range(int(sys.stdin.readline().rstrip())):

    n=int(sys.stdin.readline().rstrip())
    data=[0]*(n+1)

    def dp(n):
        if data[n]!=0:
            return data[n]
        elif n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 4
        data[n]=dp(n-1)+dp(n-2)+dp(n-3)
        return data[n]

    print(dp(n))