import sys

s=sys.stdin.readline().rstrip()

strs=[]
for i in range(len(s)):
    append_string=''
    for j in range(i,len(s)):
        append_string+=s[j]
    strs.append(append_string)
strs.sort()
for i in strs:
    print(i)