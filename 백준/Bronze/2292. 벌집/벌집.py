import sys
n=int(sys.stdin.readline().rstrip())
i=1
r_start=2
while r_start<=n:
    r_start+=(i*6)
    i+=1
print(i)