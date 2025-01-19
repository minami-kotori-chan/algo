import sys

prime=[True]*1000001
prime[1]=False
k=int(1000000**0.5)+1
for i in range(2,k):
    if prime[i]==False:
        continue
    for j in range(i*i,1000001,i):
        prime[j]=False
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
    