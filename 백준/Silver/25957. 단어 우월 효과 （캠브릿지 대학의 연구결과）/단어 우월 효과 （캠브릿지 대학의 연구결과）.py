import sys

n=int(sys.stdin.readline().rstrip())
dic={}
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    alpha=[0]*26
    for i in word:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            alpha[ord(i)-ord('a')]+=1
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            alpha[ord(i)-ord('A')]+=1
    append_string=''
    for i in alpha:
        append_string+=str(i)
    dic[word[0]+word[-1]+append_string]=word
m=int(sys.stdin.readline().rstrip())
for i in (sys.stdin.readline().rstrip().split()):
    alpha=[0]*26
    for j in i:
        if ord(j)>=ord('a') and ord(j)<=ord('z'):
            alpha[ord(j)-ord('a')]+=1
        if ord(j)>=ord('A') and ord(j)<=ord('Z'):
            alpha[ord(j)-ord('A')]+=1
    append_string=''
    for j in alpha:
        append_string+=str(j)
    print(dic[i[0]+i[-1]+append_string],end=' ')