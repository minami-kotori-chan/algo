import sys

n=int(sys.stdin.readline().rstrip())

s=[]
for i in range(n):
    s.append(list(sys.stdin.readline().rstrip().split()))
s.sort(key=lambda x:int(x[0]))
for i in s:
    print(*i)