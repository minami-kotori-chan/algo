import sys

m=int(sys.stdin.readline().rstrip())
n=int(sys.stdin.readline().rstrip())

sum=0
min=0
is_prime = True

for i in range(m,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime==True and i!=1:
        if sum==0:
            min=i
        sum+=i
    is_prime=True

if sum==0:
    print(-1)
else:
    print(f"{sum}\n{min}",end='')