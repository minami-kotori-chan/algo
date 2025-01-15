import sys

for i in range(int(sys.stdin.readline().rstrip())):
    syntax = sys.stdin.readline().rstrip()
    stack=[]
    response=1
    for j in syntax:
        if j == "(":
            stack.append(1)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                response=0
    if response==0 or stack:
        print("NO")
    else:
        print("YES")