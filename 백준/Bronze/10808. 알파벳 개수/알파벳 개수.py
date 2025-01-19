import sys

n=sys.stdin.readline().rstrip()
alpha={}
for i in n:
    if i in alpha:
        alpha[i]+=1
    else:
        alpha[i]=1
for i in range(ord('a'),ord('z')+1):
    if chr(i)in alpha:
        print(alpha[chr(i)],end=' ')
    else:
        print(0,end=' ')