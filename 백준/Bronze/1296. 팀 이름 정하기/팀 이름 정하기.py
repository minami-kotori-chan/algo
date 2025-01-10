import sys

name=sys.stdin.readline().rstrip()

s=[]

for i in range(int(sys.stdin.readline().rstrip())):
    s.append(sys.stdin.readline().rstrip())

dic = {}
for i in "LOVE":
    dic[i]=0

for i in name:
    if i in "LOVE":
        dic[i] += 1


max_match=-1
index=0
s.sort()
for i in range(len(s)):
    dic2=dic.copy()
    for j in s[i]:
        if j in "LOVE":
            dic2[j]+=1
    result=1
    key=list(dic2.keys())

    for j in range(len(key)):
        for k in range(j+1,len(key)):
            result*=(dic2[key[j]]+dic2[key[k]])
    result=result%100
    if max_match<result:
        max_match=result
        index=i

print(s[index])