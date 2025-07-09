l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0 :
  v = a // c
else :
  v = (a // c) + 1

if b % d == 0 :
  v2 = b // d
else :
  v2 = (b // d) + 1

print(l - max(v, v2))