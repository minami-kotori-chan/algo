import sys

n = int(sys.stdin.readline().rstrip())

broken=[]

m=int(sys.stdin.readline().rstrip())
if m>0:
    broken=list(map(int,sys.stdin.readline().rstrip().split()))

least_cost = abs(n-100)

if m<10:
    for i in range(n+least_cost+1):
        is_skip=False
        v=i
        count=1
        while v>=10:
            if (v%10) in broken:
                is_skip=True
                break
            count+=1
            v//=10
        if is_skip==True or (v in broken):
            continue
        least_cost=min(least_cost,abs(n-i)+count)
print(least_cost)