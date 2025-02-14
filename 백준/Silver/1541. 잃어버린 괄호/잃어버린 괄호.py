import sys

result=0
prev_number=''
prev_operate='+'
is_minus=False
in_data=sys.stdin.readline().rstrip()
for i in in_data:
    if ord(i)>=ord('0') and ord(i)<=ord('9'):
        prev_number=prev_number+i
        continue
    if prev_operate=='+':
        result+=int(prev_number)
        if i=='-':
            prev_operate='-'
    else:
        result-=int(prev_number)
        prev_operate='-'
    prev_number=''
if prev_operate=='+':
    result+=int(prev_number)
else:
    result-=int(prev_number)
print(result)