import sys
while True:
    b1,b2,b3 = map(int,sys.stdin.readline().rstrip().split())
    if b1==0 and b2==0 and b3==0:
        break
    if max(b1,b2,b3)>=(b1+b2+b3-max(b1,b2,b3)):
        print('Invalid')
    elif b1==b2 and b1==b3:
        print('Equilateral')
    elif b1!=b2 and b1!=b3 and b2!=b3:
        print('Scalene')
    else:
        print('Isosceles')