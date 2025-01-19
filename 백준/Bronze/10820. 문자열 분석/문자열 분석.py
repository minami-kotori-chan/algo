import sys


while True:
    n=sys.stdin.readline()
    nums=[0]*4
    if n=='':
        break
    for i in n:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            nums[1]+=1
        elif ord(i)>=ord('a') and ord(i)<=ord('z'):
            nums[0]+=1
        elif ord(i)>=ord('0') and ord(i)<=ord('9'):
            nums[2]+=1
        elif i==' ':
            nums[3]+=1
    print(*nums)
