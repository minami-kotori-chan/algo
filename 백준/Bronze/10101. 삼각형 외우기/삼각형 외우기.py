import sys

b1=int(sys.stdin.readline().rstrip())
b2=int(sys.stdin.readline().rstrip())
b3=int(sys.stdin.readline().rstrip())

if b1+b2+b3!=180:
    print('Error')
elif b1==b2 and b1==b3:
    print('Equilateral')
elif b1!=b2 and b1!=b3 and b2!=b3:
    print('Scalene')
else:
    print('Isosceles')