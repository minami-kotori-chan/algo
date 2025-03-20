import sys

n = sys.stdin.readline().rstrip()
v = [0] * (len(n) + 1)
v[0] = 1
v[1] = 1

if n[0] == '0':
    print(0)
else:
    for i in range(2, len(n) + 1):
        if int(n[i-1])!=0:
            v[i] += v[i - 1]
        if int(n[i - 1]) + int(n[i - 2]) * 10 <= 26 and int(n[i - 1]) + int(n[i - 2]) * 10 >= 10:
            v[i] += v[i - 2]
        v[i] %= 1000000
    print(v[len(n)])