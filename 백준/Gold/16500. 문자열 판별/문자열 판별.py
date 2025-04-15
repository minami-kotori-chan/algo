import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

arr = []

for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

v = [0] * (len(s) + 1)
v[0] = 1

for i in range(1, len(s) + 1):
    for j in range(len(arr)):
        if i < len(arr[j]):
            continue

        is_valid = True

        for k in range(len(arr[j])):
            if arr[j][k] != s[i - len(arr[j]) + k]:
                is_valid = False
                break

        if is_valid == False:
            continue

        v[i] = max(v[i],v[i - len(arr[j])])

print(v[-1])