n=int(input())
arr=list(map(int,input().split()))
result=0
for i in arr:
    if n==i:
        result+=1
print(result)