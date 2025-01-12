import sys

a,b,c=map(int,sys.stdin.readline().rstrip().split())

if c==a+b:
    print("correct!")
else:
    print("wrong!")