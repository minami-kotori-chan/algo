import sys

def reset_arr(arr):
    for i in range(len(arr)):
        arr[i]=0

n=int(sys.stdin.readline().rstrip())
alpha=[]

for i in range(ord('a'),ord('z')+1):
    alpha.append(0)

sum=0

for i in range(n):
    s=sys.stdin.readline().rstrip()
    alpha[ord(s[0])-ord('a')]+=1
    prev=s[0]
    check_sum=True
    for j in s:
        if prev!=j:
            if (alpha[ord(j)-ord('a')]==0):
                alpha[ord(j)-ord('a')]+=1
            else:
                check_sum=False
        prev=j
    if check_sum==True:
        sum+=1
    reset_arr(alpha)
print(sum)