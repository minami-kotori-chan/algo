import sys

n=int(sys.stdin.readline().rstrip())
v=[0]*(n+1)
if n>=2:
    v[2]=1
if n>=4:
    v[4]=2
if n>=5:
    v[5]=1
for i in range(6,n+1):
    two=v[i-2]+1
    if v[i-2]==0:
        two=0
    five=v[i-5]+1
    if v[i-5]==0:
        five=0
    v[i]=min(two,five)
    if two==0 or five==0:
        v[i]=max(two,five)
if v[n]==0:
    print(-1)
else:
    print(v[n])