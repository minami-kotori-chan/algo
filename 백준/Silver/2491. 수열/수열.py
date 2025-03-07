import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
v_up=[0]*n
v_down=[0]*n
v_up[0]=1
v_down[0]=1
for i in range(1,n):
    if arr[i]>arr[i-1]:
        v_up[i]=v_up[i-1]+1
        v_down[i]=1
    elif arr[i]==arr[i-1]:
        v_up[i]=v_up[i-1]+1
        v_down[i]=v_down[i-1]+1
    else:
        v_up[i]=1
        v_down[i]=v_down[i-1]+1
    
print(max(max(v_up),max(v_down)))