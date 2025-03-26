import sys

a=map(int,sys.stdin.readline().rstrip().split())
result=0
for i in a:
    result+=i**2
print(result%10)