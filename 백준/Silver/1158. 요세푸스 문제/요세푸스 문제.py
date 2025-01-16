import sys

q=[]

n,k=map(int,sys.stdin.readline().rstrip().split())

for i in range(1,n+1):
    q.append(i)
num=k-1
q.pop(num)
print(f"<{k}",end='')
while q:
    num+=k-1
    if num>=len(q):
        num%=len(q)
    print(f", {q.pop(num)}",end='')
print(">")