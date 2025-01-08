import sys
n,b=map(int,sys.stdin.readline().rstrip().split())
i=1
while n%(b**i)!=n:
    i+=1
i-=1
value=n
while i>=0:
    v=value//(b**i)
    value=value%(b**i)
    if(v>=10):
        v=chr(v-10+ord('A'))
    print(v,end='')
    i-=1