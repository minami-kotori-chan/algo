import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = set()
for i in range(n):
    arr.add(int(sys.stdin.readline().rstrip()))
v = [-1] * (k + 1)

for i in arr:
    if i <= k:
        v[i] = 1

    for j in range(i + 1, k + 1):
        if v[j] == -1 and v[j - i] == -1:
            continue
        if v[j] != -1 and v[j - i] != -1:
            v[j] = min(v[j], v[j - i] + 1)
        else:
            v[j] = max(v[j], v[j - i] + 1)
print(v[k])