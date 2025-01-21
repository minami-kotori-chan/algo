import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
l=int(sys.stdin.readline().rstrip())
sum=0
for i in map(int,sys.stdin.readline().rstrip().split()):
    l-=1
    sum+=(a**l)*i

result=[]
while sum>0:
    result.append(sum%b)
    sum//=b
for i in range(len(result)-1,-1,-1):
    print(result[i],end=' ')