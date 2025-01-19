import sys

a,b,c,d=map(int,sys.stdin.readline().rstrip().split())

t1,t2=1,1
while t1<b:
    t1*=10
while t2<d:
    t2*=10
print(a*t1+b+c*t2+d)