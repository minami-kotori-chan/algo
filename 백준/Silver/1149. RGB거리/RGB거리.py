import sys

n=int(sys.stdin.readline().rstrip())

house=[]
v=[[0]*3 for _ in range(n)]

for _ in range(n):
    house.append(list(map(int,sys.stdin.readline().rstrip().split())))

v[0][0]=house[0][0]
v[0][1]=house[0][1]
v[0][2]=house[0][2]

for i in range(1,n):
    for j in range(3):
        min_stack=[]
        for k in range(3):
            if k==j:
                continue
            min_stack.append(v[i-1][k])
        min_value=min(min_stack[0],min_stack[1])

        v[i][j]=min_value+house[i][j]

result=v[n-1][0]

for i in range(3):
    result=min(v[n-1][i],result)
print(result)