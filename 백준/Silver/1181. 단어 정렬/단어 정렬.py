import sys

n=int(sys.stdin.readline().rstrip())

s=[]
for i in range(n):
    s.append(sys.stdin.readline().rstrip())

s.sort(key=lambda x:(len(x),x))
prev_str=False
for i in s:
    if prev_str==False or prev_str!=i:
        print(i)
        prev_str=i