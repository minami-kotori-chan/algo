import sys

def division(num):
    sum=num
    while num>0:
        sum+=num%10
        num//=10
    return sum

n = int(sys.stdin.readline().rstrip())
found=False
for i in range(1,n):
    if division(i)==n:
        print(i)
        found=True
        break
if found==False:
    print(0)