import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for _ in range(n + 1)]
v = [1] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[b].append(a)

for i in range(1, n + 1):
    for j in arr[i]:
        v[i] = max(v[i], v[j] + 1)

for i in range(1, n + 1):
    print(v[i], end=' ')