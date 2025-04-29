import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
if n*100>=m:
    print('Yes')
else:
    print('No')