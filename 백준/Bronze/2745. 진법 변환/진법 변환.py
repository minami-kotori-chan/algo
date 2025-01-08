import sys
n,b=sys.stdin.readline().rstrip().split()
b=int(b)
value=0
for i,s in enumerate(n):
    if ord(s)>=ord('A'):
        temp=ord(s)-ord('A')+10
    else:
        temp=int(s)
    value+=temp*(b**(len(n)-1-i))
print(value)