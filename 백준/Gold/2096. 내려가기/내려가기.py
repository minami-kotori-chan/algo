import sys

n = int(sys.stdin.readline().rstrip())
arr = []
arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
v = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        v[i][j] = arr[0][j]

for i in range(1, n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    v[0][0], v[0][1], v[0][2] = min(v[0][0], v[0][1]) + arr[0], min(v[0][0], v[0][1], v[0][2]) + arr[1], min(v[0][1], v[0][2]) + arr[2]
    v[1][0], v[1][1], v[1][2] = max(v[1][0], v[1][1]) + arr[0], max(v[1][0], v[1][1], v[1][2]) + arr[1], max(v[1][1], v[1][2]) + arr[2]

print(max(v[1]), min(v[0]))