import sys

n=int(sys.stdin.readline().rstrip())

numbers=[]
for i in range(n):
    numbers.append(list(map(int,sys.stdin.readline().rstrip().split())))

numbers.sort(key = lambda x:(x[1],x[0]))
for i in range(len(numbers)):
    print(f"{numbers[i][0]} {numbers[i][1]}")