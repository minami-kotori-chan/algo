import sys

def division(num):
    sum=num
    while num>0:
        sum+=num%10
        num//=10
    return sum

n = int(sys.stdin.readline().rstrip())

for i in range(1,n):
    if division(i)==n:
        print(i)
        break
    if i==(n-1):
        print(0)
        break
if n==1:
    print(0)
