import sys
d, k = map(int, sys.stdin.readline().rstrip().split())
v = [[0] * 2 for _ in range(d + 1)]
v[1][0] = 1
v[1][1] = 0
v[2][0] = 0
v[2][1] = 1
for i in range(3, d + 1):
    v[i][0] = v[i - 1][0] + v[i - 2][0]
    v[i][1] = v[i - 1][1] + v[i - 2][1]

for i in range(1, k):
    if (k - i * v[d][0]) % v[d][1] == 0:
        print(i)
        print((k - i * v[d][0]) // v[d][1])
        break