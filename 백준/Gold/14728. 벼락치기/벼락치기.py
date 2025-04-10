import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
k = [0]
s = [0]

for i in range(n):
    k_in, s_in = map(int, sys.stdin.readline().rstrip().split())
    k.append(k_in)
    s.append(s_in)

v = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        if j < k[i]:
            v[i][j] = v[i - 1][j]
            continue
        v[i][j] = max(v[i - 1][j - k[i]] + s[i], v[i - 1][j])

print(v[n][t])