import sys

arr=sys.stdin.readline().rstrip()
v=[0]*(len(arr)+1)
v[0]=1
v[1]=1

for i in range(2,len(arr)+1):
    if arr[i-1]!='0':
        v[i]+=v[i-1]
    if arr[i-2]!='0' and int(arr[i-2])*10+int(arr[i-1])<=34:
        v[i]+=v[i-2]
print(v[len(arr)])