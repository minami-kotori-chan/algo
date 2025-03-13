import sys

n = int(sys.stdin.readline().rstrip())
arr = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
v = [[0] * 8 for _ in range(n + 1)]
v[0][0] = 1

for i in range(1, n + 1):
    for j in range(8):
        for k in arr[j]:
            v[i][j] += v[i - 1][k]
        v[i][j] %= 1000000007
print(v[n][0] % 1000000007)