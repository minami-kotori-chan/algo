import sys

n, s, m = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
v = [[False] * (m + 1) for _ in range(n + 1)]

v[0][s] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        if v[i - 1][j]:
            if j + arr[i] <= m:
                v[i][j + arr[i]] = True
            if j - arr[i] >= 0:
                v[i][j - arr[i]] = True
result = -1
for i in range(m + 1):
    if v[n][i]:
        result = i
print(result)