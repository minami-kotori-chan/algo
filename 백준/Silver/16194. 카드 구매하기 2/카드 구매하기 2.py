import sys

n = int(sys.stdin.readline().rstrip())
p=[]
val=[]
p.append(0)
val.append(0)
for i in map(int,sys.stdin.readline().rstrip().split()):
    p.append(i)
    val.append(i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n:
            break
        val[i+j]=min(val[i+j],val[i]+val[j])

print(val[n])