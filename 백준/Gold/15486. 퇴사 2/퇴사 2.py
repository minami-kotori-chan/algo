import sys
n=int(sys.stdin.readline().rstrip())
num=[]
for i in range(n):
    num.append(list(map(int,sys.stdin.readline().rstrip().split())))

v=[0]*(n+1)
v_max=0
for i in range(n-1,-1,-1):
    if i+num[i][0]-1<n:
        v[i]=max(v_max,v[i+num[i][0]]+num[i][1])
    else:
        v[i]=v_max
    v_max=max(v_max,v[i])
print(max(v))