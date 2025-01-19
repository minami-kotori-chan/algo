import sys

n=sys.stdin.readline().rstrip()

result=[]
stack=[]
skip=0
for i in range(len(n)):
    if ord(n[i])>=ord('A') and ord(n[i])<=ord('Z'):
        print(n[i],end='')
    else:
        if stack:
            top=stack[-1]
            if n[i]=='(':
                stack.append(n[i])
            elif n[i]==')':
                out=''
                while stack:
                    out=stack.pop()
                    if out=='(':
                        break
                    print(out,end='')
            elif n[i]=='*' or n[i]=='/':
                while stack and (stack[-1]=='*'or stack[-1]=='/'):
                    print(stack.pop(),end='')
                stack.append(n[i])
            elif n[i]=='+' or n[i]=='-':
                while stack and stack[-1]!='(':
                    print(stack.pop(),end='')
                stack.append(n[i])
        else:
            stack.append(n[i])
while stack:
    cur_str=stack.pop()
    if cur_str!='(' and cur_str!=')':
        print(cur_str,end='')
