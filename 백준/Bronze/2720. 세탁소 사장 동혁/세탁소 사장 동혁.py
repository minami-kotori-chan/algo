import sys
n=int(sys.stdin.readline().rstrip())

for i in range(n):
    t=int(sys.stdin.readline().rstrip())
    print(f"{t//25} {(t%25)//10} {((t%25)%10)//5} {((t%25)%10)%5}")