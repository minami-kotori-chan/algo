import sys

n=int(sys.stdin.readline().rstrip())
stack=[]
for i in range(n):
    word=sys.stdin.readline().rstrip().split()
    
    if word[0]=="push":
        stack.append(word[1])
    elif word[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif word[0]=="size":
        print(len(stack))
    elif word[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif word[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])