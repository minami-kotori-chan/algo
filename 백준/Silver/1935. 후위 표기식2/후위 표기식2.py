import sys

n=int(sys.stdin.readline().rstrip())
calc=sys.stdin.readline().rstrip()
num=[]
stack=[]
result=0
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

for i in range(len(calc)):
    if ord(calc[i])>=ord('A') and ord(calc[i])<=ord('Z'):
        stack.append(num[ord(calc[i])-ord('A')])
    else:
        p2=stack.pop()
        p1=stack.pop()
        if calc[i]=='+':
            result=p1+p2
        elif calc[i]=='-':
            result=p1-p2
        elif calc[i]=='*':
            result=p1*p2
        elif calc[i]=='/':
            result=p1/p2
        stack.append(result)
print(f"{stack[0]:.2f}")