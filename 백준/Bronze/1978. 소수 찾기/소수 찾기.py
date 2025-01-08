import sys

n=int(sys.stdin.readline().rstrip())
sum=0
is_prime=True
for i in list(map(int,sys.stdin.readline().rstrip().split())):
    for j in range(2,i):
        if i%j==0:
            is_prime=False
    if i!=1 and is_prime==True:
        sum+=1
    else:
        is_prime=True
print(sum)