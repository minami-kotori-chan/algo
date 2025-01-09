import sys

def division(num):
    count=0
    while num>0:
        if num%10==6:
            count+=1
        else:
            count=0
        if count>=3:
            return True
        num//=10
    return False

n=int(sys.stdin.readline().rstrip())

sum=0
i=666
while True:
    if division(i):
        sum+=1
        if sum>=n:
            print(i)
            break
    i+=1