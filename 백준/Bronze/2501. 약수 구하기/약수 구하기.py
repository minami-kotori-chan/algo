import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
num=0
num_check=False
for i in range(1,a+1):
    if a%i==0:
        num+=1
        if num==b:
            print(i)
            num_check=True

if num_check==False:
    print(0)