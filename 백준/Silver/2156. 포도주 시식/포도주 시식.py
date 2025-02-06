import sys
n=[]
n.append(0)
n_size=int(sys.stdin.readline().rstrip())
for i in range(n_size):
    n.append(int(sys.stdin.readline().rstrip()))
v=[[0]*3 for _ in range(n_size+1)]
v[1][0]=0
v[1][1]=n[1]
v[1][2]=n[1]
if n_size>1:
    v[2][0]=n[1]
    v[2][1]=n[2]
    v[2][2]=n[1]+n[2]
for i in range(3,n_size+1):
    v[i][0]=max(v[i-1][0],v[i-1][1],v[i-1][2])
    v[i][1]=max(v[i-2][0],v[i-2][1],v[i-2][2])+n[i]
    v[i][2]=n[i-1]+n[i]+max(v[i-3][0],v[i-3][1],v[i-3][2])
print(max(v[n_size][0],v[n_size][1],v[n_size][2]))