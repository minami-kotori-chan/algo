import sys

for i in range(int(sys.stdin.readline().rstrip())):
    syntax = sys.stdin.readline().rstrip().split()
    for j in syntax:
        for k in range(len(j)):
            print(j[len(j)-k-1],end='')
        print('',end=' ')
    print()