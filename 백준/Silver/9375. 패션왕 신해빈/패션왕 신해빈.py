import sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    dic={}
    for i in range(n):
        name,type=sys.stdin.readline().rstrip().split()
        if type in dic:
            dic[type]+=1
        else:
            dic[type]=1
    result=1
    for i in dic:
        result=result*(dic[i]+1)
    print(result-1)