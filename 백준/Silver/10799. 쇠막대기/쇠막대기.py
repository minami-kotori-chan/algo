from collections import deque
import sys

in_str=sys.stdin.readline().rstrip()

prev_str=''
sum=0
cur_stick=0

for i in in_str:
    if i==')':
        cur_stick-=1
    elif i=='(':
        sum+=1
        cur_stick+=1
    if prev_str!='' and prev_str=='(' and i==')':
        sum-=1
        sum+=cur_stick
    prev_str=i
print(sum)