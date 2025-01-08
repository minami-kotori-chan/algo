import sys
row=[]
max=0
for i in range(5):
    row.append(sys.stdin.readline().rstrip())
for i in range(15):
    for j in range(5):
        if len(row[j])<=i:
            pass
        else :
            print(row[j][i],end='')