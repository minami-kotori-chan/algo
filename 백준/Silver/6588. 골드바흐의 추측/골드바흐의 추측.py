import sys

prime=[True]*1000001
prime_set=[]
prime[1]=False

for i in range(2,1000001):
    if prime[i]==True:
        prime_set.append(i)
    for j in prime_set:
        if i*j>1000000:
            break
        prime[i*j]=False
        if i%j==0:
            break
while True:
    goldbach_check=False
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    for i in prime_set:
        if prime[n-i]==True:
            print(f"{n} = {i} + {n-i}")
            goldbach_check=True
            break
    if goldbach_check==False:
        print("Goldbach's conjecture is wrong.")
    