import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
stack=[]
for i in range(n):
    stack.append(int(sys.stdin.readline().rstrip()))
v=len(stack)-1
while stack[v]>m and v!=0:
    v-=1
money=m
count=0
while money!=0:
    count+=money//stack[v]
    money=money%stack[v]
    v-=1
print(count)