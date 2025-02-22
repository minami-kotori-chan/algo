import sys
N, M, K = map(int, sys.stdin.readline().rstrip().split())
n = K // M
m = K % M
print(n, m)