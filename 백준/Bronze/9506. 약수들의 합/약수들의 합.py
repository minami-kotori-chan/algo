import sys
while True:
    a=int(sys.stdin.readline().rstrip())
    if a==-1:
        break
    sum=0
    num_check=False

    for i in range(1,a):
        if a%i==0:
            sum+=i

    if sum==a:
        print(f"{a} = 1 ",end='')
        for i in range(2,a):
            if a%i==0:
                print(f"+ {i} ",end='')
        print()
    else:
        print(f"{a} is NOT perfect.")