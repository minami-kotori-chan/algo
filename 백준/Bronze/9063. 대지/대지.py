import sys

n=int(sys.stdin.readline().rstrip())

for i in range(n):      
    x,y=(map(int,sys.stdin.readline().rstrip().split()))
    if i==0:
        max_x=x
        min_x=x
        max_y=y
        min_y=y
    if max_x<x:
        max_x=x
    if max_y<y:
        max_y=y
    if min_x>x:
        min_x=x
    if min_y>y:
        min_y=y
print((max_x-min_x)*(max_y-min_y))
