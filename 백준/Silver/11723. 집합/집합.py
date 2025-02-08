import sys

n=int(sys.stdin.readline().rstrip())
s=0

for _ in range(n):
    input_op=sys.stdin.readline().rstrip().split()
    
    if len(input_op)>1:
        op_num=int(input_op[1])
        op_bit=1<<(op_num-1)
    op_code=input_op[0]
    

    if op_code=='add':
        s=s | op_bit 
    elif op_code=="remove":
        s= s & (~op_bit)
    elif op_code=="check":
        if s & op_bit==op_bit:
            print(1)
        else:
            print(0)
    elif op_code=="toggle":
        s=s^op_bit
    elif op_code=="all":
        s=(1<<20)-1
    elif op_code=="empty":
        s=0