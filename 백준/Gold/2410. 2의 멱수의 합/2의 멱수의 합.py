import sys

n = int(sys.stdin.readline().rstrip())
arr = [1]

for i in range(1, n + 1):
    if 2**i > n:
        break
    arr.append(2**i)

v = [0] * (n + 1)
v[0] = 1

for i in arr:
    for j in range(i, n + 1):
        v[j] = (v[j] + v[j - i]) % 1000000000
print(v[n])