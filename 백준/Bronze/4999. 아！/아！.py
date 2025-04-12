import sys

sound = sys.stdin.readline().rstrip()
condition = sys.stdin.readline().rstrip()

if len(sound) >= len(condition):
    print("go")
else:
    print("no")