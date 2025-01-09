import sys

n=int(sys.stdin.readline().rstrip())

numbers=[]
for i in range(10):
    numbers.append(0)

while n>0:
    numbers[n%10]+=1
    n//=10
for i in range(9,-1,-1):
    for j in range(numbers[i]):
        print(i,end='')