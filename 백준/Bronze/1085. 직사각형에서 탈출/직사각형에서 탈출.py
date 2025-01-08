import sys

x,y,w,h=map(int,sys.stdin.readline().rstrip().split())
v1 = w-x
v2 = h-y
if v1<0:
    v1=-v1
if v2<0:
    v2=-v2
min=x
if min>y:
    min=y
if min>v1:
    min=v1
if min>v2:
    min=v2
print(min)