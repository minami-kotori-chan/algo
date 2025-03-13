import sys

n = int(sys.stdin.readline().rstrip())
r = sys.stdin.readline().rstrip()
v = [-1] * n
v[0] = 0
dic = {'B': 'J', 'O': 'B', 'J': 'O'}
for i in range(1, len(r)):
    for j in range(i):
        if v[j] == -1:
            continue
        if dic[r[i]] == r[j]:
            if v[i] == -1:
                v[i] = (j - i) ** 2 + v[j]
                continue
            v[i] = min(v[i], v[j] + (j - i) ** 2)
print(v[n - 1])