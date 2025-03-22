import sys

money, life  = map(int, sys.stdin.readline().rstrip().split())

print(money//life)
print(money%life)