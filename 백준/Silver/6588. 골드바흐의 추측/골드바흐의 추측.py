import sys

prime=[True]*(1000001)
prime[1]=False

for i in range(2,int(1000000**0.5)+1):
    if prime[i]==False:
        continue
    j=2
    while i*j<=1000000:
        prime[i*j]=False
        j+=1
while True:
    goldbach_check=False
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    for i in range(2,n):
        if prime[i]==True and prime[n-i]==True:
            print(f"{n} = {i} + {n-i}")
            goldbach_check=True
            break
    if goldbach_check==False:
        print("Goldbach's conjecture is wrong.")
    