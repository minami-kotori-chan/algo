import sys

n,a,b=map(int,sys.stdin.readline().rstrip().split())

if a < b:
    print("Bus")
elif a > b:
    print("Subway")
else:
    print("Anything")