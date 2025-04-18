import sys

result=0
n=int(sys.stdin.readline().rstrip())
result=n//5
if n%5!=0:
    result+=1
print(result)