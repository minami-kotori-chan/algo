import sys

n=int(sys.stdin.readline().rstrip())
ab_n=abs(n)
v=[0]*(ab_n+1)
if n!=0:
    v[1]=1
for i in range(2,ab_n+1):
    v[i]=(v[i-1]+v[i-2])%1000000000
if n==0:
    print(0)
elif n<0 and ab_n%2==0:
    print(-1)
else:
    print(1)
print(v[ab_n])