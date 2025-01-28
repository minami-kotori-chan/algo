import sys

n=int(sys.stdin.readline().rstrip())
a=[]
a=list(map(int,sys.stdin.readline().rstrip().split()))
v=[0]*n
for i in range(n):
    max_number=1
    for j in range(i):
        if a[i]>a[j]:
            max_number=max(max_number,v[j]+1)
    v[i]=max_number
result_max=0
result_arr=[]
for i in range(n):
    result_max=max(result_max,v[i])
find_number=result_max
prev_num=0
while find_number>0:
    max_find=0
    for i in range(n):
        if (prev_num==0 and v[i]==find_number) or (v[i]==find_number and a[i]<prev_num):
            if max_find==0:
                max_find=a[i]
            max_find=max(max_find,a[i])
    result_arr.append(max_find)
    find_number-=1
    prev_num=max_find

print(result_max)
for i in range(len(result_arr)-1,-1,-1):
    print(result_arr[i],end=' ')