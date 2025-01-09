import sys

n=int(sys.stdin.readline().rstrip())

s=[]
s=list(map(int,sys.stdin.readline().rstrip().split()))
arr=sorted(set(s))
dic = {arr[i]:i for i in range(len(arr))}

for i in s:
    print(dic[i],end=' ')