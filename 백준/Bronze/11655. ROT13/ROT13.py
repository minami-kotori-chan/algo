import sys

n=sys.stdin.readline().rstrip()

for i in n:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        if ord(i)+13 > ord('Z'):
            print(chr(ord(i)+13-ord('Z')+ord('A')-1),end='')
        else:
            print(chr(ord(i)+13),end='')
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
        if ord(i)+13 > ord('z'):
            print(chr(ord(i)+13-ord('z')+ord('a')-1),end='')
        else:
            print(chr(ord(i)+13),end='')
    else:
        print(i,end='')