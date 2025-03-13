import sys

t = int(sys.stdin.readline().rstrip())
v = [[0] * 10 for _ in range(1001)]
num = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [4, 8, 0], [5, 7, 9], [6, 8]]

for i in range(10):
    v[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for k in num[j]:
            v[i][j] += v[i - 1][k]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(sum(v[n])%1234567)