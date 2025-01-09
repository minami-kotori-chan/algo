import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

min_value=-1
for i in range(n-8+1):
    for i2 in range(m-8+1):
        sum1=0
        for j in range(8):
            for k in range(8):
                if (j+k)%2==0:
                    check_char = 'W'
                else:
                    check_char = 'B'
                if arr[i+j][i2+k] !=check_char:
                    sum1+=1
        sum2=0
        for j in range(8):
            for k in range(8):
                if (j+k)%2==0:
                    check_char = 'B'
                else:
                    check_char = 'W'
                if arr[i+j][i2+k] !=check_char:
                    sum2+=1
        if min_value==-1:
            min_value=min(sum1,sum2)
        if min(sum1,sum2)<min_value:
            min_value=min(sum1,sum2)
print(min_value)
