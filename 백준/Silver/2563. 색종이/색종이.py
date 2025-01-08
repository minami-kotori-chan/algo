import sys
area = [[0]*101 for _ in range(101)]

n=int(sys.stdin.readline().rstrip())

for i in range(n):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            area[j][k]=1
count = 0
for i in range(101):
    for j in range(101):
        if area[i][j]==1:
            count+=1
print(count)