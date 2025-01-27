import sys

n=int(sys.stdin.readline().rstrip())
v=1
count_num=1

result=0
check_num=1
while v*10<=n:
    v*=10
    result+=(((v-1)-(v//10))+1)*count_num
    count_num+=1

result+=((n-v+1)*count_num)
print(result)