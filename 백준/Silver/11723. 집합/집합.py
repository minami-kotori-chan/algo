import sys

n=int(sys.stdin.readline().rstrip())
s={}

for _ in range(n):
    input_op=sys.stdin.readline().rstrip().split()
    
    if len(input_op)>1:
        op_num=int(input_op[1])
    op_code=input_op[0]

    if op_code=='add':
        s[op_num]=0
    elif op_code=="remove":
        if op_num in s:
            s.pop(op_num)
    elif op_code=="check":
        if op_num in s:
            print(1)
        else:
            print(0)
    elif op_code=="toggle":
        if op_num in s:
            s.pop(op_num)
        else:
            s[op_num]=0
    elif op_code=="all":
        s={}
        for i in range(1,21):
            s[i]=0
    elif op_code=="empty":
        s={}
