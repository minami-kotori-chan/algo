import sys

n=int(sys.stdin.readline().rstrip())
min=-1
for i in range((n//3)+1):
    for j in range((n//5)+1):
        if (i*3+j*5)==n:
            if min==-1 or min>(i+j):
                min = i+j
print(min)