import sys

tall=[]
sum=0
for i in range(9):
    tall.append(int(sys.stdin.readline().rstrip()))
    sum+=tall[i]
sum-=100

for i in range(9):
    for j in range(i+1,9):
        if tall[i]+tall[j]==sum:
            tall[i]=-1
            tall[j]=-1
            break
    if tall[i]==-1:
        break
tall.sort()

for i in tall:
    if i!=-1:
        print(i)