import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    arr.append([s, e])

arr.sort()
v = [1] * n

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[i][1] > arr[j][1]:
            v[i] = max(v[i], v[j] + 1)

print(n - max(v))