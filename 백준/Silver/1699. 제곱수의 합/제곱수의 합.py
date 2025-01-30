import sys

n=int(sys.stdin.readline().rstrip())

numbers=[]
numbers.append(0)
v=[]
v.append(0)
for i in range(1,n+1):
    numbers.append(i)
    v.append(0)

v[1]=1
prev_max=1
for i in range(2,n+1):
    min_value=i
    for j in range(1,i+1):
        if j**2>i:
            break
        min_value=min(min_value,v[i-j**2]+1)
    v[i]=min_value
print(v[n])