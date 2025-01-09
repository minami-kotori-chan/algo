import sys

n=int(sys.stdin.readline().rstrip())

numbers=[]

for i in range(10001):
    numbers.append(0)
for i in range(n):
    numbers[(int(sys.stdin.readline().rstrip()))]+=1

for i in range(1,10001):
    if numbers[i]!=0:
        for j in range(numbers[i]):
            print(i)