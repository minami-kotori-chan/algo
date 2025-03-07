import sys

n=int(sys.stdin.readline().rstrip())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    prev=2
    prev_prev=1
    result=0
    for i in range(3,n+1):
        result=(prev+prev_prev)%10
        prev_prev=prev
        prev=result
    print(result)