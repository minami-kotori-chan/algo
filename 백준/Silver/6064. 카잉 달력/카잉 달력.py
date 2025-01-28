import sys

n=int(sys.stdin.readline().rstrip())
for _ in range(n):
    m,n,x,y=map(int,sys.stdin.readline().rstrip().split())
    year=x
    if y==n:
        y=0
    while (year%n!=y) and year<=m*n:
        year+=m

    if year%n==y:
        print(year)
    else:
        print(-1)