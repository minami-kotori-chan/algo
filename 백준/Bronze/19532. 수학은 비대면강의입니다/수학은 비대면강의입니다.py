import sys

a,b,c,d,e,f=map(int,sys.stdin.readline().rstrip().split())
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i+b*j==c and d*i+e*j==f:
            print(f"{i} {j}")