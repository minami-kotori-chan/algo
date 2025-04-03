import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
v = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            v[i][j] = v[i - 1][j - 1] + 1
        else:
            continue

result = 0
for i in v:
    for j in i:
        result = max(result, j)
print(result)