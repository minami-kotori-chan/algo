import sys

n=int(sys.stdin.readline().rstrip())
m=n
i=2
while m>1:
    if m%i==0:
        if m<=1:
            break
        m=m//i
        print(i)
        i=1
    i+=1