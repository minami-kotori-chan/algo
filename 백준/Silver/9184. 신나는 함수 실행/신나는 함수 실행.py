import sys
v=[[[1]*21 for _ in range(21)]for _ in range(21)]
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j and j<k:
                v[i][j][k]=v[i][j][k-1]+v[i][j-1][k-1]-v[i][j-1][k]
                continue
            v[i][j][k]=v[i-1][j][k]+v[i-1][j-1][k]+v[i-1][j][k-1]-v[i-1][j-1][k-1]
while True:
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f"w({a}, {b}, {c}) = ",end='')
    if a<=0 or b<=0 or c<=0:
        print("1")
        continue
    if a>20 or b>20 or c>20:
        a=20
        b=20
        c=20
    
    print(v[a][b][c])